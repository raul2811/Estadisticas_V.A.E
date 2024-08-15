import reflex as rx
from database.querys import Querys_return


#! agregar este argumente en caso de querer usar los datos de la base de datos on_load=Querys_return.querys()
def index(on_load=Querys_return.querys()) -> rx.Component: # Función para la página de inicio , onload carga lla funcion para solicitar los datos nesesarios para el renderizado de las estadisticas 
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
    )

app = rx.App()
app.add_page(index)
