
import flet as ft

from services.query_operations import consultarProductos,consultarMarcasFiltros,consultarCategoriasFiltros,consultarProductosFiltros
from utils.componentes import txtDesplegable, txtInput, Producto_Administrador, diseñoBoton

from views.panel_view_insertar import Panel_View_Insertar
from views.panel_view_consultasgenerales import Panel_Window_ConsultasGenerales 
from views.panel_view_modificar import Panel_View_Modificar

class Panel_Window_Empleado(ft.View):
    def __init__(self,ancho,alto) -> None:
        super().__init__(route="/empleado")  
        self.bgcolor = "#D0C2C2"
        self.scroll = ft.ScrollMode.ALWAYS
        # Posicionamos el elemento tanto horizontal como verticalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER 

        # Inicio de sesión --> Contenedor
        self.lblDatos = ft.Text(value="DATOS",size=24, weight=ft.FontWeight.BOLD)
        self.lblDatos.color = "black"

        #Atributo que sera la posicion en el listado de los productos
        self.posicionProductos = 0
        self.listadoProductosGrid = []

        #Posicion de las paginas
        self.lblPagina = ft.Text(size=16, weight=ft.FontWeight.BOLD)
        self.numeroPagina = 1

        self.contenedorTextoDatos = ft.Container(
            content=self.lblDatos,
            margin=ft.margin.only(top=20, bottom=20,left=20 , right=20),
            bgcolor="#CA9797",  
            width=300,          
            height=60,         
            border_radius=15,
            alignment=ft.Alignment(0, 0)  
        )
        
        #Input para escribir marca o categoria
        self.txtCreacion = ft.TextField(width=150,height=40,text_size=16,text_vertical_align=ft.VerticalAlignment.CENTER)

        #Texto para indicar al usuario que se ha guardado
        self.lblGuardado = ft.Text(value="",size=12,color=ft.Colors.GREEN)
        #Botones de dialogo
        self.btnDialogo1 = ft.Button(text="Guardar",height=30)
        self.btnDialogo2 = ft.Button(text="Cancelar",height=30)

        #Contenedor de botones de dialogo
        self.contenedorDialog = ft.Container(content=ft.Row(controls=[self.btnDialogo1,self.btnDialogo2],alignment=ft.MainAxisAlignment.CENTER))


        self.alertDialogo = ft.AlertDialog(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.txtCreacion],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.lblGuardado],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.contenedorDialog],alignment=ft.MainAxisAlignment.CENTER)
                ],height=150,spacing=30
            )
        )
        
        # Estado_pagina --> Contenedor
        self.btnInsertar = diseñoBoton(text="Insertar Datos")
        self.btnInsertar.bgcolor = "#94AA94"
        self.btnInsertar.on_click = lambda e: self.panelViewInsertar(e)

        # Boton Cerrar Sesion
        self.btnCerrarSesion = diseñoBoton(icon="logout",text="Cerrar Sesión",width=200)
        self.btnCerrarSesion.bgcolor = "#FF0000"
        self.btnCerrarSesion.on_click = lambda e: self.panelViewVolver(e)

        # Boton Consultas Generales
        # Consultas las cuales sirvan para controlar datos sobre la venta de productos
        self.btnConsultas = diseñoBoton(icon="search", text="Consultas Generales")
        self.btnConsultas.bgcolor = "#94AA94"
        self.btnConsultas.on_click = lambda e: self.panelViewConsultasGenerales(e)

        # Nombre                                                                                         # Creo un contenedor donde guardo los controles del nombre
        self.lblNombre = ft.Text(value="Nombre", size=18, weight=ft.FontWeight.BOLD)
        self.lblNombre.color = "black"
        self.txtNombre = txtInput()
        self.txtNombre.height = 40
        self.txtNombre.width = 250
        
        self.contenedorNombre = ft.Container(
            margin=ft.margin.only(left=10 , right=10),
            width=250,
            height=75,
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.lblNombre], alignment=ft.MainAxisAlignment.START),
                        ft.Row(controls=[self.txtNombre], alignment=ft.MainAxisAlignment.START),
   
                    ]
                )
            )

        # Categoria
        self.lblCategoria = ft.Text(value="Categoria",size=18, weight=ft.FontWeight.BOLD)
        self.lblCategoria.color = "black"

        self.txtCategoria = txtDesplegable()
        self.txtCategoria.height = 40
        self.txtCategoria.width = 250
        
        self.contenedorCategoria = ft.Container(
            margin=ft.margin.only(left=20 , right=20),
            width=250,
            height=75,
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.lblCategoria], alignment=ft.MainAxisAlignment.START),
                        ft.Row(controls=[self.txtCategoria], alignment=ft.MainAxisAlignment.START),
   
                    ]
                )
            )
        

        self.contenedorParteSuperior = ft.Container(
            width=ancho * 85 // 100,           
            content=ft.Row(
                controls=[
                    ft.Column(controls=[self.btnInsertar], alignment=ft.MainAxisAlignment.START),
                    ft.Column(controls=[self.btnConsultas], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column(controls=[self.btnCerrarSesion], alignment=ft.MainAxisAlignment.END),
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,wrap=True
                    )
                )
        
        # Marca
        self.lblMarca = ft.Text(value="Marca",size=18, weight=ft.FontWeight.BOLD)
        self.lblMarca.color = "black"
        self.txtMarca = txtDesplegable()
        self.txtMarca.height = 40
        self.txtMarca.width = 250

        
        self.contenedorMarca = ft.Container(
            margin=ft.margin.only( left=25 , right=20),
            width=250,
            height=75,
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.lblMarca], alignment=ft.MainAxisAlignment.START),
                        ft.Row(controls=[self.txtMarca], alignment=ft.MainAxisAlignment.START),
   
                    ]
                )
            )
        
        # Precio                                                                       #Creo los controles de PRECIO que los añado en dos contenedore 
        self.lblPrecio = ft.Text(value="Precio",size=18, weight=ft.FontWeight.BOLD)
        self.lblPrecio.color = "black"

        self.txtPrecio_inicio = txtInput()
        self.txtPrecio_inicio.width= 100
        self.txtPrecio_inicio.height=40
        self.txtPrecio_inicio.label = "Min"

        self.txtPrecio_fin = txtInput()
        self.txtPrecio_fin.width = 100
        self.txtPrecio_fin.height=40
        self.txtPrecio_fin.label = "Max"
        
        self.contenedorPrecio = ft.Container(
            margin=ft.margin.only(left=20),
            width=250,
            height=75,
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.lblPrecio], alignment=ft.MainAxisAlignment.START),
                        ft.Row(
                            controls = [
                                ft.Column(controls=[self.txtPrecio_inicio],alignment=ft.MainAxisAlignment.START),
                                ft.Column(controls=[self.txtPrecio_fin],alignment=ft.MainAxisAlignment.START),
                                ]),
   
                    ]
                )
            )

        # Stock                                                                       #Creo los controles de Stock que los añado en dos contenedore 
        self.lblStock = ft.Text(value="Stock",size=18, weight=ft.FontWeight.BOLD)
        self.lblStock.color = "black"

        self.txtStock_inicio = txtInput()
        self.txtStock_inicio.width=100
        self.txtStock_inicio.height=40
        self.txtStock_inicio.label = "Min"

        self.txtStock_fin =  txtInput()
        self.txtStock_fin.width=100
        self.txtStock_fin.height = 40
        self.txtStock_fin.label = "Max"
        
        self.contenedorStock = ft.Container(
            margin=ft.margin.only(left=40),
            width=250,
            height=75,
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.lblStock]),
                        ft.Row(
                            controls = [
                                ft.Column(controls=[self.txtStock_inicio],alignment=ft.MainAxisAlignment.START),
                                ft.Column(controls=[self.txtStock_fin],alignment=ft.MainAxisAlignment.END),
                                ]),
                    ]
                )
            )
        
        # Boton Consultar 
        self.btnConsultar = diseñoBoton(icon="search", text="Consultar", width=120)
        self.btnConsultar.on_click = self.consulta

        self.contenedorBtnConsutar = ft.Container(
            margin=ft.margin.only(top=30),
            content=self.btnConsultar,
            width=150,          
            height=45,         
            border_radius=15,
            alignment=ft.Alignment(0, 0)  
        )

        self.btnLimpiar = diseñoBoton(icon="clear", text="Limpiar", width=100)
        self.btnLimpiar.on_click = self.limpiar

        self.contenedorBtnLimpiar = ft.Container(
            margin=ft.margin.only(left=20,top=30),
            content=self.btnLimpiar,
            width=100,          
            height=45,         
            border_radius=15,
            alignment=ft.Alignment(0, 0)  
        )



        self.cursor1 = ft.Button(
            content=ft.Icon(ft.icons.ARROW_FORWARD,color=ft.Colors.BLACK,size=40),
            on_click=self.adelante
        )
        self.cursor2 = ft.Button(
            content=ft.Icon(ft.icons.ARROW_BACK,color=ft.Colors.BLACK,size=40),
            on_click=self.atras
        )

        self.contenedorCursores = ft.Container(
            width=ancho * 88 // 100,
            margin=ft.margin.only(top=20),
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.cursor2,self.lblPagina,self.cursor1],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER)
                ]
            )
        )
        
        # Contenedor productos
        self.grid_productos = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=200,
            child_aspect_ratio=1.0,
            spacing=15,
            run_spacing=5,
            width=800  
        )

        self.contenedorfila1 = ft.Container(
            margin=ft.margin.only(top=50),
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.grid_productos], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Row(controls=[self.contenedorCursores], alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER)
                    ]
                )       
            )
        self.contenedorProductos = ft.Container(
            width=ancho * 85 // 100,
            bgcolor="#B29B9B",
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.contenedorfila1], alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    ]
                )
            )
        

        self.contedorFiltros = ft.Container(
        width=ancho * 85 // 100,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(controls=[self.contenedorNombre], alignment=ft.MainAxisAlignment.START),
                        ft.Column(controls=[self.contenedorCategoria], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column(controls=[self.contenedorMarca], alignment=ft.MainAxisAlignment.END),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,wrap=True
                ),
                ft.Row(
                    controls=[
                        ft.Column(controls=[self.contenedorPrecio], alignment=ft.MainAxisAlignment.START),
                        ft.Column(controls=[self.contenedorStock], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column(controls=[self.contenedorBtnLimpiar], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Column(controls=[self.contenedorBtnConsutar], alignment=ft.MainAxisAlignment.END),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,wrap=True
                ),
            ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )


        # Creamos el contenedor principal
        self.contenedorPrincipal = ft.Container(
            width=ancho * 85 // 100,
            bgcolor="#EBD6D6", 
            border_radius=20, 
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.contenedorTextoDatos], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[
                                ft.Container(content=self.contenedorParteSuperior,alignment=ft.alignment.center,expand=True),
                                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Row(controls=[self.contedorFiltros], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.contenedorProductos], alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        
                    ]
                )
            )
        self.controls.append(self.contenedorPrincipal)

    def cargarProductos(self,productos=None):
        try:

            if productos == None:
                productos = list(consultarProductos())

            self.listadoProductosGrid = []
            filaProductos = []
            contador = 0
            posicion = 0

            #Cargamos los productos
            for producto in productos:
                contador += 1
                filaProductos.append(producto)
                posicion += 1
                restante = len(productos) - posicion
                if contador == 4:
                    self.listadoProductosGrid.append(filaProductos)
                    filaProductos = []
                    contador = 0    
                elif contador < 4 and contador > 0 and restante <= 2:
                    if restante == 0:
                        self.listadoProductosGrid.append(filaProductos)
            self.longitudListaProductos = len(self.listadoProductosGrid)
            
            try:
                self.cargarCategorias()
            except Exception as e:
                print(f"Error al cargar categorías: {e}")
        
            try:
                self.cargarMarcas()
            except Exception as e:
                print(f"Error al cargar marcas: {e}")

        except Exception as e:
            print(f"Error cargando productos: {e}")

    def cargarCategorias(self):
        self.txtCategoria.options.clear()
        categorias = consultarCategoriasFiltros()
        for categoria in categorias:
            if categoria != None:
                self.txtCategoria.options.append(ft.dropdown.Option(categoria))
                
    
    def cargarMarcas(self):
        self.txtMarca.options.clear()
        marcas = consultarMarcasFiltros()
        for marca in marcas:
            if marca != None:
                self.txtMarca.options.append(ft.dropdown.Option(marca))

    def mostrarProductos(self):
        self.grid_productos.controls.clear()
        contador = 0
        for fila in range(self.posicionProductos,len(self.listadoProductosGrid)):
            contador += 1
            for producto in self.listadoProductosGrid[fila]:
                nuevoProducto = Producto_Administrador(nombre=producto['nombre'], precio=producto['precio'],
                                                        marca=producto['marca'], imagen=producto['imagen'], stock=producto['stock'],
                                                        ancho=self.grid_productos.max_extent*90//100,alto=self.grid_productos.max_extent*40//100)
                self.grid_productos.controls.append(nuevoProducto)
            if contador == 2:
                contador = 0
                break
        self.lblPagina.value = self.numeroPagina
        self.update()

    def consulta(self, e):
        try:
            # Obtener los valores de los filtros
            categoria = self.txtCategoria.value
            nombreProducto = self.txtNombre.value
            marca = self.txtMarca.value
            precioMin = self.txtPrecio_inicio.value
            precioMax = self.txtPrecio_fin.value
            stockMin = self.txtStock_inicio.value
            stockMax = self.txtStock_fin.value
            
            if not categoria and not nombreProducto and not marca and not precioMin and not precioMax and not stockMin and not stockMax:
                productos = consultarProductos()  # Obtener todos los productos
            else:
                productos = consultarProductosFiltros(
                    nombre=nombreProducto,
                    categoria=categoria,
                    marca=marca,
                    precio_min=precioMin,
                    precio_max=precioMax,
                    stock_min=stockMin,
                    stock_max=stockMax
                )
            
            self.cargarProductos(productos=productos)
            self.mostrarProductos()

        except Exception as e:
            print(f"Error en la consulta: {e}")

    def limpiar(self,e):  # Limpiamos todos los campos
        if self.txtCategoria.value != None or self.txtNombre.value != "" or self.txtMarca.value != None or self.txtPrecio_inicio.value != "" or self.txtPrecio_fin.value != "" or self.txtStock_inicio.value != "" or self.txtStock_fin.value != "": 
            self.txtCategoria.value = None
            self.txtNombre.value = ""
            self.txtMarca.value = None
            self.txtPrecio_inicio.value = ""
            self.txtPrecio_fin.value = ""
            self.txtStock_inicio.value = ""
            self.txtStock_fin.value = ""
            self.update()

    def adelante(self,e):
        if self.posicionProductos + 2 >= len(self.listadoProductosGrid):
            self.posicionProductos = len(self.listadoProductosGrid) - 1
        else:
            self.posicionProductos += 2
            self.numeroPagina += 1
        self.mostrarProductos()

    def atras(self,e):
        if self.posicionProductos - 2 < 0:
            self.posicionProductos = 0
        else:
            self.posicionProductos -= 2
            self.numeroPagina -= 1
        self.mostrarProductos()

    def panelViewInsertar(self,e):  # Interaccion cambiar a ventana Insertar Producto
        panel2 = Panel_View_Insertar(self.page.width,self.page.height)
        panel2.cargarCategorias()
        panel2.cargarMarcas()
        self.page.views.append(panel2)
        self.page.go(self.page.views[-1].route)
        panel2.page.on_resized = panel2.ajustarPantalla
        panel2.ajustarPantalla()

    def panelViewConsultasGenerales(self,e):
        panel2 = Panel_Window_ConsultasGenerales()
        self.page.views.append(panel2)
        self.page.go(self.page.views[-1].route)

    def clickBotonEditar(self,e):  # Click del Boton editar del Grid
        nombreProducto = e.control.parent.parent.parent.parent.nombre.value
        ventanaModificar = Panel_View_Modificar(self.page.width,self.page.height)  
        ventanaModificar.contenedorNombreProducto.content.value = nombreProducto
        self.page.views.append(ventanaModificar)
        self.page.go(self.page.views[-1].route)
        ventanaModificar.cargarProducto()
        ventanaModificar.page.on_resized = ventanaModificar.ajustarPantalla
        ventanaModificar.ajustarPantalla()
    
    def clickConsultasComunes(self, e):    #  # Interaccion cambiar a ventana Consultas Totales
        panel2 = Panel_Window_ConsultasGenerales()
        self.page.views.append(panel2)
        self.page.go(self.page.views[-1].route) 

    def panelViewVolver(self,e):
        self.page.views.pop()  
        self.page.go(self.page.views[-1].route)

    def ajustarPantalla(self,e=None):
        ancho = self.page.width
        self.contenedorPrincipal.width = ancho * 85 // 100
        self.contenedorProductos.width = ancho * 85 // 100
        self.grid_productos.width = self.contenedorProductos.width * 88 // 100
        self.contenedorCursores.width = ancho * 88 // 100
        self.contenedorParteSuperior.width = ancho * 85 // 100
        self.contedorFiltros.width = ancho * 85 // 100
        print("El ancho es: ",ancho)
        if ancho < 500:
            self.grid_productos.max_extent = self.grid_productos.width // 2
            for fila in self.contedorFiltros.content.controls:
                fila.wrap = True
        elif ancho > 690 and ancho < 1000:
            self.grid_productos.max_extent = self.grid_productos.width // 3
            for fila in self.contedorFiltros.content.controls:
                fila.wrap = True
        elif ancho > 500 and ancho < 690:
            self.grid_productos.max_extent = self.grid_productos.width * 60 // 100
            for fila in self.contedorFiltros.content.controls:
                fila.wrap = True
        else:
            self.grid_productos.max_extent = self.grid_productos.width // 4
            for fila in self.contedorFiltros.content.controls:
                fila.wrap = False

        self.grid_productos.height = self.grid_productos.max_extent * 2
        self.contenedorProductos.height = self.grid_productos.max_extent * 2 + 130

        
        self.ajustarImagen(self.grid_productos.max_extent*40//100)
        self.update()

    def ajustarImagen(self,alto:int):
        print("Ajustando tamaño de imagen")
        productos = [Producto_Administrador(producto.nombre.value, producto.precio.value, producto.marca.value, producto.imagen.content.src_base64,
                                             producto.stock.value,100,alto) for producto in self.grid_productos.controls]
        self.grid_productos.controls = productos
        self.update()
