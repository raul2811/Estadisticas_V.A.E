
import reflex as rx
from typing import List
from database.querys import Querys_return

class State(rx.State):
    registro_list = Querys_return.journals_r_content
    total_registros_count = Querys_return.total_r_journals
def table_row(registro_list:List[str]):
        return rx.table.row(
            rx.table.row_header_cell((registro_list)),
        )
def tabla(): # Función para crear la tabla
        return rx.vstack(
            rx.table.root(
                rx.table.header(rx.table.row(
                    rx.table.column_header_cell("path"),
                ),
                ),
                rx.table.body(
                rx.foreach(State.registro_list, table_row) # Recorrer la lista de registros y crear la tabla
                ),
                ),
        )

def index(on_load=Querys_return.querys()) -> rx.Component: # Función para la página de inicio , onload carga lla funcion para solicitar los datos nesesarios para el renderizado de las estadisticas 
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            tabla(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
app = rx.App()
app.add_page(index)
