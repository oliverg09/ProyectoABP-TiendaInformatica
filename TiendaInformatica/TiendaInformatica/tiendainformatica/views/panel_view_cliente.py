
import flet as ft

from services.query_operations import consultarProductos,consultarCategoriasFiltros,consultarMarcasFiltros,consultarProductosFiltros
from utils.componentes import txtDesplegable ,txtInput,Producto_Cliente,diseñoBoton

from views.panel_view_pago import Panel_Window_Pago

class Panel_Window_Cliente(ft.View):
    def __init__(self,ancho,alto) -> None:
        super().__init__(route="/cliente")  
        self.bgcolor = "#D0C2C2"
        self.scroll = ft.ScrollMode.ALWAYS
        # Posicionamos el elemento tanto horizontal como verticalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER 

        # Inicio de sesión --> Contenedor
        self.lblDatos = ft.Text(value="PRODUCTOS",size=24, weight=ft.FontWeight.BOLD)
        self.lblDatos.color = "black"

        # Boton Cerrar Sesion
        self.btnCerrarSesion = diseñoBoton(icon="logout",text="Cerrar Sesión",width=200)
        self.btnCerrarSesion.bgcolor = "#FF0000"
        self.btnCerrarSesion.on_click = lambda e: self.panelViewVolver(e)

        # Boton Consultar 
        self.btnConsultar = diseñoBoton(icon="search", text="Consultar", width=120)
        self.btnConsultar.on_click = self.consulta

        self.contenedorBtnConsutar = ft.Container(
            margin=ft.margin.only(top=30),
            content=self.btnConsultar,
            width=120,          
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

        #Atributo que sera la posicion en el listado de los productos
        self.posicionProductos = 0
        self.listadoProductosGrid = []

        #Posicion de las paginas
        self.lblPagina = ft.Text(size=16, weight=ft.FontWeight.BOLD)
        self.numeroPagina = 1

        self.contenedorTextoDatos = ft.Container(
            content=self.lblDatos,
            margin=ft.margin.only(top=20, bottom=20),
            bgcolor="#CA9797",  
            width=300,          
            height=60,         
            border_radius=15,
            alignment=ft.Alignment(0, 0)  
        )
        
        # Nombre                                                                                         # Creo un contenedor donde guardo los controles del nombre
        self.lblNombre = ft.Text(value="Nombre", size=18, weight=ft.FontWeight.BOLD)
        self.lblNombre.color = "black"
        self.txtNombre = txtInput()
        self.txtNombre.height = 40
        self.txtNombre.width = 250
        
        self.contenedorNombre = ft.Container(
            margin=ft.margin.only(left=20 , right=20),
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
                    ft.Column(controls=[self.btnCerrarSesion], alignment=ft.MainAxisAlignment.END),
                        ], alignment=ft.MainAxisAlignment.END
                    )
                )
        
        # Marca
        self.lblMarca = ft.Text(value="Marca",size=18, weight=ft.FontWeight.BOLD)
        self.lblMarca.color = "black"
        self.txtMarca = txtDesplegable()
        self.txtMarca.height = 40
        self.txtMarca.width = 250

        
        self.contenedorMarca = ft.Container(
            margin=ft.margin.only( left=20 , right=20),
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
        # Precio desde
        self.txtPrecio_inicio = ft.TextField(width=100,height=40, color="white")
        self.txtPrecio_inicio.bgcolor="#CA9797"
        self.txtPrecio_inicio.border_radius = 12
        self.txtPrecio_inicio.label = "Min"
        # Precio hasta
        self.txtPrecio_fin = ft.TextField(width=100,height=40, color="white")
        self.txtPrecio_fin.bgcolor="#CA9797"
        self.txtPrecio_fin.border_radius = 12
        self.txtPrecio_fin.label = "Max"
        
        self.contenedorPrecio = ft.Container(
            margin=ft.margin.only(right=40),
            width=200,
            height=75,
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.lblPrecio], alignment=ft.MainAxisAlignment.START),
                        ft.Row(
                            controls = [
                                ft.Column(controls=[self.txtPrecio_inicio],alignment=ft.MainAxisAlignment.START),
                                ft.Column(controls=[self.txtPrecio_fin],alignment=ft.MainAxisAlignment.END),
                                ]),
   
                    ]
                )
            )

        # Stock                                                                       #Creo los controles de Stock que los añado en dos contenedore 
        self.lblStock = ft.Text(value="Stock",size=18, weight=ft.FontWeight.BOLD)
        self.lblStock.color = "black"
        # Stock desde
        self.txtStock_inicio = ft.TextField(width=100,height=40, color="white")
        self.txtStock_inicio.bgcolor="#CA9797"
        self.txtStock_inicio.border_radius = 12
        self.txtStock_inicio.label = "Min"
        # Stock hasta
        self.txtStock_fin = ft.TextField(width=100,height=40, color="white")
        self.txtStock_fin.bgcolor="#CA9797"
        self.txtStock_fin.border_radius = 12
        self.txtStock_fin.label = "Max"
        
        self.contenedorStock = ft.Container(
            margin=ft.margin.only(left=40,right=20),
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

        # Contenedor porductos
        self.grid_productos = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=200,
            child_aspect_ratio=1.0,
            spacing=15,
            run_spacing=5,
            width=800
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
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.cursor2,self.lblPagina,self.cursor1],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER)
                ]
            )
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
        ),)



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

    def mostrarProductos(self):
        try:
            self.grid_productos.controls.clear()
            contador = 0
            for fila in range(self.posicionProductos,len(self.listadoProductosGrid)):
                contador += 1
                for producto in self.listadoProductosGrid[fila]:

                    try:
                        nuevoProducto = Producto_Cliente(nombre=producto['nombre'], precio=producto['precio'],
                                                                    marca=producto['marca'], imagen=producto['imagen'], stock=producto['stock'],
                                                                    ancho=self.grid_productos.max_extent*90//100,alto=self.grid_productos.max_extent*40//100)
                        nuevoProducto.btonComprar.on_click = self.clikBotonComprar
                        self.grid_productos.controls.append(nuevoProducto)  
                    except Exception as e:
                        print(f"Error en crear producto: {e}")

                if contador == 2:
                    contador = 0
                    break

            self.lblPagina.value = self.numeroPagina
            self.update()

        except Exception as e:
            print(f"Error general en mostrarProductos: {e}")

    def adelante(self,e):
        if self.posicionProductos + 2 >= len(self.listadoProductosGrid):
            self.posicionProductos = len(self.listadoProductosGrid) - 1
            print("Dentro de condicion de cursor adelante")
        else:
            self.posicionProductos += 2
            self.numeroPagina += 1
        self.mostrarProductos()

    def atras(self,e):
        if self.posicionProductos - 2 < 0:
            self.posicionProductos = 0
            print("Dentro de condicion de cursor atras")
        else:
            self.posicionProductos -= 2
            self.numeroPagina -= 1
        self.mostrarProductos()

    def panelViewVolver(self,e):
        self.page.views.pop()  
        self.page.go(self.page.views[-1].route)
    
    def clikBotonComprar(self,e):  # Click del Boton comprar del Grid
        print("Se clico el boton")
        nombreProducto = e.control.parent.parent.parent.parent.nombre.value
        ventanaComprar = Panel_Window_Pago(self.page.width,self.page.height)  
        ventanaComprar.contenedorNombreProducto.content.value = nombreProducto
        ventanaComprar.contenedorNombreCliente.content.value = self.nombreUsuario
        self.page.views.append(ventanaComprar)
        self.page.go(self.page.views[-1].route)
        ventanaComprar.cargarProductoCliente()
        ventanaComprar.stockAsincrono()
        ventanaComprar.page.on_resized = ventanaComprar.ajustarPantalla
        ventanaComprar.ajustarPantalla()

    def ajustarPantalla(self,e=None):
        ancho = self.page.width
        self.contenedorPrincipal.width = ancho * 85 // 100
        self.contenedorProductos.width = ancho * 85 // 100
        self.grid_productos.width = ancho * 88 // 100
        self.contenedorCursores.width = ancho * 88 // 100
        self.contenedorParteSuperior.width = ancho * 85 // 100
        self.contedorFiltros.width = ancho * 85 // 100
        if ancho < 500:
            self.grid_productos.max_extent = self.grid_productos.width * 80 // 100
            for fila in self.contedorFiltros.content.controls:
                fila.wrap = True
        else:
            for fila in self.contedorFiltros.content.controls:
                fila.wrap = False
        self.update()

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
        productos = []
        for producto in self.grid_productos.controls:
            producto_insertar = Producto_Cliente(producto.nombre.value, producto.precio.value, 
                            producto.marca.value, producto.imagen.content.src_base64,
                            producto.stock.value,100,alto)
            producto_insertar.btonComprar.on_click = self.clikBotonComprar
            productos.append(producto_insertar)
        self.grid_productos.controls = productos
        self.update()
        
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

    def inicial(self):
        self.txtNombre.value = ""
        self.txtPrecio_inicio.value = ""
        self.txtPrecio_fin.value = ""
        self.txtStock_inicio.value = ""
        self.txtStock_fin.value = ""
        self.txtCategoria.value = ""
        self.txtMarca.value = ""
        self.update()
