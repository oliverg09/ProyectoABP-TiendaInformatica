
import flet as ft
from utils.componentes import diseñoBoton,txtDesplegable,txtInput
from services.crud_operations import modificarProducto
from services.query_operations import consultarProducto,consultarCategoriasFiltros,consultarMarcasFiltros
import base64

class Panel_View_Modificar(ft.View):
    def __init__(self,ancho,alto):
        super().__init__("/panel3")
        self.bgcolor = "#D0C2C2"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER 

        # Titulo
        self.lblTitulo = ft.Text(value="MODIFICAR DATOS", size=ancho * 2.33 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.contenedorTitulo = ft.Container(
            content=self.lblTitulo,
            margin=ft.margin.only(top=20, bottom=20),
            bgcolor="#CA9797",
            width=ancho * 29 // 100,
            height=ancho * 5.83 // 100,
            border_radius=15,
            alignment=ft.Alignment(0, 0)
        )

        # Nombre y cargamos el nombre del producto a modificar
        self.lblNombreProducto = ft.Text(value="Nombre Producto:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.contenedorNombreProducto = ft.Container(
            content=ft.Text(value="", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black"),
            bgcolor="#CA9797",
            width=ancho * 29 // 100,
            height=alto * 5.87 // 100,
            border_radius=12,
            alignment=ft.Alignment(0, 0))

        # Precio Producto
        self.lblPrecio = ft.Text(value="Precio Producto:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.txtPrecio = txtInput()
        self.txtPrecio.width = ancho * 29 // 100
        self.txtPrecio.height = alto * 8.8 // 100 

        # Stock Producto
        self.lblStockProducto = ft.Text(value="Stock Producto:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.txtStockProducto = txtInput()
        self.txtStockProducto.width = ancho * 29 // 100
        self.txtStockProducto.height = alto * 8.8 // 100 

        # Categoria Producto
        self.lblCategoriaProducto = ft.Text(value="Categoria:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.txtCategoriaProducto = txtDesplegable()
        self.txtCategoriaProducto.width = ancho * 22.85 // 100
        
        # Marca Producto
        self.lblMarcaProducto = ft.Text(value="Marca:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.txtMarcaProducto = txtDesplegable()
        self.txtMarcaProducto.width = ancho * 22.85 // 100
        
        #Botones para agregar nueva categoria y marca
        self.btnCategoria = ft.Button(
            height=50,
            bgcolor="#CA9797",
            # on_click=self.dialogo,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                side=ft.BorderSide(color=ft.Colors.BLACK,width=1)
            ),
            content=ft.Row(controls=[
                    ft.Icon(name=ft.icons.ADD_CIRCLE_OUTLINED,color=ft.Colors.BLACK)
                ]
            ),on_click=self.dialogo
        )

        self.btnMarca = ft.Button(
            height=50,
            bgcolor="#CA9797",
            # on_click=self.dialogo,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                side=ft.BorderSide(color=ft.Colors.BLACK,width=1)
            ),                
            content=ft.Row(controls=[
                    ft.Icon(name=ft.icons.ADD_CIRCLE_OUTLINED,color=ft.Colors.BLACK)
                ]
            ),on_click=self.dialogo
        )

        # Boton Modificar y Volver
        self.btnModificar = diseñoBoton(text="Modificar",on_click=self.modificar)
        self.botonVolver = diseñoBoton(text="Volver",on_click=self.panelViewVolver)

        # Modificación de imagenes
        self.botonArchivos = ft.ElevatedButton(text="Seleccionar imagen",icon=ft.Icons.UPLOAD_FILE,
                            on_click=self.abrirArchivos
        )
        # Selector de archivos
        self.selectorArchivos = ft.FilePicker(on_result=self.resultadoArchivos)

        #Atributo que sera la imagen codificada a base 64
        self.archivoCodificado = ""

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

        #Dialogo para notificar al usuario de una modificacion
        self.lblDialogo = ft.Text(value="Producto modificado",width=250,height=80,size=24,color=ft.Colors.GREEN,text_align=ft.TextAlign.CENTER)
        self.alertDialogo2 = ft.AlertDialog(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblDialogo],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER)
                ],height=150,spacing=30,alignment=ft.MainAxisAlignment.END)
        )

        # Contenedor principal
        self.contenedorPrincipal = ft.Container(
            width=ancho * 68 // 100,
            height=alto * 70 // 100,
            bgcolor="#EBD6D6",
            border_radius=20,
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row([self.contenedorTitulo], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([self.lblNombreProducto, self.contenedorNombreProducto], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(
                        controls=[
                            ft.Column(controls=[self.lblPrecio, self.txtPrecio], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[self.lblStockProducto, self.txtStockProducto], alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,wrap=True
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(controls=[
                                ft.Row(controls=[self.lblCategoriaProducto],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row(controls=[self.txtCategoriaProducto, self.btnCategoria],alignment=ft.MainAxisAlignment.CENTER ,vertical_alignment=ft.CrossAxisAlignment.START)
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[
                                ft.Row(controls=[self.lblMarcaProducto],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row(controls=[self.txtMarcaProducto, self.btnMarca], alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.START)
                            ], alignment=ft.MainAxisAlignment.CENTER),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row([self.botonArchivos,self.selectorArchivos], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(
                        controls=[
                            ft.Column(controls=[self.btnModificar], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[self.botonVolver], alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),  
                ]))
        
        self.controls.append(self.contenedorPrincipal)

    def panelViewVolver(self,e):
        self.page.views[-2].cargarProductos()
        self.page.views[-2].mostrarProductos()
        self.page.views.pop()  
        self.page.go(self.page.views[-1].route)


    def modificar(self,e):
        nombreProducto = self.contenedorNombreProducto.content.value
        precio = float(self.txtPrecio.value)
        stock = int(self.txtStockProducto.value)
        categoria = self.txtCategoriaProducto.value
        marca = self.txtMarcaProducto.value
        imagen = self.archivoCodificado
        datosModificar ={"nombre":nombreProducto,"precio":precio,"stock":stock,"categoria":categoria,
                "marca":marca,"imagen":imagen}
        if precio != "" and stock != "":
            try:
                if int(stock) and float(precio):
                    modificarProducto(product_filter={"nombre":nombreProducto},product_data={'$set':datosModificar})
                    self.alertDialogo2.content.controls[-1].alignment = ft.MainAxisAlignment.END
                    self.mostrarMensaje("Producto modificado",ft.Colors.GREEN)
            except ValueError:
                self.alertDialogo2.content.controls[-1].alignment = ft.MainAxisAlignment.CENTER
                self.mostrarMensaje("El precio y stock deben ser",ft.Colors.RED)    
        else:
            self.alertDialogo2.content.controls[-1].alignment = ft.MainAxisAlignment.CENTER
            self.mostrarMensaje("Los campos no pueden estar vacios",ft.Colors.RED)
        
        
    def abrirArchivos(self,e):
        self.selectorArchivos.pick_files()

    def resultadoArchivos(self,e:ft.FilePickerResultEvent):
            archivos = []
            rutaArchivos = []
            if e.files != None:
                for archivo in e.files:
                    archivos.append(archivo.name)
                    rutaArchivos.append(archivo.path)
                self.archivoCodificado = self.codificar64(ruta=rutaArchivos[-1])   

    def codificar64(self,ruta):
        with open(ruta,"rb") as imagen:
            #Extraemos los binarios de la imagen
            binarios = imagen.read()
            #Con este modulo convertimos a formate base64
            bytes64 = base64.b64encode(binarios).decode('utf-8')
            return bytes64
    
    def dialogo(self,e):
        if e.control == self.btnCategoria:
            self.alertDialogo.title = ft.Text("Creación de categoría",text_align=ft.TextAlign.CENTER)
        else:
            self.alertDialogo.title = ft.Text("Creación de marca",text_align=ft.TextAlign.CENTER)
        self.page.open(self.alertDialogo)

    def cargarProducto(self):
        try:
            producto = consultarProducto({"nombre":self.contenedorNombreProducto.content.value})
            self.cargarCategorias()
            self.cargarMarcas()
            self.txtPrecio.value = producto['precio']
            self.txtStockProducto.value = producto['stock']
            self.txtCategoriaProducto.value = producto['categoria']
            self.txtMarcaProducto.value = producto['marca']
            self.archivoCodificado = producto['imagen']
            self.update()
        except Exception as e:
            print(f"Error al cargar producto: {e}")

    def cargarCategorias(self):
        categorias = consultarCategoriasFiltros()
        for categoria in categorias:
            if categoria != None:
                self.txtCategoriaProducto.options.append(ft.dropdown.Option(categoria))
    
    def cargarMarcas(self):
        marcas = consultarMarcasFiltros()
        for marca in marcas:
            if marca != None:
                self.txtMarcaProducto.options.append(ft.dropdown.Option(marca))

    def guardarCategoriaMarca(self,e):
        if self.txtCreacion.value != "":    
            if self.alertDialogo.title.value == "Creación de categoría":
                self.txtCategoriaProducto.options.append(
                    ft.dropdown.Option(self.txtCreacion.value)
                )
                self.lblGuardado.value = "Categoría creada correctamente."
                self.txtCreacion.value = ""
                self.alertDialogo.update()
                self.update()
            else:
                self.txtMarcaProducto.options.append(
                    ft.dropdown.Option(self.txtCreacion.value)
                )
                self.lblGuardado.value = "Marca creada correctamente."
                self.txtCreacion.value = ""
                self.alertDialogo.update()
                self.update()

    def cerrarDialogo(self,e):
        self.limpiarDialogo()
        self.alertDialogo.update()
        self.page.close(self.alertDialogo)

    def limpiarDialogo(self):
        self.txtCreacion.value = ""
        self.lblGuardado.value = ""
    
    def mostrarMensaje(self,mensaje:str,color:ft.Colors=ft.Colors.BLACK,funcion="") -> None:
        self.lblDialogo.value = mensaje
        self.lblDialogo.color = color
        self.alertDialogo2.on_dismiss = funcion
        self.page.open(self.alertDialogo2)  
        self.alertDialogo2.update()

    def ajustarPantalla(self,e=None):
        ancho = self.page.width
        alto = self.page.height
        self.contenedorPrincipal.width=ancho * 68 // 100
        self.contenedorPrincipal.height=alto * 70 // 100
        self.lblTitulo.size = ancho * 2.33 // 100
        self.contenedorTitulo.width = ancho * 29 // 100
        self.contenedorTitulo.height = alto * 9 // 100
        self.lblNombreProducto.size = ancho * 1.75 // 100
        self.contenedorNombreProducto.content.size = ancho * 1.75 // 100
        self.contenedorNombreProducto.width=ancho * 29 // 100
        self.contenedorNombreProducto.height=alto * 5.87 // 100
        self.lblPrecio.size = ancho * 1.75 // 100
        self.txtPrecio.width = ancho * 29 // 100
        self.txtPrecio.height = alto * 8.8 // 100 
        self.lblStockProducto.size = ancho * 1.75 // 100
        self.txtStockProducto.width = ancho * 29 // 100
        self.txtStockProducto.height = alto * 9 // 100 
        self.lblCategoriaProducto.size = ancho * 1.75 // 100
        self.txtCategoriaProducto.width = ancho * 22.85 // 100
        self.lblMarcaProducto.size = ancho * 1.75 // 100
        self.txtMarcaProducto.width = ancho * 22.85 // 100
        print({"Ancho":ancho,"Alto":alto},"DENTRO")
        if ancho <= 600:
            self.lblNombreProducto.size = ancho * 3 // 100
            self.lblPrecio.size = ancho * 3 // 100
            self.lblStockProducto.size = ancho * 3 // 100
            self.lblCategoriaProducto.size = ancho * 3 // 100
            self.lblMarcaProducto.size = ancho * 3 // 100
            self.txtCategoriaProducto.width = ancho * 40 // 100
            self.txtMarcaProducto.width = ancho * 40 // 100
            for fila in range(1,len(self.contenedorPrincipal.content.controls)-2):
                self.contenedorPrincipal.content.controls[fila].wrap = True
        else:
            self.lblNombreProducto.size = ancho * 1.75 // 100
            self.lblPrecio.size = ancho * 1.75 // 100
            self.lblStockProducto.size = ancho * 1.75 // 100
            self.lblCategoriaProducto.size = ancho * 1.75 // 100
            self.lblMarcaProducto.size = ancho * 1.75 // 100
            self.txtCategoriaProducto.width = ancho * 22.85 // 100
            self.txtMarcaProducto.width = ancho * 22.85 // 100
            for fila in range(1,len(self.contenedorPrincipal.content.controls)-2):
                self.contenedorPrincipal.content.controls[fila].wrap = False
        self.update()
