import reflex as rx
import vae.styles.styles as styles

from vae.views.navbar import navbar
from vae.views.header import header
from .table_render import tabla
from database.querys import Querys_return


def index() -> rx.Component:
    return rx.box(
        navbar(),
        header(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(index)


