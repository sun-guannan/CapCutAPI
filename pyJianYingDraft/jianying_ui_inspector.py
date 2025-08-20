import uiautomation as auto
import json
from typing import Dict, List

class JianYingUIInspector:
    def __init__(self):
        self.jianying_window = None
        
    def find_jianying_window(self) -> bool:
        """查找剪映窗口"""
        # 尝试多种可能的窗口名称
        window_names = [
            "剪映",
            "JianYing", 
            "CapCut",
            "剪映专业版"
        ]
        
        for name in window_names:
            try:
                # 按窗口标题查找
                window = auto.WindowControl(searchDepth=1, Name=name)
                if window.Exists(0, 0):
                    self.jianying_window = window
                    print(f"找到剪映窗口: {name}")
                    return True
                    
                # 按类名查找（如果知道的话）
                window = auto.WindowControl(searchDepth=1, ClassName="Qt5QWindowIcon")
                if window.Exists(0, 0) and name.lower() in window.Name.lower():
                    self.jianying_window = window
                    print(f"找到剪映窗口: {window.Name}")
                    return True
            except Exception as e:
                continue
                
        # 如果按名称找不到，尝试遍历所有窗口
        print("按名称未找到，正在遍历所有窗口...")
        for window in auto.GetRootControl().GetChildren():
            if window.ControlType == auto.ControlType.WindowControl:
                window_title = window.Name
                if any(keyword in window_title for keyword in ["剪映", "JianYing", "CapCut"]):
                    self.jianying_window = window
                    print(f"找到剪映窗口: {window_title}")
                    return True
                    
        print("未找到剪映窗口，请确保剪映正在运行")
        return False
    
    def get_control_info(self, control) -> Dict:
        """获取控件的详细信息"""
        try:
            info = {
                "Name": control.Name,
                "ControlType": control.ControlTypeName,
                "ClassName": getattr(control, 'ClassName', ''),
                "AutomationId": getattr(control, 'AutomationId', ''),
                "BoundingRectangle": {
                    "left": control.BoundingRectangle.left,
                    "top": control.BoundingRectangle.top,
                    "right": control.BoundingRectangle.right,
                    "bottom": control.BoundingRectangle.bottom,
                    "width": control.BoundingRectangle.width(),
                    "height": control.BoundingRectangle.height()
                },
                "IsEnabled": control.IsEnabled,
                "IsVisible": getattr(control, 'IsOffscreen', True) == False,
                "ProcessId": getattr(control, 'ProcessId', 0)
            }
            
            # 获取FullDescription属性 (属性ID: 30159)
            try:
                if hasattr(control, 'GetCurrentPropertyValue'):
                    full_description = control.GetCurrentPropertyValue(30159)
                    info["FullDescription"] = full_description or ""
                else:
                    info["FullDescription"] = ""
            except Exception as e:
                info["FullDescription"] = ""
                info["FullDescriptionError"] = str(e)
            
            # 获取文本内容的多种方式
            text_content = ""
            
            # 方式1: 通过Value属性获取
            try:
                if hasattr(control, 'GetValuePattern'):
                    value_pattern = control.GetValuePattern()
                    if value_pattern:
                        text_content = value_pattern.Value
            except:
                pass
                
            # 方式2: 通过Text属性获取
            try:
                if hasattr(control, 'GetTextPattern'):
                    text_pattern = control.GetTextPattern()
                    if text_pattern:
                        text_content = text_pattern.DocumentRange.GetText(-1)
            except:
                pass
                
            # 方式3: 直接通过属性获取
            try:
                if not text_content and hasattr(control, 'CurrentValue'):
                    text_content = str(control.CurrentValue)
            except:
                pass
                
            # 方式4: 通过LegacyIAccessible获取
            try:
                if not text_content and hasattr(control, 'GetLegacyIAccessiblePattern'):
                    legacy_pattern = control.GetLegacyIAccessiblePattern()
                    if legacy_pattern:
                        text_content = legacy_pattern.CurrentValue or legacy_pattern.CurrentName
            except:
                pass
                
            # 方式5: 对于QML控件，尝试获取特定属性
            try:
                if not text_content and "QQuickText" in info["ClassName"]:
                    # QML Text控件可能需要特殊处理
                    if hasattr(control, 'GetCurrentPropertyValue'):
                        # 尝试获取Text属性
                        text_content = control.GetCurrentPropertyValue(auto.PropertyId.ValueValueProperty)
            except:
                pass
                
            info["TextContent"] = text_content or ""
            info["HasText"] = bool(text_content)
            
            # 原有的其他属性获取
            try:
                info["Value"] = control.GetValuePattern().Value if hasattr(control, 'GetValuePattern') else ""
            except:
                info["Value"] = ""
                
            try:
                info["IsSelected"] = control.GetSelectionItemPattern().IsSelected if hasattr(control, 'GetSelectionItemPattern') else False
            except:
                info["IsSelected"] = False
                
            return info
        except Exception as e:
            return {"Error": str(e), "Name": "获取信息失败"}
    
    def build_ui_tree(self, control, max_depth: int = 10, current_depth: int = 0) -> Dict:
        """递归构建UI元素树"""
        if current_depth >= max_depth:
            return {"MaxDepthReached": True}
            
        node = self.get_control_info(control)
        node["Depth"] = current_depth
        node["Children"] = []
        
        try:
            children = control.GetChildren()
            for child in children:
                if child.Exists(0, 0):  # 检查子控件是否存在
                    child_node = self.build_ui_tree(child, max_depth, current_depth + 1)
                    node["Children"].append(child_node)
        except Exception as e:
            node["ChildrenError"] = str(e)
            
        return node
    
    def print_ui_tree(self, node: Dict, indent: str = ""):
        """打印UI树结构"""
        control_type = node.get("ControlType", "Unknown")
        name = node.get("Name", "")
        class_name = node.get("ClassName", "")
        automation_id = node.get("AutomationId", "")
        full_description = node.get("FullDescription", "")
        
        # 构建显示文本
        display_parts = [control_type]
        if name:
            display_parts.append(f'Name="{name}"')
        if class_name:
            display_parts.append(f'Class="{class_name}"')
        if automation_id:
            display_parts.append(f'Id="{automation_id}"')
        if full_description:
            # 限制FullDescription显示长度，避免输出过长
            desc_display = full_description[:100] + "..." if len(full_description) > 100 else full_description
            display_parts.append(f'FullDesc="{desc_display}"')
            
        display_text = " ".join(display_parts)
        
        # 添加位置信息
        if "BoundingRectangle" in node:
            rect = node["BoundingRectangle"]
            display_text += f" [{rect['left']},{rect['top']},{rect['width']}x{rect['height']}]"
            
        print(f"{indent}{display_text}")
        
        # 递归打印子节点
        for child in node.get("Children", []):
            self.print_ui_tree(child, indent + "  ")
    
    def save_ui_tree_to_file(self, tree: Dict, filename: str = "jianying_ui_tree.json"):
        """保存UI树到文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(tree, f, ensure_ascii=False, indent=2)
            print(f"UI树已保存到: {filename}")
        except Exception as e:
            print(f"保存文件失败: {e}")
    
    def find_elements_by_type(self, tree: Dict, control_type: str) -> List[Dict]:
        """按控件类型查找元素"""
        results = []
        
        if tree.get("ControlType") == control_type:
            results.append(tree)
            
        for child in tree.get("Children", []):
            results.extend(self.find_elements_by_type(child, control_type))
            
        return results
    
    def find_elements_by_name(self, tree: Dict, name: str) -> List[Dict]:
        """按名称查找元素"""
        results = []
        
        if name.lower() in tree.get("Name", "").lower():
            results.append(tree)
            
        for child in tree.get("Children", []):
            results.extend(self.find_elements_by_name(child, name))
            
        return results
    
    def find_text_controls(self, tree: Dict) -> List[Dict]:
        """查找所有包含文本的控件"""
        results = []
        
        if tree.get("HasText") and tree.get("TextContent"):
            results.append({
                "ControlType": tree.get("ControlType"),
                "Name": tree.get("Name"),
                "ClassName": tree.get("ClassName"),
                "TextContent": tree.get("TextContent"),
                "BoundingRectangle": tree.get("BoundingRectangle")
            })
            
        for child in tree.get("Children", []):
            results.extend(self.find_text_controls(child))
            
        return results
    
    def inspect_jianying_ui(self, max_depth: int = 8, save_to_file: bool = True):
        """检查剪映UI并显示元素树"""
        print("正在查找剪映窗口...")
        
        if not self.find_jianying_window():
            return None
            
        print(f"窗口信息: {self.jianying_window.Name}")
        print(f"窗口位置: {self.jianying_window.BoundingRectangle}")
        print("\n正在构建UI元素树...")
        
        # 构建UI树
        ui_tree = self.build_ui_tree(self.jianying_window, max_depth)
        
        print("\n=== 剪映UI元素树 ===")
        self.print_ui_tree(ui_tree)
        
        if save_to_file:
            self.save_ui_tree_to_file(ui_tree)
            
        return ui_tree
    
    def list_all_windows(self):
        """列出所有窗口，帮助调试"""
        print("当前所有窗口:")
        for window in auto.GetRootControl().GetChildren():
            if window.ControlType == auto.ControlType.WindowControl:
                try:
                    print(f"- {window.Name} (PID: {getattr(window, 'ProcessId', 'Unknown')})")
                except:
                    print(f"- 无法获取窗口信息")

def main():
    """主函数"""
    inspector = JianYingUIInspector()
    
    # 如果找不到剪映窗口，先列出所有窗口
    if not inspector.find_jianying_window():
        print("\n列出所有窗口以供参考:")
        inspector.list_all_windows()
        return
    
    # 检查UI
    ui_tree = inspector.inspect_jianying_ui(max_depth=6, save_to_file=True)
    
    if ui_tree:
        # 示例：查找所有按钮
        buttons = inspector.find_elements_by_type(ui_tree, "ButtonControl")
        print(f"\n找到 {len(buttons)} 个按钮控件")
        
        # 示例：查找包含"导出"的元素
        export_elements = inspector.find_elements_by_name(ui_tree, "导出")
        if export_elements:
            print(f"\n找到 {len(export_elements)} 个包含'导出'的元素:")
            for elem in export_elements:
                print(f"  - {elem.get('ControlType')}: {elem.get('Name')}")
        
        # 新增：查找所有包含文本的控件
        text_controls = inspector.find_text_controls(ui_tree)
        if text_controls:
            print(f"\n找到 {len(text_controls)} 个包含文本的控件:")
            for ctrl in text_controls:
                print(f"  - {ctrl['ControlType']}: '{ctrl['TextContent']}'")

if __name__ == "__main__":
    main()