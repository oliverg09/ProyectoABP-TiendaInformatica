import flet as ft


class Custom_Drop_Down(ft.Dropdown):
    def __init__(self, controls = None, value = None, bar_leading = None, bar_trailing = None, bar_hint_text = None, bar_bgcolor = None, bar_overlay_color = None, 
                 bar_shadow_color = None, bar_surface_tint_color = None, bar_elevation = None, bar_border_side = None, bar_shape = None, bar_text_style = None,
                   bar_hint_text_style = None, bar_padding = None, view_leading = None, view_trailing = None, view_elevation = None, view_bgcolor = None,
                     view_hint_text = None, view_side = None, view_shape = None, view_header_text_style = None, view_hint_text_style = None, view_size_constraints = None, view_header_height = None, divider_color = None, capitalization = None, full_screen = None, keyboard_type = None, view_surface_tint_color = None, autofocus = None, on_tap = None, on_tap_outside_bar = None, on_submit = None, on_change = None, on_focus = None, on_blur = None, ref = None, key = None, width = None, height = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None):
        super().__init__(controls, value, bar_leading, bar_trailing, bar_hint_text, bar_bgcolor, bar_overlay_color, bar_shadow_color, bar_surface_tint_color, bar_elevation, bar_border_side, bar_shape, bar_text_style, bar_hint_text_style, bar_padding, view_leading, view_trailing, view_elevation, view_bgcolor, view_hint_text, view_side, view_shape, view_header_text_style, view_hint_text_style, view_size_constraints, view_header_height, divider_color, capitalization, full_screen, keyboard_type, view_surface_tint_color, autofocus, on_tap, on_tap_outside_bar, on_submit, on_change, on_focus, on_blur, ref, key, width, height, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data)
        self.width = 256
        self.height = 32
        self.border_radius = 12
        self.fill_color="#CA9797"
        self.label_style=ft.TextStyle(color=ft.Colors.WHITE)