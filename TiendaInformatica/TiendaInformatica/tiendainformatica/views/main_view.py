
import flet as ft

from services.crud_operations import crearUsuario
from services.query_operations import consultaUsuario , consultarTipoUsuario
from utils.hash import generarHash,validarPassword

from utils.componentes import diseñoBoton,txtInput

from views.panel_view_empleado import Panel_Window_Empleado
from views.panel_view_cliente import Panel_Window_Cliente


class Main_Window(ft.View):
    def __init__(self,ancho,alto) -> None:
        super().__init__(route="/index")  # Para crear una view es necesario una ruta (por defecto es el "index")
        self.bgcolor = "#D0C2C2"
        # Posicionamos el elemento tanto horizontal como verticalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER 

        # Inicio de sesión --> Contenedor
        self.lblInicioSesion = ft.Text(value="INICIAR SESIÓN",size=ancho * 2.34 // 100, weight=ft.FontWeight.BOLD)
        self.lblInicioSesion.color = "black"

        self.contenedorTextoInicioSesion = ft.Container(
            content=self.lblInicioSesion,
            margin=ft.margin.only(top=20, bottom=20),
            bgcolor="#CA9797",  
            width=ancho * 30 // 100,          
            height=alto * 9 // 100,         
            border_radius=15,
            alignment=ft.Alignment(0, 0)  
        )

        # Usuario
        self.lblUsuario = ft.Text(value="Usuario", size=ancho * 2 // 100, weight=ft.FontWeight.BOLD)
        self.lblUsuario.color = "black"
        self.txtUsuario = txtInput()
        self.txtUsuario.width = ancho * 29 // 100
        self.txtUsuario.heigth = alto * 9 // 100

        # Contraseña
        self.lblContraseña = ft.Text(value="Contraseña",size=ancho * 2 // 100, weight=ft.FontWeight.BOLD)
        self.lblContraseña.color = "black"
        
        self.txtContraseña = txtInput()
        self.txtContraseña.password = True
        self.txtContraseña.width = ancho * 29 // 100
        self.txtContraseña.heigth = alto * 9 // 100

        # Botones
        self.btnIngresar = diseñoBoton(text="Ingresar", on_click=self.clickUsuario) 
        self.btnRegistrarse = diseñoBoton(text="Registrarse", on_click=self.registrar) 

        # Creamos un contenedor para el botón "Registrarte" dentro del principal
        self.contenedorRegistro = ft.Container()
        self.contenedorRegistro.margin = ft.margin.only(top=30)
        self.contenedorRegistro.content = self.btnRegistrarse

        # Repetir contraseña 
        self.lblRepetirContraseña = ft.Text(value="Repetir contraseña", size=ancho * 2 // 100, weight=ft.FontWeight.BOLD)
        self.lblRepetirContraseña.color = "black"

        self.txtRepetirContraseña = txtInput()
        self.txtRepetirContraseña.password = True
        self.txtRepetirContraseña.width = ancho * 29 // 100
        self.txtRepetirContraseña.heigth = alto * 9 // 100

        # Mensaje de acierto o error al entrar en la página
        self.lblMensaje = ft.Text(size=12) 
        self.lblMensaje.color = "black"

        # RadioButton para saber que puesto pertenece el usuario
        self.rbCliente = ft.Radio(value="cliente")
        self.rbAdmin = ft.Radio(value="admin")

        self.lblrbCliente = ft.Text(value="Cliente", color="black", size=15)
        self.lblrbAdmin = ft.Text(value="Administrador", color="black", size=15)

        self.radioGroup = ft.RadioGroup(
            content=ft.Column(controls=[
                ft.Row(controls=[self.rbCliente, self.lblrbCliente]), 
                ft.Row(controls=[self.rbAdmin, self.lblrbAdmin]) 
            ])  
        )

        # Creamos un contenedor para el RadioGroup 
        self.contenedorRadio = ft.Container(
            content=self.radioGroup,
            margin=ft.margin.only(top=20, left=30),
            alignment=ft.Alignment(0, 0),
        )

        self.filaLblRepetirContraseña = ft.Row(controls=[self.lblRepetirContraseña],alignment=ft.MainAxisAlignment.CENTER)
        self.filaTxtRepetirContraseña = ft.Row(controls=[self.txtRepetirContraseña],alignment=ft.MainAxisAlignment.CENTER)

        # Creamos el contenedor principal
        self.contenedorPrincipal = ft.Container(
            width=ancho * 49 // 100,
            height=475,
            bgcolor="#EBD6D6", 
            border_radius=20, 
            content=ft.Column(
                    controls=[
                        ft.Row(controls=[self.contenedorTextoInicioSesion], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.lblUsuario],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.txtUsuario],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.lblContraseña],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.txtContraseña],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.lblMensaje],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.btnIngresar],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.contenedorRegistro],alignment=ft.MainAxisAlignment.CENTER)
                    ],scroll=ft.ScrollMode.ALWAYS
                )
            )
        self.controls.append(self.contenedorPrincipal)

    # Diferentes funcionalidades que pueda hacer el usuario al hacer click
    def clickUsuario(self, e):
        if self.txtContraseña.value != "" and self.txtUsuario.value != "":
            if self.lblInicioSesion.value == "REGISTRARSE": # Si nos vamos a registrar
                if self.txtContraseña.value == self.txtRepetirContraseña.value and \
                    self.txtContraseña.value != "" and self.txtRepetirContraseña.value != "":
                    if consultaUsuario({"nombre": self.txtUsuario.value}) is None:  # NO existe un usuario con ese nombre
                        hash,sal = generarHash(self.txtContraseña.value)
                        userData = {"nombre": self.txtUsuario.value, "contrasena":hash,'sal':sal , "usuario": self.radioGroup.value}
                        crearUsuario(userData)
                        self.lblMensaje.value = "Usuario registrado correctamente"
                        self.lblMensaje.color = "green"
                        
                        print(self.radioGroup.value)
                        if self.radioGroup.value == "admin":

                            self.panelViewEmpleado()
                        else:
                            self.panelViewCliente()

                        self.limpiar()
                        self.update()
                        self.registrar(e)
                    else:
                        self.lblMensaje.value = "Error, el usuario ya existe."
                        self.lblMensaje.color = "red"
                        self.update()
                else:
                    self.lblMensaje.value = "Las contraseñas no coinciden"
                    self.lblMensaje.color = "red"
                    self.update()

            else: # Si queremos iniciar sesión
                print(self.txtUsuario.value)
                valor_nombre_consulta = {"nombre": self.txtUsuario.value}  # Asignamo a una variavle clave valor del usuario para realizar una consulta 
                usuario = consultaUsuario(valor_nombre_consulta) #Obtenemos el usuario al que se desea acceder
                print(usuario)
                if usuario is not None:
                    userData = {"nombre": self.txtUsuario.value, "contrasena": self.txtContraseña.value, "usuario": self.radioGroup.value}
                    if validarPassword(self.txtContraseña.value,usuario['sal'],usuario['contrasena']):  # Si las contraseñas encriptadas son iguales
                        self.lblMensaje.value = "Inicio de sesión exitoso"
                        self.lblMensaje.color = "green"

                        # print(self.radioGroup.value) # --> NONE
                        if consultarTipoUsuario(valor_nombre_consulta) == "admin": #llamamos a una funcion que nos devuelve el tipo de Usuario
                            self.panelViewEmpleado()
                        else:
                            self.panelViewCliente()

                        self.limpiar()
                        self.update()
                    else:
                        self.lblMensaje.value = "Error, la contraseña es incorrecta."
                        self.lblMensaje.color = "red"
                        self.update()
                else:
                    self.lblMensaje.value = "Error, el usuario ingresado no existe."
                    self.lblMensaje.color = "red"
                    self.update()

    def registrar(self, e):
        # Elementos para registrar usuario
        if self.btnRegistrarse.text == "Registrarse": 
            self.btnRegistrarse.text = "Volver"
            self.btnIngresar.text = "Confirmar"
            self.lblContraseña.value = "Nueva contraseña"
            self.lblInicioSesion.value = "REGISTRARSE"
            self.contenedorPrincipal.height = 700

            self.contenedorPrincipal.content.controls.insert(5, self.filaLblRepetirContraseña) 
            self.contenedorPrincipal.content.controls.insert(6, self.filaTxtRepetirContraseña)
            self.contenedorPrincipal.content.controls.insert(7, self.contenedorRadio)

            self.inicial()
            self.update()

        # Elementos para iniciar con un usuario
        else:
            self.contenedorPrincipal.height = 475
            self.lblInicioSesion.value = "INICIAR SESIÓN"
            self.btnRegistrarse.text = "Registrarse"
            self.btnIngresar.text = "Ingresar"
            self.lblContraseña.value = "Contraseña"

            self.contenedorPrincipal.content.controls.remove(self.filaLblRepetirContraseña)
            self.contenedorPrincipal.content.controls.remove(self.filaTxtRepetirContraseña)
            self.contenedorPrincipal.content.controls.remove(self.contenedorRadio)

            self.inicial()
            self.update()

    def inicial(self):  # Estado incial del proyecto
        self.txtUsuario.value = ""
        self.txtContraseña.value = ""
        self.txtRepetirContraseña.value = ""
        self.lblMensaje.value = ""
    
    def limpiar(self):  # Limpiamos todos los campos
        self.txtUsuario.value = ""
        self.txtContraseña.value = ""
        self.txtRepetirContraseña.value = ""

    def panelViewEmpleado(self):
        try:
            panel2 = Panel_Window_Empleado(self.page.width,self.page.height)
            panel2.nombreUsuario = self.txtUsuario.value
            self.page.views.append(panel2)
            self.page.go(self.page.views[-1].route)

            try:
                panel2.cargarProductos()
            except Exception as e:
                print(f"Error al cargar productos: {e}")
            
            try:
                panel2.cargarMarcas()
            except Exception as e:
                print(f"Error al cargar marcas: {e}")
            
            try:
                panel2.mostrarProductos()
            except Exception as e:
                print(f"Error al mostrar productos: {e}")
            
            try:
                panel2.ajustarPantalla()
            except Exception as e:
                print(f"Error al ajustar la pantalla: {e}")
            
            panel2.page.on_resized = panel2.ajustarPantalla

        except Exception as e:
            print(f"Error: {e}")
        
    def panelViewCliente(self):
        try:
            panel3 = Panel_Window_Cliente(self.page.width,self.page.height)
            panel3.nombreUsuario = self.txtUsuario.value
            self.page.views.append(panel3)
            self.page.go(self.page.views[-1].route)
            
            try:
                panel3.cargarProductos()
            except Exception as e:
                print(f"Error al cargar productos: {e}")
            
            try:
                panel3.cargarMarcas()
            except Exception as e:
                print(f"Error al cargar marcas: {e}")
            
            try:
                panel3.mostrarProductos()
            except Exception as e:
                print(f"Error al mostrar productos: {e}")
            
            try:
                panel3.ajustarPantalla()
            except Exception as e:
                print(f"Error al ajustar la pantalla: {e}")
            
            panel3.page.on_resized = panel3.ajustarPantalla

        except Exception as e:
            print(f"Error: {e}")
        
    def ajustarPantalla(self,e=None):
        ancho = self.page.width
        alto = self.page.height
        print({"Ancho":ancho},{"Alto":alto})
        self.contenedorPrincipal.width = ancho * 49 // 100
        self.contenedorPrincipal.height = alto * 60 // 100
        self.lblInicioSesion.size = ancho * 2.34 // 100
        self.lblUsuario.size = ancho * 2 // 100
        self.lblContraseña.size = ancho * 2 // 100
        self.contenedorTextoInicioSesion.width = ancho * 30 // 100
        self.contenedorTextoInicioSesion.height = alto * 9 // 100
        self.txtUsuario.width = ancho * 29 // 100
        self.txtUsuario.height = alto * 9 // 100
        self.txtContraseña.width = ancho * 29 // 100
        self.txtContraseña.height = alto * 9 // 100
        if ancho < 500:
            self.contenedorPrincipal.width = ancho * 60 // 100
            self.lblInicioSesion.size = ancho * 3.5 // 100
            self.lblUsuario.size = ancho * 3 // 100
            self.lblContraseña.size = ancho * 3 // 100
            self.lblRepetirContraseña.size=ancho * 3 // 100
        self.update()