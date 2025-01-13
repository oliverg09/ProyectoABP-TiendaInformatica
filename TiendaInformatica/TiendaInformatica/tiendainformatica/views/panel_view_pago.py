
import flet as ft
import threading,time
from utils.componentes import diseñoBoton, txtDesplegable, txtInput
from services.query_operations import consultarProducto,calcularId
from services.crud_operations import comprarProducto
class Panel_Window_Pago(ft.View):
    def __init__(self,ancho,alto) -> None:
        super().__init__(route="/panel2")
        self.bgcolor = "#D0C2C2"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Titulo
        self.lblpago = ft.Text(value="PAGO", size=ancho*2.33//100, weight=ft.FontWeight.BOLD, color="black")
        self.contenedorPago = ft.Container(
            content=self.lblpago,
            margin=ft.margin.only(top=20, bottom=20),
            bgcolor="#CA9797",
            width=ancho * 29 //100,
            height=alto * 5.83 // 100,
            border_radius=15,
            alignment=ft.Alignment(0, 0)
        )

        # Nombre
        self.lblNombreProducto = ft.Text(value="Nombre Producto:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.contenedorNombreProducto = ft.Container(
            content=ft.Text(value="", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black"),
            bgcolor="#CA9797",
            width=ancho * 29 //100,
            height=alto * 8.81 // 100,
            border_radius=12,
            alignment=ft.Alignment(0, 0))

        # Forma de Pago
        self.lblFormaPago = ft.Text(value="Forma de pago:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.txtFormaPago = txtDesplegable()
        self.txtFormaPago.width = ancho * 29 // 100
        self.txtFormaPago.height = alto * 8.81 // 100
        self.txtFormaPago.options=[
                ft.dropdown.Option("Bizum"),
                ft.dropdown.Option("Paypal"),
                ft.dropdown.Option("Transferencia")]
        # Precio Producto
        self.lblPrecio = ft.Text(value="Precio Producto:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.txtPrecio = ft.Text(value="", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.contenedorPrecio = ft.Container(
            content=self.txtPrecio,
            bgcolor="#CA9797",
            width=ancho * 14.60 // 100,
            height=alto * 5.87 // 100,
            border_radius=12,
            alignment=ft.Alignment(0, 0))
        
        # Monto total
        self.lblMonto = ft.Text(value="Monto total:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.txtMonto = ft.Text(value="", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black")
        self.contenedorMonto = ft.Container(
            content=self.txtMonto,
            bgcolor="#CA9797",
            width=ancho * 14.60 // 100,
            height=alto * 5.87 // 100,
            border_radius=12,
            alignment=ft.Alignment(0, 0))


        # Nombre Cliente
        self.lblNombreCliente = ft.Text(value="Nombre Cliente:", size=18, weight=ft.FontWeight.BOLD, color="black")
        self.contenedorNombreCliente = ft.Container(
            content=ft.Text(value="", size=18, weight=ft.FontWeight.BOLD, color="black"),
            bgcolor="#CA9797",
            width=300,
            height=40,
            border_radius=12,
            alignment=ft.Alignment(0, 0))

        # Numero de unidades del producto que desea el cliente 
        self.lblStockProducto = ft.Text(value="Nº de unidades:", size=ancho * 1.75 // 100, weight=ft.FontWeight.BOLD, color="black") # CONSULTA --> SI PIDE MAS DE LO PERMITIDO = MENSAJE DE ERROR
        self.txtStockProducto = txtInput()  
        self.txtStockProducto.text_align = ft.TextAlign.CENTER
        self.txtStockProducto.width = 80
        self.txtStockProducto.value = 0
        self.txtStockProducto.height = 40
        self.txtStockProducto.on_change = self.tecladoStock
        self.txtStockProducto.text_vertical_align = ft.VerticalAlignment.START
        self.txtStockProducto.input_filter=ft.NumbersOnlyInputFilter()
        self.txtStockProducto.on_blur=self.desenfoque

        #Botones para sumar y restar unidades
        self.btnRestar = ft.IconButton(ft.Icons.REMOVE, on_click=self.restarUnidad)
        self.btnSumar = ft.IconButton(ft.Icons.ADD, on_click=self.sumarUnidad)

        #Label y texto para mostrar disponibilidad de stock
        self.lblStockDisponible = ft.Text(value="Disponible(s):", size=18, weight=ft.FontWeight.BOLD, color="black")
        self.txtStockDisponible = ft.Text(value="", size=18, weight=ft.FontWeight.BOLD, color="black")
        self.txtStockActualizar = ft.Text(value="", size=12, weight=ft.FontWeight.BOLD, color="black",text_align=ft.TextAlign.CENTER)
        self.contenedorStockTxt = ft.Container(
            content=self.txtStockDisponible,
            bgcolor="#CA9797",
            width=100,
            height=40,
            border_radius=12,
            alignment=ft.Alignment(0, 0))
        
        self.contenedorStockDisponible = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblStockDisponible],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.contenedorStockTxt],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.END),
                    ft.Row(controls=[self.txtStockActualizar],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.END),
                ]
            )
        )
        
        #Contenedor donde va el input de botones y unidades
        self.contenedorStock = ft.Container(
                content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblStockProducto],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.btnRestar,
                    self.txtStockProducto,
                    self.btnSumar],alignment=ft.MainAxisAlignment.CENTER)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

        # Direccion Pedido
        self.lblDireccionPedido = ft.Text(value="Direccion Pedido:", size=18, weight=ft.FontWeight.BOLD, color="black")
        self.txtDireccionPedido = txtInput()

        # Boton Comprar
        self.btnPagar = diseñoBoton(text="Comprar",on_click=self.clickBtnComprar)
        self.btnVolver = diseñoBoton(text="Volver", on_click=self.panelViewVolver)

        #Texto del dialogo de notificacion
        self.lblMensaje = ft.Text(value="Compra exitosa",height=40,size=26,color=ft.Colors.GREEN)

        #Dialogo para notificar al usuario de la compra
        self.alertDialogo = ft.AlertDialog(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblMensaje],alignment=ft.MainAxisAlignment.CENTER),
                ],height=150,spacing=30,alignment=ft.MainAxisAlignment.CENTER
            ),on_dismiss=self.panelViewVolver
        )

        self.contenedorFormaPago = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.lblFormaPago],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.txtFormaPago],alignment=ft.MainAxisAlignment.CENTER),
                ]
            )
        )

        # Contenedor principal
        self.contenedorPrincipal = ft.Container(
            width=700,
            height=500,
            bgcolor="#EBD6D6",
            border_radius=20,
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    ft.Row([self.contenedorPago], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(
                        controls=[
                            ft.Column(controls=[
                                ft.Row(controls=[self.lblNombreProducto],alignment=ft.MainAxisAlignment.CENTER), 
                                ft.Row(controls=[self.contenedorNombreProducto],alignment=ft.MainAxisAlignment.CENTER)
                                ], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[self.lblPrecio, self.contenedorPrecio], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[self.lblMonto, self.contenedorMonto], alignment=ft.MainAxisAlignment.CENTER)
                            
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(controls=[self.lblNombreCliente, self.contenedorNombreCliente], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[self.contenedorStock], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[self.contenedorStockDisponible],alignment=ft.MainAxisAlignment.CENTER),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(controls=[self.contenedorFormaPago], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Column(controls=[self.lblDireccionPedido, self.txtDireccionPedido], alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    ft.Row(
                        controls=[
                            ft.Row([self.btnPagar], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([self.btnVolver], alignment=ft.MainAxisAlignment.CENTER),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER 
            )
        )

        self.controls.append(self.contenedorPrincipal)

    def restarUnidad(self,e):
        if not int(self.txtStockProducto.value) <= 0:
            self.txtStockProducto.value = str(int(self.txtStockProducto.value) - 1)
            self.txtMonto.value = str(int(self.txtStockProducto.value) * float(self.txtPrecio.value))
            self.update()

    def sumarUnidad(self,e):
        self.txtStockProducto.value = str(int(self.txtStockProducto.value) + 1)
        self.txtMonto.value = str(int(self.txtStockProducto.value) * float(self.txtPrecio.value))
        self.update()

    def panelViewVolver(self, e):
        # Detener el hilo antes de volver
        self.detenerHilo()
        
        self.page.views.pop()  
        self.page.go(self.page.views[-2].route)

    def cargarProductoCliente(self):
        try:
            
            producto = consultarProducto({"nombre":self.contenedorNombreProducto.content.value})
            self.contenedorPrecio.content.value = producto['precio']
            self.txtStockDisponible.value = producto['stock']
            self.update()

        except Exception as e:
            print("Error al cargar producto:", str(e))

    def clickBtnComprar(self, e):
        nombreProducto = self.contenedorNombreProducto.content.value
        precioProducto = self.contenedorPrecio.content.value
        stock = self.txtStockProducto.value
        stockDisponible = int(self.txtStockDisponible.value)
        formaPago = self.txtFormaPago.value
        direccionPedido = self.txtDireccionPedido.value
        nombreCliente = self.contenedorNombreCliente.content.value    
        idPedido = calcularId()
        
        if stock != "" and formaPago != "" and direccionPedido != "":
            if int(stock) <= stockDisponible:
                if comprarProducto({"id_pedido": idPedido, "nombre_producto": nombreProducto, 'precio': float(precioProducto), 'stock': int(stock), 'forma_pago': formaPago, "usuario_cliente": nombreCliente, "direccion_pedido": direccionPedido}):
                    print("Compra realizada")
                    self.mostrarMensaje("Compra realizada", ft.Colors.GREEN, self.panelViewVolver)
                    # Detener el hilo antes de volver
                    self.detenerHilo()
            else:
                print("Ha excedido la cantidad de Stock")
                self.mostrarMensaje("Ha excedido la cantidad de Stock", ft.Colors.RED)
                
        else:
            print("Debe llenar todos los campos")
            self.mostrarMensaje("Debe llenar todos los campos", ft.Colors.RED)
    
    def detenerHilo(self):
        self.evento.set()

    def tecladoStock(self,e):
        self.txtStockProducto.value = int(self.txtStockProducto.value)
        self.txtMonto.value = str(int(self.txtStockProducto.value) * float(self.txtPrecio.value))
        self.update()
        

    def desenfoque(self,e):
        if self.txtStockProducto.value == "":
            self.txtStockProducto.value = "0"
            self.txtMonto.value = str(int(self.txtStockProducto.value) * float(self.txtPrecio.value))
            self.update()
        
    def stockAsincrono(self):
        self.evento = threading.Event()
        hilo = threading.Thread(target=self.contadorAsincrono)
        hilo.start()

    def contadorAsincrono(self):
        contador = 10
        while not self.evento.is_set():
            if contador < 0:
                contador = 10
                producto = consultarProducto({'nombre':self.contenedorNombreProducto.content.value})
                if producto:
                    self.txtStockDisponible.value = str(producto['stock'])
                else:
                    self.txtStockDisponible.value = "0"
                self.update()
            self.txtStockActualizar.value = f"Actualizando en: {contador}"
            time.sleep(1)
            contador -= 1
            if not self.evento.is_set():
                self.update()

    def mostrarMensaje(self,mensaje:str,color:ft.Colors=ft.Colors.BLACK,funcion="") -> None:
        self.lblMensaje.value = mensaje
        self.lblMensaje.color = color
        self.alertDialogo.on_dismiss = funcion
        self.page.open(self.alertDialogo)  
        self.alertDialogo.update()

    def ajustarPantalla(self,e=None):
        ancho = self.page.width
        alto = self.page.height
        print({"Alto":alto,"Ancho":ancho})
        self.contenedorPrincipal.width = ancho * 68 // 100
        self.contenedorPrincipal.height = alto * 73 // 100
        self.lblpago.size = ancho * 2.33 // 100
        self.contenedorPago.width = ancho * 29 //100
        self.contenedorPago.height = alto * 5.83 // 100
        self.lblNombreProducto.size = ancho * 1.75 // 100
        self.contenedorNombreProducto.width = ancho * 29 //100
        self.contenedorNombreProducto.height = alto * 5.83 // 100
        self.contenedorNombreProducto.content.size = ancho * 1.75 // 100
        self.lblPrecio.size=ancho * 1.75 // 100
        self.txtPrecio.size=ancho * 1.75 // 100
        self.contenedorPrecio.width = ancho * 14.60 // 100
        self.contenedorPrecio.height = alto * 5.87 // 100
        self.lblMonto.size=ancho * 1.75 // 100
        self.txtMonto.size=ancho * 1.75 // 100
        self.contenedorMonto.width= ancho * 14.60 // 100
        self.contenedorMonto.height= alto * 5.87 // 100
        self.lblNombreCliente.size = ancho * 1.75 // 100
        self.contenedorNombreCliente.content.size = ancho * 1.75 // 100
        self.contenedorNombreCliente.width = ancho * 29 //100
        self.contenedorNombreCliente.height = alto * 5.87 // 100
        self.lblStockProducto.size = ancho * 1.75 // 100
        self.txtStockProducto.width = ancho * 7.78 // 100
        self.txtStockProducto.height = alto * 5.87 // 100
        self.lblStockDisponible.size = ancho * 1.75 // 100
        self.txtStockDisponible.size = ancho * 1.75 // 100
        self.txtStockActualizar.size = ancho * 1.16 // 100
        self.contenedorStockTxt.width = ancho * 9.73 // 100
        self.contenedorStockTxt.height = alto * 5.87 // 100
        self.lblDireccionPedido.size = ancho * 1.75 // 100
        self.txtDireccionPedido.width = ancho * 29 //100
        self.txtDireccionPedido.size = ancho * 1.75 // 100
        self.txtFormaPago.width = ancho * 29 // 100
        self.txtFormaPago.height = alto * 8.81 // 100
        self.lblFormaPago.size= ancho * 1.75 // 100
        if ancho <= 600:
            self.txtDireccionPedido.width = ancho * 40 //100
            self.txtFormaPago.width = ancho * 40 // 100
            self.contenedorNombreProducto.width = ancho * 40 // 100
            self.contenedorPrecio.width = ancho * 24.60 // 100
            self.contenedorMonto.width = ancho * 24.60 // 100
            self.contenedorNombreCliente.width = ancho * 40 // 100
            self.txtStockProducto.width = ancho * 15 // 100
            self.txtStockProducto.height = alto * 7 // 100
            self.contenedorStockTxt.width = ancho * 20 // 100
            self.contenedorStockTxt.height = alto * 7 // 100
            self.lblpago.size = ancho * 3 // 100
            self.lblNombreProducto.size = ancho * 2.5 // 100
            self.lblFormaPago.size= ancho * 2.5 // 100
            self.lblDireccionPedido.size = ancho * 2.5 // 100
            self.lblStockDisponible.size = ancho * 2.5 // 100
            self.lblStockProducto.size = ancho * 2.5 // 100
            self.lblNombreCliente.size = ancho * 2.5 // 100
            self.lblMonto.size=ancho * 2.5 // 100
            self.lblPrecio.size=ancho * 2.5 // 100

            for fila in range(1,len(self.contenedorPrincipal.content.controls)):
                self.contenedorPrincipal.content.controls[fila].wrap = True
        self.update()