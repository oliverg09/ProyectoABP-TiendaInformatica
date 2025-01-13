import flet as ft
from services.crud_operations import modificarProducto,eliminarProducto


class CustomButton(ft.Button):
    def __init__(self, text = None, icon = None, icon_color = None, color = None, bgcolor = None, content = None, elevation = None, style = None, autofocus = None, clip_behavior = None, url = None, url_target = None, on_click = None, on_long_press = None, on_hover = None, on_focus = None, on_blur = None, ref = None, key = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None, adaptive = None):
        super().__init__(text, icon, icon_color, color, bgcolor, content, elevation, style, autofocus, clip_behavior, url, url_target, on_click, on_long_press, on_hover, on_focus, on_blur, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, adaptive)
        self.style=ft.ButtonStyle(
            bgcolor={ft.ControlState.HOVERED: ft.Colors.BLACK},
        )
        self.color = "white"
        self.bgcolor = "#90A6C1"
        

class diseñoBoton(ft.Button):
    def __init__(self, text = None, icon = None, icon_color = None, color = None, bgcolor = None, content = None, elevation = None, style = None, autofocus = None, clip_behavior = None, url = None, url_target = None, on_click = None, on_long_press = None, on_hover = None, on_focus = None, on_blur = None, ref = None, key = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None, adaptive = None):
        super().__init__(text, icon, icon_color, color, bgcolor, content, elevation, style, autofocus, clip_behavior, url, url_target, on_click, on_long_press, on_hover, on_focus, on_blur, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, adaptive)
        self.style=ft.ButtonStyle(
            bgcolor={ft.ControlState.HOVERED: ft.Colors.BLACK},
        )
        self.color = "white"
        self.bgcolor = "#90A6C1"

class txtDesplegable(ft.Dropdown):
    def __init__(self, controls = None, value = None, bar_leading = None, bar_trailing = None, bar_hint_text = None, bar_bgcolor = None, bar_overlay_color = None, 
                 bar_shadow_color = None, bar_surface_tint_color = None, bar_elevation = None, bar_border_side = None, bar_shape = None, bar_text_style = None,
                   bar_hint_text_style = None, bar_padding = None, view_leading = None, view_trailing = None, view_elevation = None, view_bgcolor = None,
                     view_hint_text = None, view_side = None, view_shape = None, view_header_text_style = None, view_hint_text_style = None, view_size_constraints = None, view_header_height = None, divider_color = None, capitalization = None, full_screen = None, keyboard_type = None, view_surface_tint_color = None, autofocus = None, on_tap = None, on_tap_outside_bar = None, on_submit = None, on_change = None, on_focus = None, on_blur = None, ref = None, key = None, width = None, height = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None):
        super().__init__(controls, value, bar_leading, bar_trailing, bar_hint_text, bar_bgcolor, bar_overlay_color, bar_shadow_color, bar_surface_tint_color, bar_elevation, bar_border_side, bar_shape, bar_text_style, bar_hint_text_style, bar_padding, view_leading, view_trailing, view_elevation, view_bgcolor, view_hint_text, view_side, view_shape, view_header_text_style, view_hint_text_style, view_size_constraints, view_header_height, divider_color, capitalization, full_screen, keyboard_type, view_surface_tint_color, autofocus, on_tap, on_tap_outside_bar, on_submit, on_change, on_focus, on_blur, ref, key, width, height, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data)
        self.width = 300
        self.height = 60
        self.border_radius = 12
        self.fill_color="#CA9797"
        self.label_style=ft.TextStyle(color=ft.Colors.WHITE)
        self.options = []
        self.bgcolor="#CA9797"
        self.max_menu_height = 200
        


