import reflex as rx
import vae.constants as constants

from vae.styles.styles import Size, BackgroundColor, TextColor
from vae.components.link_icon import link_icon
from reflex import desktop_only

def navbar() -> rx.Component:
    return desktop_only(
        rx.vstack(
            rx.hstack(
                rx.image(
                    src="user.svg",
                    alt="Avatar de usuario",
                    width=Size.BIG.value,
                    height=Size.MEDIUM.value,
                    margin_top=Size.DEFAULT.value,
                    cursor="pointer",
                ),
                rx.text("Usuarios", padding_x=Size.HUGE.value, margin_top=Size.DEFAULT.value, cursor="pointer", _hover={"color": TextColor.HOVER.value}),
                rx.text("Articulos y Revistas", padding_x=Size.HUGE.value, margin_top=Size.DEFAULT.value, cursor="pointer", _hover={"color": TextColor.HOVER.value}),
                rx.text("Descargas", padding_x=Size.HUGE.value, margin_top=Size.DEFAULT.value, cursor="pointer", _hover={"color": TextColor.HOVER.value}),
                
                rx.spacer(),
                link_icon(
                    "logo.svg",
                    constants.REVISTAS_UP
                ),
                link_icon(
                    "uplogo.png",
                    constants.UNIVERSIDAD_URL
                ),
                rx.color_mode.button(
                    margin_top=Size.DEFAULT.value,
                    width=Size.BIG.value,
                    height=Size.MEDIUM.value,
                    disabled=True, 
                ),
                width="100%",
            ),
            bg=BackgroundColor.DEFAULT.value,
            position="sticky",
            padding_x=Size.MEDIUM.value,
            padding_y=Size.DEFAULT.value,
        )
    )