#!/usr/bin/env python3
"""
Streaming-capable MCP server for CapCut API tools.

This server reuses the tool registry and execution logic defined in
`mcp_server.py` but exposes them through the `mcp` FastMCP server,
which supports stdio and SSE (HTTP) transports.
"""

import argparse
import sys
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP, Context
import mcp.types as types
from pydantic import BaseModel, Field, create_model

# Reuse tool schemas and executor from the existing implementation
from mcp_tools import TOOLS, execute_tool


def _json_type_to_py(type_name: str) -> Any:
    mapping: Dict[str, Any] = {
        "string": str,
        "number": float,
        "integer": int,
        "boolean": bool,
        "array": list[Any],
        "object": dict[str, Any],
    }
    return mapping.get(type_name, Any)


def _build_args_model(tool_name: str, input_schema: Dict[str, Any]) -> type[BaseModel]:
    properties: Dict[str, Dict[str, Any]] = input_schema.get("properties", {}) or {}
    required_fields = set(input_schema.get("required", []) or [])

    fields: Dict[str, tuple[Any, Any]] = {}
    for prop_name, prop_schema in properties.items():
        type_name = prop_schema.get("type", "string")
        py_type = _json_type_to_py(type_name)

        is_required = prop_name in required_fields
        has_default = "default" in prop_schema
        default_value = prop_schema.get("default", None)

        # Optional if not required
        annotated_type: Any = py_type if is_required else Optional[py_type]  # type: ignore[index]
        # Required fields without default use Ellipsis to mark required
        default = default_value if (is_required and has_default) else (None if not is_required else ...)
        fields[prop_name] = (
            annotated_type,
            Field(
                default,
                description=prop_schema.get("description"),
            ),
        )

    model_name = f"{tool_name}_Args"
    if not fields:
        # Fallback to an empty model
        return create_model(model_name)  # type: ignore[return-value]
    return create_model(model_name, **fields)  # type: ignore[return-value]


def _register_tools(app: FastMCP) -> None:
    """Dynamically register tools in FastMCP from the TOOLS spec."""
    for tool in TOOLS:
        name: str = tool.get("name", "")
        if not name:
            continue
        description: str = tool.get("description", "")
        input_schema: Dict[str, Any] = tool.get("inputSchema", {"type": "object"})
        ArgsModel = _build_args_model(name, input_schema)

        def make_handler(tool_name: str, args_model: type[BaseModel], desc: str):
            def _handler(params: args_model, ctx: Context):  # type: ignore[valid-type]
                arguments = params.model_dump(exclude_none=True) if isinstance(params, BaseModel) else {}
                return execute_tool(tool_name, arguments)

            app.add_tool(_handler, name=tool_name, description=desc)

        make_handler(name, ArgsModel, description)


def _override_list_tools(app: FastMCP) -> None:
    """Override list_tools to include inputSchema from TOOLS (and optional outputSchema)."""
    tool_map: Dict[str, Dict[str, Any]] = {t.get("name", ""): t for t in TOOLS if t.get("name")}

    @app._mcp_server.list_tools()  # type: ignore[attr-defined]
    async def list_tools() -> list[types.Tool]:
        result: list[types.Tool] = []
        for name, spec in tool_map.items():
            result.append(
                types.Tool(
                    name=name,
                    description=spec.get("description", ""),
                    inputSchema=spec.get("inputSchema", {"type": "object"}),
                    outputSchema=spec.get("outputSchema"),
                )
            )
        return result


def create_fastmcp_app(host: str = "127.0.0.1", port: int = 3333, path: str = "/mcp") -> FastMCP:
    """Factory to create a FastMCP app with tools registered and list_tools overridden."""
    app = FastMCP("capcut-api", host=host, port=port, streamable_http_path=path)
    _register_tools(app)
    _override_list_tools(app)
    return app


def main() -> None:
    parser = argparse.ArgumentParser(description="Streaming-capable MCP server for CapCut API")
    parser.add_argument("--host", default="127.0.0.1", help="streamable host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=3333, help="streamable port (default: 3333)")
    args = parser.parse_args()

    app = FastMCP("capcut-api", host=args.host, port=args.port)
    _register_tools(app)

    # _override_list_tools(app)

    print(f"Starting CapCut FastMCP SSE server on http://{args.host}:{args.port}", file=sys.stderr)
    app.run(transport="streamable-http", mount_path="/streamable")


if __name__ == "__main__":
    main()