class txtInput(ft.TextField):
    def __init__(self, value = None, keyboard_type = None, multiline = None, min_lines = None, max_lines = None, max_length = None, password = None, can_reveal_password = None, read_only = None, shift_enter = None, text_align = None, autofocus = None, capitalization = None, autocorrect = None, enable_suggestions = None, smart_dashes_type = None, smart_quotes_type = None, show_cursor = None, cursor_color = None, cursor_error_color = None, cursor_width = None, cursor_height = None, cursor_radius = None, selection_color = None, input_filter = None, obscuring_character = None, enable_interactive_selection = None, enable_ime_personalized_learning = None, can_request_focus = None, ignore_pointers = None, enable_scribble = None, animate_cursor_opacity = None, always_call_on_tap = None, scroll_padding = None, clip_behavior = None, keyboard_brightness = None, mouse_cursor = None, strut_style = None, autofill_hints = None, on_change = None, on_click = None, on_submit = None, on_focus = None, on_blur = None, text_size = None, text_style = None, text_vertical_align = None, label = None, label_style = None, icon = None, border = None, color = None, bgcolor = None, border_radius = None, border_width = None, border_color = None, focused_color = None, focused_bgcolor = None, focused_border_width = None, focused_border_color = None, content_padding = None, dense = None, filled = None, fill_color = None, hover_color = None, hint_text = None, hint_style = None, helper = None, helper_text = None, helper_style = None, counter = None, counter_text = None, counter_style = None, error = None, error_text = None, error_style = None, prefix = None, prefix_icon = None, prefix_text = None, prefix_style = None, suffix = None, suffix_icon = None, suffix_text = None, suffix_style = None, focus_color = None, align_label_with_hint = None, hint_fade_duration = None, hint_max_lines = None, helper_max_lines = None, error_max_lines = None, prefix_icon_size_constraints = None, suffix_icon_size_constraints = None, size_constraints = None, collapsed = None, fit_parent_size = None, ref = None, key = None, width = None, height = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None,
                  animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None, 
                  rtl = None, adaptive = None):
        super().__init__(value, keyboard_type, multiline, min_lines, max_lines, max_length, password, can_reveal_password, read_only, shift_enter, text_align, autofocus, capitalization, autocorrect, enable_suggestions, smart_dashes_type, smart_quotes_type, show_cursor, cursor_color, cursor_error_color, cursor_width, cursor_height, cursor_radius, selection_color, input_filter, obscuring_character, enable_interactive_selection, enable_ime_personalized_learning, can_request_focus, ignore_pointers, enable_scribble, animate_cursor_opacity, always_call_on_tap, scroll_padding, clip_behavior, keyboard_brightness, mouse_cursor, strut_style, autofill_hints, on_change, on_click, on_submit, on_focus, on_blur, text_size, text_style, text_vertical_align, label, label_style, icon, border, color, bgcolor, border_radius, border_width, border_color, focused_color, focused_bgcolor, focused_border_width, focused_border_color, content_padding, dense, filled, fill_color, hover_color, hint_text, hint_style, helper, helper_text, helper_style, counter, counter_text, counter_style, error, error_text, error_style, prefix, prefix_icon, prefix_text, prefix_style, suffix, suffix_icon, suffix_text, suffix_style, focus_color, align_label_with_hint, hint_fade_duration, hint_max_lines, helper_max_lines, error_max_lines, prefix_icon_size_constraints, suffix_icon_size_constraints, size_constraints, collapsed, fit_parent_size, ref, key, width, height, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, rtl, adaptive)
        self.width = 300
        self.height = 60
        self.color = "white"
        self.bgcolor="#CA9797"
        self.border_radius = 12

