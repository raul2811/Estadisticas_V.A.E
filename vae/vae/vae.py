
import reflex as rx
from typing import List
from database.querys import Querys_return

class State(rx.State):
    journals_r_content= Querys_return.journals_r_content
    issues_r_content=Querys_return.issues_r_content

def table_cell(issues_r_content: List[str]):
    return rx.table.cell((issues_r_content))


def table_row_header_cell(journals_r_content: List[str]):
        return rx.table.row_header_cell(journals_r_content) # Elemento de la primera lista


def table_row():
    return rx.table.row(
        rx.foreach(State.journals_r_content, table_row_header_cell), # Recorrer la lista de registros y crear la tabla 
        rx.foreach(State.issues_r_content, table_cell),
    )


def tabla(): # Función para crear la tabla
        return rx.vstack(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                    rx.table.column_header_cell("path"),
                    rx.table.column_header_cell("date_published"),
                ),
                ),
                rx.table.body(
                    rx.foreach(None, table_row),
                          ),     
                ),
                direction="column",
                spacing="2",   
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
