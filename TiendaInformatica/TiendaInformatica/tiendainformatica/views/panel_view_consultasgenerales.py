import flet as ft

from utils.componentes import diseñoBoton, txtDesplegable
from services.query_operations import consultaProductoMasVendido, consultaCantidadVendidaProducto, consultaProductoMasVendidoPorCategoria, consultaProductoMasVendidoPorMarca, consultaDineroRecaudado

class Panel_Window_ConsultasGenerales(ft.View):
    def __init__(self) -> None:
        super().__init__(route="/consultas")  
        self.bgcolor = "#D0C2C2"
        self.scroll = ft.ScrollMode.ALWAYS
        # Posicionamos el elemento tanto horizontal como verticalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER 

        # Inicio de sesión --> Contenedor
        self.lblDatos = ft.Text(value="CONSULTAS GENERALES", size=24, weight=ft.FontWeight.BOLD)
        self.lblDatos.color = "black"

        self.contenedorTextoDatos = ft.Container(
            content=self.lblDatos,
            margin=ft.margin.only(top=20, bottom=20),
            bgcolor="#CA9797",  
            width=300,          
            height=60,         
            border_radius=15,
            alignment=ft.Alignment(0, 0)  
        )

        # Creamos el AlertDialog para mostrar los resultados
        self.alertDialogo = ft.AlertDialog(
            title=ft.Text("Resultado", color="#000000"),
            bgcolor="#ffffff", 
            actions=[diseñoBoton("Cerrar", on_click=lambda e: self.cerrarDialogo())]
        )

        # Consultas generales sobre los productos vendidos
        self.consulta01 = diseñoBoton(text="Producto más vendido", on_click=lambda e: self.mostrarResultado(consultaProductoMasVendido))
        self.consulta01.bgcolor = "#94AA94"
        self.consulta02 = diseñoBoton(text="Producto más vendido (por categoría)", on_click=lambda e: self.mostrarResultadoCategoria(consultaProductoMasVendidoPorCategoria))
        self.consulta02.bgcolor = "#94AA94"
        self.consulta03 = diseñoBoton(text="Producto más vendido (por marca)", on_click=lambda e: self.mostrarResultadoMarcas(consultaProductoMasVendidoPorMarca))
        self.consulta03.bgcolor = "#94AA94"
        self.consulta04 = diseñoBoton(text="Cantidad de producto vendido (cada uno)", on_click=lambda e: self.mostrarResultado(consultaCantidadVendidaProducto)) 
        self.consulta04.bgcolor = "#94AA94"
        self.consulta05 = diseñoBoton(text="Dinero recaudado por productos", on_click=lambda e: self.mostrarResultadoRecaudacion(consultaDineroRecaudado))
        self.consulta05.bgcolor = "#94AA94"
        self.botonVolver = diseñoBoton(text="Volver", on_click = lambda e: self.panelViewVolver(e))

        # Creamos el contenedor principal
        self.contenedorPrincipal = ft.Container(
            width=400,
            height=450,
            bgcolor="#EBD6D6", 
            border_radius=20, 
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.contenedorTextoDatos], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.consulta01], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.consulta02], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.consulta03], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.consulta04], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.consulta05], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.botonVolver], alignment=ft.MainAxisAlignment.CENTER),
                    ]
                )
            )
        self.controls.append(self.contenedorPrincipal)
        self.controls.append(self.alertDialogo) 

    def mostrarResultado(self, funcion): # --> Tabla para consultas producto mas vendido / cantidad de producto vendido (de cada uno)
        try:
            resultados = funcion()
            if resultados: 
                
                # Creamos una tabla para que los datos se muestren 
                tabla = ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Nombre Producto", color="#ff0000")),
                        ft.DataColumn(ft.Text("Cantidad Vendida", color="#ff0000"))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(producto["nombre"], color="#000000")),
                                ft.DataCell(ft.Text(str(producto["cantidad"]), color="#000000")),
                            ]
                        )
                        for producto in resultados 
                    ],
                )

                # Poder hacer scroll debido a que puede haber consultas muy grandes
                tablaScroll = ft.Container( 
                    content=ft.Column(
                        controls=[tabla],
                        width=350,  
                        height=200,  
                        scroll=True 
                    )
                )
                
                self.alertDialogo.content = tablaScroll
            else:
                self.alertDialogo.content = ft.Text("No se encontraron resultados.")

            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()

        except Exception as e:
            print(f"Error al ejecutar la función: {e}")
            self.alertDialogo.content = ft.Text(value=f"Error: {e}")
            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()

    def mostrarResultadoCategoria(self, funcion):  # --> Tabla para consultas separar por categorías
        try:
            resultados = funcion()
            if resultados:
                tabla = ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Categoria", color="#ff0000")),
                        ft.DataColumn(ft.Text("Nombre Producto", color="#ff0000")),
                        ft.DataColumn(ft.Text("Cantidad Vendida", color="#ff0000"))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(producto["categoria"], color="#000000")),
                                ft.DataCell(ft.Text(producto["nombre"], color="#000000")),
                                ft.DataCell(ft.Text(str(producto["cantidad"]), color="#000000")),
                            ]
                        )
                        for producto in resultados
                    ],
                )

                tablaScroll = ft.Container(
                    content=ft.Column(
                        controls=[tabla],
                        width=450,  
                        height=200,  
                        scroll=True 
                    )
                )
                
                self.alertDialogo.content = tablaScroll
            else:
                self.alertDialogo.content = ft.Text("No se encontraron resultados.")

            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()

        except Exception as e:
            print(f"Error al ejecutar la función: {e}")
            self.alertDialogo.content = ft.Text(value=f"Error: {e}")
            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()


    def mostrarResultadoMarcas(self, funcion): # --> Tabla para consultas separar por marcas
        try:
            resultados = funcion()
            if resultados:
                tabla = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Marca", color="#ff0000")),
                    ft.DataColumn(ft.Text("Nombre Producto", color="#ff0000")),
                    ft.DataColumn(ft.Text("Cantidad Vendida", color="#ff0000"))
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(producto["marca"], color="#000000")),
                            ft.DataCell(ft.Text(producto["nombre"], color="#000000")),
                            ft.DataCell(ft.Text(str(producto["cantidad"]), color="#000000")),
                        ]
                    )
                    for producto in resultados 
                ],
                )
                                
                tablaScroll = ft.Container(
                    content=ft.Column(
                        controls=[tabla],
                        width=450,  
                        height=200,  
                        scroll=True 
                    )
                )
                
                self.alertDialogo.content = tablaScroll
            else:
                self.alertDialogo.content = ft.Text("No se encontraron resultados.")

            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()

        except Exception as e:
            print(f"Error al ejecutar la función: {e}")
            self.alertDialogo.content = ft.Text(value=f"Error: {e}")
            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()

    def mostrarResultadoRecaudacion(self, funcion): # --> Tabla para consultas total de recaudacion
        try:
            resultados = funcion()
            if resultados: 
                tabla = ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Recaudacion Total", color="#ff0000"))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(str(producto["cantidad"]), color="#000000")),
                            ]
                        )
                        for producto in resultados 
                    ],
                )
                self.alertDialogo.content = tabla
            else:
                self.alertDialogo.content = ft.Text("No se encontraron resultados.")

            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()

        except Exception as e:
            print(f"Error al ejecutar la función: {e}")
            self.alertDialogo.content = ft.Text(value=f"Error: {e}")
            self.page.dialog = self.alertDialogo
            self.alertDialogo.open = True
            self.page.update()

    def cerrarDialogo(self):
        self.alertDialogo.open = False  
        self.page.update() 

    def panelViewVolver(self, e):
        self.page.views.pop()  
        self.page.go(self.page.views[-1].route)