class txtDesplegableBusqueda(ft.SearchBar):
    def __init__(self, controls = None, value = None, bar_leading = None, bar_trailing = None, bar_hint_text = None, 
                 bar_bgcolor = None, bar_overlay_color = None, bar_shadow_color = None, bar_surface_tint_color = None, 
                 bar_elevation = None, bar_border_side = None, bar_shape = None, bar_text_style = None, bar_hint_text_style = None, 
                 bar_padding = None, view_leading = None, view_trailing = None, view_elevation = None, view_bgcolor = None, view_hint_text = None, view_side = None, view_shape = None, view_header_text_style = None, view_hint_text_style = None, view_size_constraints = None, view_header_height = None, divider_color = None, capitalization = None, full_screen = None, keyboard_type = None, view_surface_tint_color = None, autofocus = None, on_tap = None, on_tap_outside_bar = None, on_submit = None, on_change = None, on_focus = None, on_blur = None, ref = None, key = None, width = None, height = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None):
        super().__init__(controls, value, bar_leading, bar_trailing, bar_hint_text, bar_bgcolor, bar_overlay_color, bar_shadow_color, bar_surface_tint_color, bar_elevation, bar_border_side, bar_shape, bar_text_style, bar_hint_text_style, bar_padding, view_leading, view_trailing, view_elevation, view_bgcolor, view_hint_text, view_side, view_shape, view_header_text_style, view_hint_text_style, view_size_constraints, view_header_height, divider_color, capitalization, full_screen, keyboard_type, view_surface_tint_color, autofocus, on_tap, on_tap_outside_bar, on_submit, on_change, on_focus, on_blur, ref, key, width, height, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data)
        self.width = 300
        self.height = 50
        self.bar_hint_text_style=ft.TextStyle(color=ft.Colors.WHITE)
        self.view_hint_text_style = ft.TextStyle(color=ft.Colors.WHITE)
        self.view_header_text_style = ft.TextStyle(color=ft.Colors.WHITE)
        self.view_hint_text = "Categorias..."
        self.bar_hint_text = "Categorias..."
        self.controls = []
        self.bar_bgcolor="#CA9797"
        self.view_bgcolor="#CA9797"
        self.on_tap=self.abrir
        self.bar_shape = ft.RoundedRectangleBorder(radius=12)
        self.bar_border_side = ft.BorderSide(1,ft.Colors.BLACK)
        self.bar_shadow_color = {ft.ControlState.DEFAULT:ft.Colors.with_opacity(0.2,ft.Colors.WHITE)}
        self.view_size_constraints = ft.BoxConstraints(max_height=250)
        
    def cerrar(self,e):
        controlIndex = e.control.data
        texto = self.controls[controlIndex].title
        self.close_view(texto)

    def abrir(self,e):
        self.open_view()


