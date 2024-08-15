import reflex as rx
import vae.styles.styles as styles
from vae.views.navbar import navbar
from vae.views.header import header

def index() -> rx.Component: # Función para la página de inicio
    return rx.box(
        navbar(),
        header(),
    )

# Se crea una instancia de la clase App y se añade la página index
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(index)


