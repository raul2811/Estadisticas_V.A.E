
import reflex as rx
from .table_render import tabla
from database.querys import Querys_return


#! Agregar este argumente en caso de querer usar los datos de la base de datos on_load=Querys_return.querys()
def index(on_load=Querys_return.querys()) -> rx.Component: # Función para la página de inicio , onload carga lla funcion para solicitar los datos nesesarios para el renderizado de las estadisticas 
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            tabla(), #*llama a la funcion tabla para renderizar la tabla
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

app = rx.App()
app.add_page(index)