class Producto_Administrador(ft.Container):
    
    def __init__(self, nombre, precio, marca, imagen, stock,ancho=100,alto=100 ,content = None, padding = None, margin = None, alignment = None, bgcolor = None, gradient = None, blend_mode = None, border = None, border_radius = None, image_src = None, image_src_base64 = None, image_repeat = None, image_fit = None, image_opacity = None, shape = None, clip_behavior = None, ink = None, image = None, ink_color = None, animate = None, blur = None, shadow = None, url = None, url_target = None, theme = None, theme_mode = None, color_filter = None, ignore_interactions = None, foreground_decoration = None, on_click = None, on_tap_down = None, on_long_press = None, on_hover = None, ref = None, key = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None, rtl = None, adaptive = None):
        super().__init__(content, padding, margin, alignment, bgcolor, gradient, blend_mode, border, border_radius, image_src, image_src_base64, image_repeat, image_fit, image_opacity, shape, clip_behavior, ink, image, ink_color, animate, blur, shadow, url, url_target, theme, theme_mode, color_filter, ignore_interactions, foreground_decoration, on_click, on_tap_down, on_long_press, on_hover, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, rtl, adaptive)
        self.nombre =  ft.Text(nombre,size=alto * 20 // 100,color=ft.Colors.BLACK)
        self.precio = ft.Text(precio,size=alto * 20 // 100,color=ft.Colors.BLACK)
        self.marca = ft.Text(marca,size=alto * 20 // 100,color=ft.Colors.BLACK)
        self.imagen =  ft.Container(expand=True,content=ft.Image(src_base64=imagen,width=ancho, height=alto,fit=ft.ImageFit.FILL,expand=True),border = ft.border.all(1,ft.Colors.BLACK))
        self.stock = ft.Text(stock,size=alto * 20 // 100,color=ft.Colors.BLACK)

        self.btonEditar = CustomButton("Editar",on_click=self.clickBotonEditar) 
        self.btonEditar.height = alto * 30 // 100
        self.btonEditar.text_style = ft.TextStyle(size=alto * 14 // 100)

        self.btonEliminar = CustomButton("Eliminar",on_click=self.clickBotonEliminar)
        self.btonEliminar.height = alto * 30 // 100
        self.btonEliminar.text_style = ft.TextStyle(size=alto * 14 // 100)


        self.bgcolor=ft.colors.WHITE
        self.border = ft.border.all(1,ft.Colors.BLACK)
        self.content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.imagen], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(
                            controls = [self.nombre,self.marca],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        ft.Row(
                            controls = [self.precio,self.stock],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        ft.Row(
                            controls = [
                                ft.Column(controls=[self.btonEditar],alignment=ft.MainAxisAlignment.START),
                                ft.Column(controls=[self.btonEliminar],alignment=ft.MainAxisAlignment.CENTER),
                                
                                ],alignment=ft.MainAxisAlignment.CENTER),
                    ]
                )
    def clickBotonEditar(self,e): 
        from views.panel_view_empleado import Panel_Window_Empleado
        Panel_Window_Empleado.clickBotonEditar(self,e)
        
        
    def clickBotonEliminar(self,e):
        nombreProducto = self.nombre.value
        modificarProducto({"nombre":nombreProducto},{'$inc':{'stock':-1}})
        self.stock.value -= 1
        if self.stock.value <= 0:
            self.parent.controls.remove(self)
            eliminarProducto({"nombre":nombreProducto})
        self.parent.update()

class Producto_Cliente(ft.Container):
    def __init__(self, nombre, precio, marca, imagen, stock,ancho=100,alto=100, content = None, padding = None, margin = None, alignment = None, bgcolor = None, gradient = None, blend_mode = None, border = None, border_radius = None, image_src = None, image_src_base64 = None, image_repeat = None, image_fit = None, image_opacity = None, shape = None, clip_behavior = None, ink = None, image = None, ink_color = None, animate = None, blur = None, shadow = None, url = None, url_target = None, theme = None, theme_mode = None, color_filter = None, ignore_interactions = None, foreground_decoration = None, on_click = None, on_tap_down = None, on_long_press = None, on_hover = None, ref = None, key = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None, rtl = None, adaptive = None):
        super().__init__(content, padding, margin, alignment, bgcolor, gradient, blend_mode, border, border_radius, image_src, image_src_base64, image_repeat, image_fit, image_opacity, shape, clip_behavior, ink, image, ink_color, animate, blur, shadow, url, url_target, theme, theme_mode, color_filter, ignore_interactions, foreground_decoration, on_click, on_tap_down, on_long_press, on_hover, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, rtl, adaptive)
        self.nombre =  ft.Text(nombre,color=ft.Colors.BLACK)
        self.precio = ft.Text(precio,color=ft.Colors.BLACK)
        self.marca = ft.Text(marca,color=ft.Colors.BLACK)
        self.imagen =  ft.Container(expand=True,content=ft.Image(src_base64=imagen,width=ancho, height=alto,fit=ft.ImageFit.FILL,expand=True),border = ft.border.all(1,ft.Colors.BLACK))
        self.stock = ft.Text(stock,color=ft.Colors.BLACK)

        self.btonComprar = CustomButton("Comprar") 
        self.btonComprar.height = alto * 30 // 100
        self.btonComprar.text_style = ft.TextStyle(size=alto * 14 // 100)

        self.bgcolor=ft.colors.WHITE
        self.border = ft.border.all(1,ft.Colors.BLACK)
        self.content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.imagen], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(
                            controls = [self.nombre,self.marca],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        ft.Row(
                            controls = [self.precio,self.stock],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        ft.Row(
                            controls = [
                                ft.Column(controls=[self.btonComprar],alignment=ft.MainAxisAlignment.START),                                
                                ],alignment=ft.MainAxisAlignment.CENTER),
                    ]
                )