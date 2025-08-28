from flask import Blueprint, request, jsonify
import requests

from add_sticker_impl import add_sticker_impl


bp = Blueprint('sticker', __name__)


@bp.route('/add_sticker', methods=['POST'])
def add_sticker():
    data = request.get_json()

    resource_id = data.get('sticker_id')
    start = data.get('start', 0)
    end = data.get('end', 5.0)
    draft_id = data.get('draft_id')
    transform_y = data.get('transform_y', 0)
    transform_x = data.get('transform_x', 0)
    alpha = data.get('alpha', 1.0)
    flip_horizontal = data.get('flip_horizontal', False)
    flip_vertical = data.get('flip_vertical', False)
    rotation = data.get('rotation', 0.0)
    scale_x = data.get('scale_x', 1.0)
    scale_y = data.get('scale_y', 1.0)
    track_name = data.get('track_name', 'sticker_main')
    relative_index = data.get('relative_index', 0)
    width = data.get('width', 1080)
    height = data.get('height', 1920)

    result = {
        "success": False,
        "output": "",
        "error": ""
    }

    if not resource_id:
        result["error"] = "Hi, the required parameter 'sticker_id' is missing. Please add it and try again. "
        return jsonify(result)

    try:
        draft_result = add_sticker_impl(
            resource_id=resource_id,
            start=start,
            end=end,
            draft_id=draft_id,
            transform_y=transform_y,
            transform_x=transform_x,
            alpha=alpha,
            flip_horizontal=flip_horizontal,
            flip_vertical=flip_vertical,
            rotation=rotation,
            scale_x=scale_x,
            scale_y=scale_y,
            track_name=track_name,
            relative_index=relative_index,
            width=width,
            height=height
        )

        result["success"] = True
        result["output"] = draft_result
        return jsonify(result)

    except Exception as e:
        result["error"] = f"Error occurred while adding sticker: {str(e)}. "
        return jsonify(result)



@bp.route('/search_sticker', methods=['POST'])
def search_sticker():
    data = request.get_json() or {}

    keywords = data.get('keywords')

    result = {
        "error": "",
        "output": {
            "data": [],
            "message": ""
        },
        "purchase_link": "",
        "success": False
    }

    if not keywords:
        result["error"] = "Hi, the required parameter 'keywords' is missing. Please add it and try again. "
        return jsonify(result)

    try:
        # Call external search API
        url = "https://lv-api-sinfonlineb.ulikecam.com/artist/v1/effect/search?aid=3704"
        payload = {
            "count": 50,
            "effect_type": 2,
            "need_recommend": False,
            "offset": 0,
            "query": keywords
        }
        headers = {
            "Content-Type": "application/json"
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        body = resp.json() or {}

        ret_code = str(body.get("ret", ""))
        errmsg = body.get("errmsg", "")
        data_section = (body.get("data") or {})
        items = data_section.get("effect_item_list") or []

        mapped_items = []
        for item in items:
            common = item.get("common_attr") or {}
            sticker = item.get("sticker") or {}

            large_image = (sticker.get("large_image") or {})
            sticker_package = (sticker.get("sticker_package") or {})

            # Determine sticker_id with fallbacks
            sticker_id = (
                str(common.get("effect_id") or "")
                or str(common.get("id") or "")
                or str(common.get("third_resource_id_str") or "")
                or (str(common.get("third_resource_id")) if common.get("third_resource_id") is not None else "")
            )

            mapped_items.append({
                "sticker": {
                    "large_image": {
                        "image_url": large_image.get("image_url", "")
                    },
                    "preview_cover": sticker.get("preview_cover", ""),
                    "sticker_package": {
                        "height_per_frame": int(sticker_package.get("height_per_frame", 0) or 0),
                        "size": int(sticker_package.get("size", 0) or 0),
                        "width_per_frame": int(sticker_package.get("width_per_frame", 0) or 0)
                    },
                    "sticker_type": int(sticker.get("sticker_type", 0) or 0),
                    "track_thumbnail": sticker.get("track_thumbnail", "")
                },
                "sticker_id": sticker_id,
                "title": common.get("title", "")
            })

        result["output"]["data"] = mapped_items
        result["output"]["message"] = errmsg or "success"
        result["success"] = (ret_code == "0")
        if not result["success"] and not result["error"]:
            result["error"] = errmsg or "Search failed"
        return jsonify(result)
    except Exception as e:
        result["error"] = f"Error occurred while searching sticker: {str(e)}. "
        return jsonify(result)
