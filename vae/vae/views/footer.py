import reflex as rx
import vae.constants as constants
from vae.styles.styles import Size, BackgroundColor, TextColor

def footer() -> rx.Component:
    return rx.desktop_only(
        rx.hstack(
            rx.box(
                rx.text(
                    "Revistas UP",
                    font_size="20px",
                    padding_x="2.8em",
                    margin_top=Size.DEFAULT.value,
                    cursor="pointer",
                    _hover={"color": TextColor.HOVER.value}
                ),
                rx.link(
                    rx.text(
                        "+507 6839-5958",
                        cursor="pointer",
                        padding_x=Size.HUGE.value,
                        margin_top=Size.DEFAULT.value,
                        _hover={"color": TextColor.HOVER.value}
                    ),
                    href="https://opac.up.ac.pa/",
                    is_external=True
                ),
                align_items="center",
                justify_content="flex-start"
            ),
            rx.spacer(),
            rx.hstack(
                rx.box(
                    rx.text(
                        "Universidad de Panamá",
                        font_size="20px",
                        padding_x="2.8em",
                        margin_top=Size.DEFAULT.value,
                        cursor="pointer",
                        _hover={"color": TextColor.HOVER.value}
                    ),
                    rx.link(
                        rx.text(
                            "Pagina Web",
                            cursor="pointer",
                            padding_x=Size.HUGE.value,
                            margin_top=Size.DEFAULT.value,
                            _hover={"color": TextColor.HOVER.value}
                        ),
                        href="https://opac.up.ac.pa/",
                        is_external=True
                    ),
                    rx.link(
                        rx.text(
                            "Vicerrectoría de Investigación y Postgrado",
                            cursor="pointer",
                            padding_x=Size.HUGE.value,
                            margin_top=Size.DEFAULT.value,
                            _hover={"color": TextColor.HOVER.value}
                        ),
                        href="https://opac.up.ac.pa/",
                        is_external=True
                    ),
                    rx.link(
                        rx.text(
                            "Vicerrectoría Académica",
                            cursor="pointer",
                            padding_x=Size.HUGE.value,
                            margin_top=Size.DEFAULT.value,
                            _hover={"color": TextColor.HOVER.value}
                        ),
                        href="https://opac.up.ac.pa/",
                        is_external=True
                    ),
                    rx.link(
                        rx.text(
                            "Sistema de Bibliotecas de la Universidad de Panamá",
                            cursor="pointer",
                            padding_x=Size.HUGE.value,
                            margin_top=Size.DEFAULT.value,
                            _hover={"color": TextColor.HOVER.value}
                        ),
                        href="https://opac.up.ac.pa/",
                        is_external=True
                    ),
                    align_items="center",
                    justify_content="flex-start"
                ),
                rx.spacer(),
                rx.box(
                    rx.text(
                        "Servicios de Información",
                        font_size="20px",
                        padding_x="2.8em",
                        margin_top=Size.DEFAULT.value,
                        cursor="pointer",
                        _hover={"color": TextColor.HOVER.value}
                    ),
                    rx.link(
                        rx.text(
                            "Información General",
                            cursor="pointer",
                            padding_x=Size.HUGE.value,
                            margin_top=Size.DEFAULT.value,
                            _hover={"color": TextColor.HOVER.value}
                        ),
                        href="https://opac.up.ac.pa/",
                        is_external=True
                    ),
                    rx.link(
                        rx.text(
                            "Repositorio Institucional Digital de la Universidad de Panamá",
                            cursor="pointer",
                            padding_x=Size.HUGE.value,
                            margin_top=Size.DEFAULT.value,
                            _hover={"color": TextColor.HOVER.value}
                        ),
                        href="https://opac.up.ac.pa/",
                        is_external=True
                    ),
                    rx.link(
                        rx.text(
                            "Amelica Centroamérica Colección Digital de Revistas Académicas Centroamérica",
                            cursor="pointer",
                            padding_x=Size.HUGE.value,
                            margin_top=Size.DEFAULT.value,
                            _hover={"color": TextColor.HOVER.value}
                        ),
                        href="https://opac.up.ac.pa/",
                        is_external=True
                    ),
                    align_items="center",
                    justify_content="flex-start"
                )
            ),
            bg=BackgroundColor.DEFAULT.value,
            padding_x=Size.EXTRA_BIG.value,
            padding_y=Size.GIGANTIC.value,
            class_name="flex align-center justify-center"
        ),
        rx.text(
                "Universidad de Panamá © 2024. - Vicerrectoria de Investigación y Postgrado",
                bg=BackgroundColor.DEFAULT.value,
                padding_x=Size.EXTRA_BIG.value,
                padding_y=Size.SMALL.value,
                class_name="flex align-center justify-center",
                color=TextColor.HOVER.value
            )

    )
