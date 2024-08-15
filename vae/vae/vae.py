import reflex as rx
from states.totals import Totals


def index() -> rx.Component: # Función para la página de inicio
    return rx.container(
        rx.text(Totals.journals_total),
        rx.text(Totals.volumen_total),
        rx.text(Totals.arti_ess_total),
        rx.text(Totals.users_total),
        rx.text(Totals.users_pa_total),
        rx.text(Totals.users_ext_total),
        rx.text(Totals.downloads_total),
        rx.color_mode.button(position="top-right"))

# Se crea una instancia de la clase App y se añade la página index
app = rx.App()
app.add_page(index)
