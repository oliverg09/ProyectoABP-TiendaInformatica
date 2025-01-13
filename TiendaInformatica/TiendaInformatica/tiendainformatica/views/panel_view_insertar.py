import flet as ft
import base64
from utils.componentes import diseñoBoton,txtDesplegable,txtInput
from services.crud_operations import insertarProducto
from services.query_operations import consultarCategoriasFiltros,consultarMarcasFiltros

class Panel_View_Insertar(ft.View):
    def __init__(self,ancho,alto):
        super().__init__("/insertar")
        # Configuracion inicial de todas las ventanas
        self.bgcolor = "#D0C2C2"
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER 
        self.scroll = ft.ScrollMode.ALWAYS
        
        self.lblTitulo = ft.Text(
            value="INSERTAR DATOS",
            size=ancho * 2.33 // 100, 
            weight=ft.FontWeight.BOLD,
            color = "black"
        )

        self.contenedorTitulo = ft.Container(
            content=self.lblTitulo,
            margin=ft.margin.only(top=20, bottom=20),
            bgcolor="#CA9797",  
            width=300,          
            height=60,         
            border_radius=15,
            alignment=ft.Alignment(0, 0)  
        )

        #Labels 
        self.lblNombreProducto = ft.Text(value="Nombre Producto:", size=18, weight=ft.FontWeight.BOLD, color="black",text_align=ft.TextAlign.START)
        self.lblCategoria = ft.Text(value="Categoría:", size=18, weight=ft.FontWeight.BOLD, color="black")
        self.lblMarca = ft.Text(value="Marca:", size=18, weight=ft.FontWeight.BOLD, color="black")
        self.lblPrecio = ft.Text(value="Precio:", size=18, weight=ft.FontWeight.BOLD, color="black")
        self.lblStock = ft.Text(value="Stock:", size=18, weight=ft.FontWeight.BOLD, color="black")
        
        #Inputs personalizados
        self.txtNombre = txtInput()
        self.txtNombre.width = ancho * 24.90 // 100
        self.txtPrecio = txtInput()
        self.txtPrecio.width = ancho * 24.90 // 100
        self.txtStock = txtInput()
        self.txtStock.width = ancho * 24.90 // 100
        
        #Barras de busqueda
        self.categorias = txtDesplegable(autofocus=True)
        self.categorias.width = ancho * 24.90 // 100
        self.marca = txtDesplegable(autofocus=True)
        self.marca.width = ancho * 24.90 // 100

        # Creamos el objeto FilePicker para seleccionar archivos con el explorador de archivos nativo
        self.botonArchivos = ft.ElevatedButton(text="Seleccionar imagen",icon=ft.Icons.UPLOAD_FILE,
                            on_click=self.abrirArchivos
        )

        self.selectorArchivos = ft.FilePicker(on_result=self.resultadoArchivos)

        #Atributo que sera la imagen codificada a base 64
        self.archivoCodificado = ""

        #Boton para insertar datos personalizado
        self.boton = diseñoBoton(text="Insertar datos",on_click=self.insertarDatos)
        self.botonVolver = diseñoBoton(text="Volver",on_click=self.panelViewVolver)

        #Botones para agregar nueva categoria y marca
        self.btnCategoria = ft.Button(
            height=50,
            bgcolor="#CA9797",
            on_click=self.dialogo,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                side=ft.BorderSide(color=ft.Colors.BLACK,width=1)
            ),
            content=ft.Row(controls=[
                    ft.Icon(name=ft.icons.ADD_CIRCLE_OUTLINED,color=ft.Colors.BLACK)
                ]
            )
        )
        self.btnMarca = ft.Button(
            height=50,
            bgcolor="#CA9797",
            on_click=self.dialogo,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                side=ft.BorderSide(color=ft.Colors.BLACK,width=1)
            ),                
            content=ft.Row(controls=[
                    ft.Icon(name=ft.icons.ADD_CIRCLE_OUTLINED,color=ft.Colors.BLACK)
                ]
            )
        )

        #Input para escribir marca o categoria
        self.txtCreacion = ft.TextField(width=150,height=40,text_size=16,text_vertical_align=ft.VerticalAlignment.CENTER)

        #Texto para indicar al usuario que se ha guardado
        self.lblGuardado = ft.Text(value="",size=12,color=ft.Colors.GREEN)
        #Botones de dialogo
        self.btnDialogo1 = ft.Button(text="Guardar",height=30,on_click=self.guardarCategoriaMarca)
        self.btnDialogo2 = ft.Button(text="Cancelar",height=30,on_click=self.cerrarDialogo)

        #Contenedor de botones de dialogo
        self.contenedorDialog = ft.Container(content=ft.Row(controls=[self.btnDialogo1,self.btnDialogo2],alignment=ft.MainAxisAlignment.CENTER))

        #Dialogo para añadir categoria o marca
        self.alertDialogo = ft.AlertDialog(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.txtCreacion],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.lblGuardado],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.contenedorDialog],alignment=ft.MainAxisAlignment.CENTER)
                ],height=150,spacing=30
            )
        )

        #Texto del dialogo de notificacion
        self.lblMensaje = ft.Text(value="Producto insertado",height=30,size=26,color=ft.Colors.GREEN)

        #Dialogo para notificar al usuario al insertar un producto o mensaje de error
        self.alertDialogo2 = ft.AlertDialog(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblMensaje],alignment=ft.MainAxisAlignment.CENTER),
                ],height=150,spacing=30,alignment=ft.MainAxisAlignment.CENTER
            )
        )

        #Controles de la seccion 1
        self.contenedor1 = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblNombreProducto],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.txtNombre],alignment=ft.MainAxisAlignment.CENTER)
                    ]
            )
        )

        self.contenedor2 = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblCategoria],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.categorias,self.btnCategoria],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.START)
                    ]
            )
        )
        self.contenedor3 = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblMarca],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.marca,self.btnMarca],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.START)
                    ]
            )
        )

        #Controles de la seccion 2
        self.contenedor4 = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblPrecio],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.txtPrecio],alignment=ft.MainAxisAlignment.CENTER)
                ]
            )
        )

        self.contenedor5 = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblStock],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.txtStock],alignment=ft.MainAxisAlignment.CENTER)
                ] 
            )
        )

        self.contenedor7 = ft.Container(
            width= 256,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.botonArchivos,self.selectorArchivos],alignment=ft.MainAxisAlignment.CENTER)
                ]
            )
        )

        #Contenedor principal de todo el contenido
        self.contenedorPrincipal = ft.Container(
            width=ancho * 80 // 100,
            height=alto * 97 // 100,
            bgcolor="#EBD6D6", 
            border_radius=20, 
            content = ft.Column(
                controls=[
                    ft.Row(controls=[self.contenedorTitulo],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.contenedor1,self.contenedor4],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Row(controls=[self.contenedor2,self.contenedor5],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Row(controls=[self.contenedor3,self.contenedor7],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Row(controls=[self.boton, self.botonVolver],alignment=ft.MainAxisAlignment.CENTER)
                ],scroll=ft.ScrollMode.ALWAYS
            ),
        )

        self.controls.append(self.contenedorPrincipal)
    
    def dialogo(self,e):
        if e.control == self.btnCategoria:
            self.alertDialogo.title = ft.Text("Creación de categoría",text_align=ft.TextAlign.CENTER)
        else:
            self.alertDialogo.title = ft.Text("Creación de marca",text_align=ft.TextAlign.CENTER)
        self.page.open(self.alertDialogo)

    def cerrarDialogo(self,e):
        self.limpiarDialogo()
        self.alertDialogo.update()
        self.page.close(self.alertDialogo)

    def guardarCategoriaMarca(self,e):
        if self.txtCreacion.value != "":    
            if self.alertDialogo.title.value == "Creación de categoría":
                self.categorias.options.append(
                    ft.dropdown.Option(self.txtCreacion.value)
                )
                self.lblGuardado.value = "Categoría creada correctamente."
                self.txtCreacion.value = ""
                self.alertDialogo.update()
                self.update()
            else:
                self.marca.options.append(
                    ft.dropdown.Option(self.txtCreacion.value)
                )
                self.lblGuardado.value = "Marca creada correctamente."
                self.txtCreacion.value = ""
                self.alertDialogo.update()
                self.update()
    
    def limpiarDialogo(self):
        self.txtCreacion.value = ""
        self.lblGuardado.value = ""

    def abrirArchivos(self,e):
        self.selectorArchivos.pick_files()

    def resultadoArchivos(self, e: ft.FilePickerResultEvent):
        archivos = []
        rutaArchivos = []
        if e.files is not None:
            for archivo in e.files:
                if archivo.name.lower().endswith(('.png', '.jpg')): # Verificar si el archivo tiene la extensión permitida
                    archivos.append(archivo.name)
                    rutaArchivos.append(archivo.path)
                    self.archivoCodificado = self.codificar64(ruta=rutaArchivos[-1])
                else:
                    print(f"Archivo no permitido: {archivo.name}")
   
    def codificar64(self,ruta):
        with open(ruta,"rb") as imagen:
            #Extraemos los binarios de la imagen
            binarios = imagen.read()
            #Con este modulo convertimos a formate base64
            bytes64 = base64.b64encode(binarios).decode('utf-8')
            return bytes64
        
    def insertarDatos(self,e):
        try:
            # Validar que sean numeros
            precio = float(self.txtPrecio.value)
            stock = int(self.txtStock.value)

            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            if stock < 0:
                raise ValueError("El stock no puede ser negativo.")

            nombreProducto = self.txtNombre.value
            categoria = self.categorias.value
            marca = self.marca.value

            # Validar que no estén vacíos
            if not nombreProducto:
                raise ValueError("El nombre del producto no puede estar vacío.")
            if not categoria:
                raise ValueError("La categoría no puede estar vacía.")
            if not marca:
                raise ValueError("La marca no puede estar vacía.")
  
            imagen = self.archivoCodificado  

            producto = {"nombre":nombreProducto,
                        "categoria":categoria,
                        "marca":marca,
                        "precio":precio,
                        "stock":stock,
                        "imagen":imagen}
            
            insertarProducto(producto)
            
            self.page.open(self.alertDialogo2)

            self.limpiar()

        except Exception as error:
            self.lblMensaje.value = f"Error: {str(error)}"
            self.lblMensaje.color = ft.Colors.RED
            self.page.open(self.alertDialogo2)

    def panelViewVolver(self,e):
        self.page.views.pop()  
        self.page.views[-1].cargarProductos()
        self.page.views[-1].mostrarProductos()
        self.page.go(self.page.views[-1].route)

    def limpiar(self):
        self.txtNombre.value = ""
        self.txtPrecio.value = ""
        self.txtStock.value = ""
        self.marca.value = ""
        self.categorias.value = ""
        self.update()

    def cargarCategorias(self):
        self.categorias.options.clear()
        categorias = consultarCategoriasFiltros()
        for categoria in categorias:
            if categoria != None:
                self.categorias.options.append(ft.dropdown.Option(categoria))
                
    def cargarMarcas(self):
        self.marca.options.clear()
        marcas = consultarMarcasFiltros()
        for marca in marcas:
            if marca != None:
                self.marca.options.append(ft.dropdown.Option(marca))
    
    def panelViewVolver(self, e):
        self.page.views.pop()  
        self.page.go(self.page.views[-1].route)

    def ajustarPantalla(self,e=None):
        ancho = self.page.width
        alto = self.page.height
        self.contenedorPrincipal.width = ancho * 60 // 100
        self.contenedorTitulo.width = ancho * 30 // 100
        self.contenedorPrincipal.height = alto * 77 // 100
        self.lblTitulo.size = ancho * 2.33 // 100
        self.lblNombreProducto.size = ancho * 1.80 // 100
        self.lblCategoria.size = ancho * 1.80 // 100
        self.lblMarca.size = ancho * 1.80 // 100
        self.lblPrecio.size = ancho * 1.80 // 100
        self.lblStock.size = ancho * 1.80 // 100
        self.txtNombre.width = ancho * 24.90 // 100
        self.txtNombre.height = alto * 9 // 100
        self.txtPrecio.width = ancho * 24.90 // 100
        self.txtPrecio.height = alto * 9 // 100
        self.txtStock.width = ancho * 24.90 // 100
        self.txtStock.height = alto * 9 // 100
        self.categorias.width = ancho * 24.90 // 100
        self.marca.width = ancho * 24.90 // 100
        print({"Ancho":ancho},{"Alto":alto})
        if ancho <= 800:
            self.lblTitulo.size = ancho * 3.2 // 100
            self.contenedorTitulo.width = ancho * 30 // 100
            self.lblNombreProducto.size = ancho * 3 // 100
            self.lblCategoria.size = ancho * 3 // 100
            self.lblMarca.size = ancho * 3 // 100
            self.lblPrecio.size = ancho * 3 // 100
            self.lblStock.size = ancho * 3 // 100
            self.txtNombre.width = ancho * 50 // 100
            self.txtNombre.height = alto * 9 // 100
            self.txtPrecio.width = ancho * 50 // 100
            self.txtPrecio.height = alto * 9 // 100
            self.txtStock.width = ancho * 50 // 100
            self.txtStock.height = alto * 9 // 100
            self.categorias.width = ancho * 40 // 100
            self.marca.width = ancho * 40 // 100
            self.contenedorPrincipal.content.controls[2].controls.remove(self.contenedor5)
            self.contenedorPrincipal.content.controls[1].controls.insert(-1,self.contenedor5)
            for fila in range(1,len(self.contenedorPrincipal.content.controls)-1):
                self.contenedorPrincipal.content.controls[fila].wrap = True
            self.txtPrecio.text_align = ft.TextAlign.CENTER
            self.txtStock.text_align = ft.TextAlign.CENTER
            self.txtNombre.text_align = ft.TextAlign.CENTER
        else:
            self.txtPrecio.text_align = ft.TextAlign.START
            self.txtStock.text_align = ft.TextAlign.START
            self.txtNombre.text_align = ft.TextAlign.START
            if not self.contenedor5 in self.contenedorPrincipal.content.controls[2].controls:
                self.contenedorPrincipal.content.controls[1].controls.remove(self.contenedor5)
                self.contenedorPrincipal.content.controls[2].controls.append(self.contenedor5)
                self.contenedorPrincipal.update()
            for fila in range(1,len(self.contenedorPrincipal.content.controls)-1):
                self.contenedorPrincipal.content.controls[fila].wrap = False
        self.update()