import reflex as rx
from reflex import desktop_only
from vae.styles.styles import Size, BackgroundColor, TextColor

# Definicion de datos ficticios esto debe ser eliminado en la version final
data_usuarios = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]

# Ejemplo sacado de la pagina de reflex
def line_simple_usuarios():
    return rx.recharts.line_chart(
        rx.recharts.line(data_key="pv"),
        rx.recharts.line(data_key="uv"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data_usuarios,
        width="80%",
        height=300,
    )

def header() -> rx.Component:
    return desktop_only(

        # Parte inicial donde se ve el inicio contiene el buscador y la bienvenida
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Universidad de Panamá",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold"
                        ),
                        rx.text(
                            "Estadística de Revistas y Artículos Científicos",
                            font_size=Size.EXTRA_HUGE.value,
                            font_weight="bold"
                        ),
                        justify="center"
                    ),
                    flex="1",
                    margin_right="1vw"
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Bienvenidos a la página de estadísticas de revistas y artículos científicos. Aquí puedes encontrar información sobre el número de revistas y artículos por provincia, así como estadísticas por área de conocimiento.",
                            font_size=Size.EXTRA_DEFAULT.value,
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="Buscar revistas y artículos...",
                                type="search",
                                font_size=Size.EXTRA_DEFAULT.value,
                                margin_top=Size.MEDIUM.value,
                                width="70%",
                                height="2.5em",
                                border_radius="0.5em",
                                style={"padding-left": "0.5em"}
                            ),
                            rx.button(
                                "Buscar",
                                font_size=Size.EXTRA_DEFAULT.value,
                                color=TextColor.WHITE.value,
                                bg=BackgroundColor.AZUL.value,
                                border_radius="1.5em",
                                width="15%",
                                height="2.5em",
                                margin_top=Size.MEDIUM.value,
                                margin_left="0.5em"
                            ),
                            width="100%",
                        ),
                        rx.text(
                        "Explora nuestras estadísticas al instante. Ingresa un término clave y descubre datos fascinantes con un solo clic.",
                        margin_top=Size.SMALL.value,
                        class_name="wave-hand",
),
                    ),
                    flex="1",
                    margin_left="1vw"
                ),
            ),
            bg=BackgroundColor.DEFAULT.value,
            padding_x=Size.EXTRA_BIG.value,
            padding_y=Size.GIGANTIC.value,
        ),

        # En esta parte se espera que coloquen la imagen de las 4 revistas (o articulos) mas descargadas o algo simiar al tema 
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Revistas y Artículos Científicos Destacados",
                        font_size=Size.EXTRA_BIG.value,
                        font_weight="bold",
                        width="30%",
                        text_align="center"
                    ),
                    rx.text(
                        "Las revistas y artículos más descargados en la pagina oficial",
                        font_size=Size.EXTRA_DEFAULT.value,
                        width="30%",
                        text_align="center"
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="100%"
            ),

            #Aqui estan los espacios 
            rx.hstack(
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                margin_top=Size.EXTRA_BIG.value,
            ),
            padding_y=Size.GIGANTIC.value,
            bg=f"{BackgroundColor.PATTERN_URL.value}, {BackgroundColor.GRADIENT.value}"
        ),

        # En esta parte se aya la primera grafica referente al los usuarios cuantas personas activas hay en la plataforma
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Nuestra Comunidad Global en Crecimiento",
                        font_size=Size.EXTRA_BIG.value,
                        font_weight="bold",
                        width="80%",
                        text_align="center"
                    ),
                    rx.text(
                        "Descubre el impacto internacional de nuestra plataforma. Cada número representa una mente curiosa, un investigador apasionado, un profesional comprometido. ¿Te unes a nuestra red de conocimiento en expansión?",
                        font_size=Size.EXTRA_DEFAULT.value,
                        width="80%",
                        text_align="center"
                    ),
                    rx.button(
                        "Quiero ver más",
                        font_size=Size.EXTRA_DEFAULT.value,
                        color=TextColor.WHITE.value,
                        bg=BackgroundColor.AZUL.value,
                        border_radius="1.5em",
                        width="20%",
                        height="2.5em",
                        margin_top=Size.MEDIUM.value,
                        margin_left="0.5em"
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="50%",
                margin_right="5vw"
            ),
            rx.box(
                line_simple_usuarios(),
                justify_content="center",
                align_items="center",
                width="50%",
                margin_top=Size.EXTRA_BIG.value,
            ),
            justify_content="center",
            align_items="center",
            padding_x=Size.EXTRA_SMALL.value,
            padding_y=Size.GIGANTIC.value,
            bg=BackgroundColor.DEFAULT.value,
        ),


        # En esta es la segunda grafica es lo mismo que la primera pero a la inversa se espera una grafica comparativa de usuarios locales y extranjeros 
        rx.hstack(
            rx.box(
                line_simple_usuarios(),
                justify_content="center",
                align_items="center",
                width="50%",
                margin_left="5vw",
            ),
            rx.box(
                rx.vstack(
                    rx.text(
                        "Uniendo Mentes: Del Local al Global",
                        font_size=Size.EXTRA_BIG.value,
                        font_weight="bold",
                        width="80%",
                        text_align="center"
                    ),
                    rx.text(
                        "Explora la diversidad de nuestra comunidad académica. Desde investigadores locales hasta colaboradores internacionales, cada miembro aporta una perspectiva única. Descubre cómo el conocimiento trasciende fronteras en nuestra plataforma. ¿Listo para ser parte de este intercambio global de ideas?",
                        font_size=Size.EXTRA_DEFAULT.value,
                        width="80%",
                        text_align="center"
                    ),
                    rx.button(
                        "Quiero ver más",
                        font_size=Size.EXTRA_DEFAULT.value,
                        color=TextColor.WHITE.value,
                        bg=BackgroundColor.AZUL.value,
                        border_radius="1.5em",
                        width="20%",
                        height="2.5em",
                        margin_top=Size.MEDIUM.value,
                        margin_left="0.5em"
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="50%",
                margin_right="5vw"
            ),
            justify_content="center",
            align_items="center",
            padding_x=Size.EXTRA_SMALL.value,
            padding_y=Size.HUGE.value,
            bg=BackgroundColor.DEFAULT.value,
        ),


        # En esta parte se espera que coloquen las ultima 4 revistas (o articulos) que se han subido a la plataforma
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Lo último en revistas, articulos, etc.",
                        font_size=Size.EXTRA_BIG.value,
                        font_weight="bold",
                        width="30%",
                        text_align="center"
                    ),
                    rx.text(
                        "Descubre las últimas publicaciones en nuestra plataforma. Encuentra información actualizada sobre revistas, artículos, investigaciones y mucho más.",
                        font_size=Size.EXTRA_DEFAULT.value,
                        width="30%",
                        text_align="center"
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="100%"
            ),
            rx.hstack(
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    width="20%",
                    height="350px",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                margin_top=Size.EXTRA_BIG.value,
            ),
            padding_y=Size.GIGANTIC.value,
            bg=f"{BackgroundColor.PATTERN_URL.value}, {BackgroundColor.GRADIENT.value}"
        ),


        # En esta parte la grafica se basa en las descargas generales que hay en la plataforma 
        rx.hstack(
            rx.box(
                line_simple_usuarios(),
                justify_content="center",
                align_items="center",
                width="50%",
                margin_left="5vw",
                margin_top=Size.EXTRA_BIG.value,
            ),
            rx.box(
                rx.vstack(
                    rx.text(
                        "El Impacto Medido en Clics",
                        font_size=Size.EXTRA_BIG.value,
                        font_weight="bold",
                        width="80%",
                        text_align="center"
                    ),
                    rx.text(
                        "Visualiza la sed de conocimiento en tiempo real. Cada descarga es una idea compartida, un concepto explorado, una innovación en potencia. ¿Qué artículo inspirará tu próximo gran avance?",
                        font_size=Size.EXTRA_DEFAULT.value,
                        width="80%",
                        text_align="center"
                    ),
                    rx.button(
                        "Quiero ver más",
                        font_size=Size.EXTRA_DEFAULT.value,
                        color=TextColor.WHITE.value,
                        bg=BackgroundColor.AZUL.value,
                        border_radius="1.5em",
                        width="20%",
                        height="2.5em",
                        margin_top=Size.MEDIUM.value,
                        margin_left="0.5em"
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="50%",
                margin_right="5vw"
            ),
            justify_content="center",
            align_items="center",
            padding_x=Size.EXTRA_SMALL.value,
            padding_y=Size.GIGANTIC.value,
            bg=BackgroundColor.DEFAULT.value,
        ), 
    )

# se aclara que de momento solo esta el contenido de pc y no de movil, tambien que el dinamismo (movimiento de los patrones, animaciones y otros componentes) no fueron implementados el dia de hoy
