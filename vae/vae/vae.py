import reflex as rx
import vae.styles.styles as styles
from vae.views.navbar import navbar
from vae.views.body import body
from vae.views.footer import footer

def index() -> rx.Component: 
    return rx.box(
        navbar(),
        body(),
        footer(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    
)

app.add_page(index)


