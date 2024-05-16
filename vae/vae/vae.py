"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from typing import List
from rxconfig import config
from database.table_test import Consultar ,consultar_tabla

class State(rx.State):
    registro_list = Consultar.registro_lista
         
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

def index(on_load=consultar_tabla()) -> rx.Component:
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
