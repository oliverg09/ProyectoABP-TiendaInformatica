import flet as ft

class CustomButton(ft.Button):
    def __init__(self, text = None, icon = None, icon_color = None, color = None, bgcolor = None, content = None, elevation = None, style = None, autofocus = None, clip_behavior = None, url = None, url_target = None, on_click = None, on_long_press = None, on_hover = None, on_focus = None, on_blur = None, ref = None, key = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None, adaptive = None):
        super().__init__(text, icon, icon_color, color, bgcolor, content, elevation, style, autofocus, clip_behavior, url, url_target, on_click, on_long_press, on_hover, on_focus, on_blur, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, adaptive)
        self.style=ft.ButtonStyle(
            bgcolor={ft.ControlState.HOVERED: ft.Colors.BLACK},
        )
        self.color = "white"
        self.bgcolor = "#90A6C1"