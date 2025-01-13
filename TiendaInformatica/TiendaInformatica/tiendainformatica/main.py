
import flet as ft
from views.main_view import Main_Window

def main(page:ft.Page):
    try:
        page.title = "Tienda Informática - Proyecto ABP"

        index = Main_Window(page.width,page.height) # Pantalla principal

        page.views.append(index)
        page.update() # Siempre que quieras actualizar contenido hay que actulizar
        
        index.page.on_resized = index.ajustarPantalla
        index.ajustarPantalla()

    except ConnectionError:  
        error = ft.SnackBar(ft.Text("Error: No se pudo conectar a la base de datos. Intente más tarde."), bgcolor="red")
        error.open = True
        page.overlay.append(error) 
        page.update()
    except Exception as e: 
        errorInesperado = ft.SnackBar(ft.Text(f"Error inesperado: {str(e)}"), bgcolor="red")
        errorInesperado.open = True
        page.overlay.append(errorInesperado)
        page.update()

if __name__ == "__main__":
    ft.app(target=main) 