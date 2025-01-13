import flet as ft
import base64
from services.crud_operations import cargarImagen
from services.query_operations import consultarProducto

class Panel_Window(ft.View):
    def __init__(self) -> None:
        super().__init__("/panel")
        self.bgcolor = ft.Colors.BLUE_100 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.label1 = ft.Text(value="Gestion de tareas",size=34,color=ft.Colors.BLACK)
        self.boton = ft.OutlinedButton(text="Abrir busqueda",on_click=self.mostrar)
        self.boton2 = ft.FilledButton(text="Cerrar sesion",on_click=self.cerrarSesion)
        self.selectorArchivos = ft.FilePicker(on_result=self.resultadoArchivos)
        self.campoTexto = ft.TextField(width=150,height=40)
        self.archivosSeleccionados = ft.Text()             
        self.boton3 = ft.ElevatedButton(text="Pick files",icon=ft.Icons.UPLOAD_FILE,
                            on_click=self.abrirArchivos
                        )
        self.imagen = ft.Image(
            src="mi_gestor\colecciones\dragon.png",
            width=300,
            height=300
        )
        self.categorias = ft.SearchBar(
            view_elevation=2,
            divider_color=ft.Colors.BLUE,
            bar_hint_text="Categorias...",
            on_tap=self.mostrar,
            controls=[
                ft.ListTile(title=ft.Text(f"Color {i}"),on_click=self.cerrar,data=i) for i in range(10)
            ]
        )
        self.boton4 = ft.FilledButton(text="Mostrar producto",on_click=self.mostrarProducto)
        self.contenedor = ft.Container(
            width=700,
            height=450,
            bgcolor=ft.Colors.WHITE,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.boton,self.boton2,self.boton4,self.campoTexto]),
                    ft.Row(controls=[self.categorias],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.imagen],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.boton3],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.archivosSeleccionados],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.selectorArchivos],alignment=ft.MainAxisAlignment.CENTER)
                ]
            )
        )
        self.controls.append(self.contenedor)
    def mostrar(self,e):
        print("Abriendo barra de busqueda")
        self.categorias.open_view()

    def cerrar(self,e):
        texto = f"Color {e.control.data}"
        texto = self.categorias.controls[e.control.data].title.value
        print("Cerrando barra de categorias.")
        self.categorias.close_view(text=texto)

    def cerrarSesion(self,e):
        self.page.views.pop(-1)
        print(f"Ruta actual: {self.page.route}")
        self.page.go(self.page.views[-1].route)

    def resultadoArchivos(self,e: ft.FilePickerResultEvent):
            archivos = []
            rutaArchivos = []
            archivosSeleccionados = ""
            if e.files != None:
                for archivo in e.files:
                    archivos.append(archivo.name)
                    rutaArchivos.append(archivo.path)
                nombresArchivosSeleccionados = ", ".join(archivos) +" "+rutaArchivos[-1]
                archivoCodificado = self.codificar64(ruta=rutaArchivos[-1])
                producto = {"nombre":self.campoTexto.value,"imagen":archivoCodificado}
                cargarImagen(producto)
                print(archivoCodificado)
                self.archivosSeleccionados.value = nombresArchivosSeleccionados
            else:
                self.archivosSeleccionados.value = "Cancelado por el usuario."    
            self.update()
    
    def abrirArchivos(self,e):
        self.page.overlay.append(self.selectorArchivos)
        # self.selectorArchivos.pick_files(allow_multiple=True)
        self.selectorArchivos.pick_files()

    def codificar64(self,ruta):
        with open(ruta,"rb") as imagen:
            #Extraemos los binarios de la imagen
            binarios = imagen.read()
            #Con este modulo convertimos a formate base64
            bytes64 = base64.b64encode(binarios).decode('utf-8')
            return bytes64
        
    def mostrarProducto(self,e):
        consulta = {"nombre":self.campoTexto.value}
        producto = consultarProducto(consulta)
        self.imagen.src_base64=producto["imagen"]
        self.update()