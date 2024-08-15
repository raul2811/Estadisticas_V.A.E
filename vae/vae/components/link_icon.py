import reflex as rx
from vae.styles.styles import Size



def link_icon(icon: str, url: str) -> rx.Component:
    image_src = f"/{icon}" 
    
    return rx.link(
        rx.image(
            src=image_src,
            alt=icon,
            width=Size.EXTRA_BIG.value,
            height=Size.EXTRA_BIG.value
        ),
        margin_top=Size.EXTRA_SMALL.value,
        padding_x=Size.SMALL.value,
        href=url,
        is_external=True,
    )

def facultades (icon: str, url: str) -> rx.Component:
    image_src = f"/{icon}" 

    return rx.link(
        rx.image(
            src=image_src,
            alt=icon,
            width=Size.MASSIVE.value,
            height=Size.MASSIVE.value
        ),
        margin_top=Size.EXTRA_SMALL.value,
        padding_x=Size.HUGE.value,
        href=url,
        is_external=True,
    )

def universidades (icon: str, url: str) -> rx.Component:
    image_src = f"/{icon}" 

    return rx.link(
        rx.image(
            src=image_src,
            alt=icon,
            width=Size.MASSIVE.value,
            height=Size.MASSIVE.value
        ),
        margin_top=Size.EXTRA_SMALL.value,
        padding_x=Size.HUGE.value,
        href=url,
        is_external=True,
    )

def redes (icon: str, url: str) -> rx.Component:
    image_src = f"/{icon}" 

    return rx.link(
        rx.image(
            src=image_src,
            alt=icon,
            width=Size.EXTRA_BIG.value,
            height=Size.EXTRA_BIG.value
        ),
        margin_top=Size.EXTRA_SMALL.value,
        padding_x=Size.HUGE.value,
        href=url,
        is_external=True,
    )