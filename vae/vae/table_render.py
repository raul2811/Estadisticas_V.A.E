import reflex as rx
from typing import List
from database.querys import Querys_return

class State(rx.State):
    journals_r_content= Querys_return.journals_r_content
    issues_r_content=Querys_return.issues_r_content

def table_row_header_cell(journals_r_content: List[str]):
        return rx.table.row( 
            rx.table.row_header_cell(journals_r_content) # Elemento de la primera lista
        )

def tabla(): # Función para crear la tabla
        return rx.vstack(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                    rx.table.column_header_cell("path"),
                ),
                ),
                rx.table.body(
                    rx.foreach(State.journals_r_content, table_row_header_cell),
                          ),     
                ),
                direction="column",
                spacing="2",   
        )