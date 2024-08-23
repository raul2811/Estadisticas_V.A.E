import reflex as rx
import vae.constants as constants
from states.Statistics import Totals
#from states.Submission_Downloads_top import Submission_Downloads_top
from reflex import desktop_only
from vae.styles.styles import Size, BackgroundColor, TextColor
from vae.components.link_icon import facultades, universidades, redes


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

rx.html(
    """
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        function handleScroll() {
            document.querySelectorAll('.slide-in').forEach(function(element) {
                const slideInAt = (window.scrollY + window.innerHeight) - element.offsetHeight / 8;
                const isHalfShown = slideInAt > element.offsetTop;
                const isNotScrolledPast = window.scrollY < element.offsetTop + element.offsetHeight;
                if (isHalfShown && isNotScrolledPast) {
                    element.classList.add('active');
                } else {
                    element.classList.remove('active');
                }
            });
        }

        window.addEventListener('scroll', handleScroll);
        
        // Llama a handleScroll inicialmente para manejar elementos que ya están en la vista
        handleScroll();
    });
    </script>
    """
)

class TypingState(rx.State):
    def start_typing(self):
        return rx.call_script("startTypingEffect()")


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

def body() -> rx.Component:
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
                    font_size=Size.HUGE.value,
                    font_weight="bold"
                ),
                justify="center"
            ),
            class_name="flex-1 mr-[1vw] animate-slide-in-left",  
            id="left-content"
        ),
        rx.box(
            rx.vstack(
                rx.text(
                    "Bienvenidos a la página de estadísticas de revistas y artículos científicos. Este portal te ofrece una visión completa del impacto de nuestras publicaciones, incluyendo información sobre el número de usuarios registrados, la cantidad de artículos disponibles, y estadísticas detalladas de descargas.",
                    font_size=Size.EXTRA_DEFAULT.value,
                ),
                rx.html(
                    """
                    <div id="typing-container" style="font-size: {}; font-weight: bold; margin-top: {}; color: {}; white-space: nowrap;">
                        <span id="typing-text"></span><span id="cursor" style="visibility: visible;">|</span>
                    </div>
                    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                    <script>
                        function startTypingEffect() {{
                            const sentences = [
                                "Más de 10,000 usuarios registrados confían en nuestra plataforma.",
                                "Superamos el millón de descargas en artículos científicos.",
                                "Apoyando la investigación nacional y extranjera.",
                                "Facilitando el acceso a datos científicos de calidad.",
                                "Promoviendo la difusión del conocimiento en Panamá."
                            ];
                            let currentSentence = 0;
                            let currentChar = 0;
                            let isTyping = true;

                            function typeChar() {{
                                if (currentChar < sentences[currentSentence].length) {{
                                    $("#typing-text").text(function(_, text) {{
                                        return text + sentences[currentSentence][currentChar];
                                    }});
                                    currentChar++;
                                    setTimeout(typeChar, 50);
                                }} else if (isTyping) {{
                                    isTyping = false;
                                    setTimeout(eraseChar, 2000);
                                }}
                            }}

                            function eraseChar() {{
                                if (currentChar > 0) {{
                                    $("#typing-text").text(function(_, text) {{
                                        return text.slice(0, -1);
                                    }});
                                    currentChar--;
                                    setTimeout(eraseChar, 20);
                                }} else {{
                                    isTyping = true;
                                    currentSentence = (currentSentence + 1) % sentences.length;
                                    setTimeout(typeChar, 500);
                                }}
                            }}

                            function toggleCursor() {{
                                $("#cursor").css("visibility", function(_, visibility) {{
                                    return visibility === 'visible' ? 'hidden' : 'visible';
                                }});
                            }}

                            setInterval(toggleCursor, 500);
                            typeChar();
                        }}
                        $(document).ready(function() {{
                            startTypingEffect();
                        }});
                    </script>
                    """,
                    margin_top=Size.BIG.value,
                ),
                rx.text(
                    "Descubre los últimos avances científicos y cómo impactan en nuestra comunidad.",
                    margin_top=Size.SMALL.value,
                ),
            ),
            class_name="flex-1 mr-[1vw] animate-slide-in-right",  
            id="right-content"
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
                        class_name="font-bold w-[30%] text-center"
                    ),
                    rx.text(
                        "Las revistas y artículos más descargados en la pagina oficial",
                        font_size=Size.EXTRA_DEFAULT.value,
                        class_name="w-[30%] text-center"
                    ),
                    class_name="items-center w-full"
                ),
                class_name="flex w-full"
            ),

            #Aqui estan los espacios 
            rx.hstack(
                rx.image(
                    src="ejemplo.jpg",
                    class_name="w-[20%] h-[400px]",
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    class_name="w-[20%] h-[400px]",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    class_name="w-[20%] h-[400px]",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    class_name="w-[20%] h-[400px]",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                class_name="justify-center items-center w-full",
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
                        class_name="font-bold w-[80%] text-center"
                    ),
                    rx.text(
                        "Descubre el impacto internacional de nuestra plataforma. Cada número representa una mente curiosa, un investigador apasionado, un profesional comprometido. ¿Te unes a nuestra red de conocimiento en expansión?",
                        font_size=Size.EXTRA_DEFAULT.value,
                        class_name="w-[80%] text-center"
                    ),
                    rx.button(
                        "Quiero ver más",
                        font_size=Size.EXTRA_DEFAULT.value,
                        color=TextColor.WHITE.value,
                        bg=BackgroundColor.AZUL.value,
                        class_name="rounded-[1.5em] w-[20%] h-[2.5em] mt-[valor]",
                        margin_top=Size.MEDIUM.value,
                    ),
                    class_name="items-center w-full"
                ),
                class_name="flex w-[50%] mr-[5vw]"
            ),
            rx.box(
                line_simple_usuarios(),
                justify_content="center",
                align_items="center",
                width="50%",
                margin_top=Size.EXTRA_BIG.value,
            ),
            class_name="justify-center items-center",
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
                        "El Impacto Medido en Clicks",
                        font_size=Size.EXTRA_BIG.value,
                        class_name="font-bold w-[80%] text-center",
                    ),
                    rx.text(
                        "Visualiza la sed de conocimiento en tiempo real. Cada descarga es una idea compartida, un concepto explorado, una innovación en potencia. ¿Qué artículo inspirará tu próximo gran avance?",
                        font_size=Size.EXTRA_DEFAULT.value,
                        class_name="w-[80%] text-center",
                    ),
                    rx.button(
                        "Quiero ver más",
                        font_size=Size.EXTRA_DEFAULT.value,
                        color=TextColor.WHITE.value,
                        bg=BackgroundColor.AZUL.value,
                        margin_top=Size.MEDIUM.value,
                        class_name="rounded-[1.5em] w-[20%] h-[2.5em] ml-[0.5em]"
                    ),
                    class_name="items-center w-full"
                ),
                display="flex",
                width="50%",
                margin_right="1vw"
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
                        class_name="font-bold w-[30%] text-center",
                    ),
                    rx.text(
                        "Descubre las últimas publicaciones en nuestra plataforma. Encuentra información actualizada sobre revistas, artículos, investigaciones y mucho más.",
                        font_size=Size.EXTRA_DEFAULT.value,
                        margin_top=Size.SMALL.value,
                        class_name="w-[40%] text-center",
                    ),
                    class_name="items-center w-full"
                ),
                class_name="flex w-full"
            ),
            rx.hstack(
                rx.box(
                    class_name="w-[20%] h-[400px]",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    class_name="w-[20%] h-[400px]",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    class_name="w-[20%] h-[400px]",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                rx.box(
                    class_name="w-[20%] h-[400px]",
                    bg=BackgroundColor.DEFAULT.value,
                    margin_x=Size.SMALL.value
                ),
                class_name="justify-center items-center w-full",
                margin_top=Size.EXTRA_BIG.value,
            ),
            padding_y=Size.GIGANTIC.value,
            bg=f"{BackgroundColor.PATTERN_URL.value}, {BackgroundColor.GRADIENT.value}"
        ),

        # En esta parte se espera que coloquen las facultades de la universidad de panama y que al darle click a una te lleve a la pagina de la facultad
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Explora las contribuciones más recientes de nuestras facultades. Accede a publicaciones y estudios innovadores de diversas áreas académicas.",
                        font_size=Size.EXTRA_DEFAULT.value,
                        margin_top=Size.SMALL.value,
                        class_name="w-[50%] text-center"
                    ),
                    class_name="items-center w-full"
                ),
                class_name="flex w-full"
            ),
            rx.hstack(
                facultades(
                    "humanidades.svg",
                    constants.HUMANIDADES_URL
                ),
                 facultades(
                    "derecho.png",
                    constants.DERECHO_URL
                ),
                facultades(
                    "exactas.webp",
                    constants.CIENCIAS_URL
                ),
                 facultades(
                    "artes.svg",
                    constants.BELLAS_ARTES_URL
                ),
                facultades(
                    "economia.png",
                    constants.ECONOMIA_URL
                ),
                 facultades(
                    "fiec.png",
                    constants.FIEC_URL
                ),
                class_name="justify-center items-center w-full",
                margin_top=Size.MEDIUM.value,
            ),
            padding_y=Size.GIGANTIC.value,
            bg=BackgroundColor.DEFAULT.value,
        ),

        # Esta es la primera seccion de estadisticas de usuarios se espera que se muestre el total de usuarios nacionales, extranjeros y otro dato que puedan sacar
         rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Nacionales vs Extranjeros",
                        font_size=Size.EXTRA_BIG.value,
                        class_name="font-bold w-2/5 text-center"
                    ),
                    rx.text(
                        "Explora la dinámica de nuestra comunidad de usuarios con un desglose detallado del total de registros. Descubre cuántos usuarios son locales y cuántos provienen de otros países, ofreciendo una perspectiva clara sobre el alcance global de nuestras publicaciones.",
                        font_size=Size.EXTRA_DEFAULT.value,
                        class_name="w-2/5 text-center",
                        margin_top=Size.SMALL.value
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="100%"
                ),
                rx.hstack(
                    rx.vstack(
                        rx.image(
                            src="varios.svg",
                            alt="Imagen de la seccion de usuarios",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            Totals.users_pa_total, #usuarios nacionales
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Usuarios Nacionales",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                    rx.vstack(
                        rx.image(
                            src="varios.svg",
                            alt="Imagen de la seccion de usuarios",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            Totals.users_total,#usuarios totales 
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Usuarios Totales",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                    rx.vstack(
                        rx.image(
                            src="varios.svg",
                            alt="Imagen de la seccion de usuarios",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            Totals.users_ext_total, # usuarios extranjeros
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Usuarios Extranjeros",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                        class_name="justify-center items-center w-full",
                        margin_top=Size.EXTRA_BIG.value,
                    ),
                    padding_y=Size.GIGANTIC.value,
                    bg=f"{BackgroundColor.PATTERN_URL.value}, {BackgroundColor.GRADIENT.value}"
                ),

            # En esta parte se colocan las universidades aliadas de la universidad de panama
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Nuestra Universidad se enorgullece de colaborar con una red selecta de universidades aliadas, reconocidas por su excelencia académica y su compromiso con la investigación de vanguardia. Estas alianzas nos permiten ofrecer un contenido enriquecido y diverso, garantizando que nuestros usuarios tengan acceso a investigaciones y publicaciones de alto impacto, provenientes de instituciones educativas líderes a nivel global.",
                            font_size=Size.EXTRA_DEFAULT.value,
                            margin_top=Size.SMALL.value,
                            class_name="w-[50%] text-center"
                        ),
                        class_name="items-center w-full"
                    ),
                    class_name="flex w-full"
                ),
                rx.hstack(
                    universidades(
                        "utp.png",
                        constants.UTP_URL
                    ),
                    universidades(
                        "uplogo.png",
                        constants.UNIVERSIDAD_URL
                    ),
                    class_name="justify-center items-center w-full",
                    margin_top=Size.MEDIUM.value,
                ),
                padding_y=Size.GIGANTIC.value,
                bg=BackgroundColor.DEFAULT.value,
            ),


        # En esta parte se espera que coloquen las estadisticas de las revistas activas, volumenes y articulos disponibles
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Catálogo de Publicaciones y Artículos Disponibles",
                        font_size=Size.EXTRA_BIG.value,
                        class_name="font-bold w-2/5 text-center"
                    ),
                    rx.text(
                        "Conoce el panorama completo de nuestro contenido académico: desde el número de revistas activas hasta los volúmenes disponibles. Aquí encontrarás un resumen detallado de la cantidad de artículos y ensayos, destacando la variedad y profundidad de los temas cubiertos en nuestra plataforma.",
                        font_size=Size.EXTRA_DEFAULT.value,
                        class_name="w-2/5 text-center",
                        margin_top=Size.SMALL.value
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="100%"
                ),
                rx.hstack(
                    rx.vstack(
                        rx.image(
                           src="trending.svg",
                            alt="Imagen de la seccion de revistas",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            Totals.journals_total,#revistas activas
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Revistas Activas",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                    rx.vstack(
                        rx.image(
                            src="trending.svg",
                            alt="Imagen de la seccion de revistas",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            Totals.volumen_total,#num total de volumenes de revistas
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Número total de volumenes de revistas",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                    rx.vstack(
                        rx.image(
                            src="trending.svg",
                            alt="Imagen de la seccion de revistas",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            Totals.arti_ess_total,#num total de articulos y ensay
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Número total de artículos y ensayos",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                    class_name="justify-center items-center w-full",
                    margin_top=Size.EXTRA_BIG.value,
                ),
                padding_y=Size.GIGANTIC.value,
                bg=f"{BackgroundColor.PATTERN_URL.value}, {BackgroundColor.GRADIENT.value}"
            ),

            # Esta es una seccion de cortina de las redes sociales 
            rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "¡Mantente al día con las últimas noticias, eventos y oportunidades académicas! Sigue las redes sociales oficiales de nuestra universidad y de la vicerrectoría de asuntos académicos. Encontrarás información valiosa sobre programas, investigaciones, becas y mucho más. Búscanos en Facebook, X , Instagram y otras plataformas populares. ¡Conéctate con nosotros y forma parte de una comunidad académica vibrante!",
                        font_size=Size.EXTRA_DEFAULT.value,
                        margin_top=Size.SMALL.value,
                        class_name="w-[50%] text-center"
                    ),
                    class_name="items-center w-full"
                ),
                class_name="flex w-full"
            ),
            rx.hstack(
                redes(
                    "youtube.svg",
                    constants.UTP_URL
                ),
                redes(
                    "instagram.svg",
                    constants.UNIVERSIDAD_URL
                ),
                redes(
                    "twitter.svg",
                    constants.UNIVERSIDAD_URL
                ),
                redes(
                    "facebook.svg",
                    constants.UNIVERSIDAD_URL
                ),
                class_name="justify-center items-center w-full",
                margin_top=Size.MEDIUM.value,
            ),
            padding_y=Size.GIGANTIC.value,
            bg=BackgroundColor.DEFAULT.value,
        ),

        # Esta en la tercer seccion de estadisticas donde ira el numero total de descargas, descargas por dia, descargas menusales
         rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Actividad de Descargas y Publicaciones Populares",
                        font_size=Size.EXTRA_BIG.value,
                        class_name="font-bold w-2/5 text-center"
                    ),
                    rx.text(
                        "En esta sección, se detallan las métricas de descargas de la plataforma, destacando tanto las descargas diarias como las mensuales. Además, se identifican las revistas más populares en términos de descargas, proporcionando información clave sobre el interés de los usuarios en los contenidos ofrecidos.",
                        font_size=Size.EXTRA_DEFAULT.value,
                        class_name="w-2/5 text-center",
                        margin_top=Size.SMALL.value
                    ),
                    align_items="center",
                    width="100%"
                ),
                display="flex",
                width="100%"
                ),
                rx.hstack(
                    rx.vstack(
                        rx.image(
                            src="descargas.svg",
                            alt="Imagen de la seccion de descargas",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            Totals.downloads_total, #descargas totales
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Número total de descargas",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                    rx.vstack(
                        rx.image(
                            src="descargas.svg",
                            alt="Imagen de la seccion de descargas",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            "0",
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Número de descargas por día",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                    rx.vstack(
                        rx.image(
                            src="descargas.svg",
                            alt="Imagen de la seccion de descargas",
                            width=Size.EXTRA_BIG.value,
                            height=Size.EXTRA_BIG.value,
                        ),
                        rx.text(
                            "0",
                            font_size=Size.EXTRA_BIG.value,
                            font_weight="bold",
                        ),
                        rx.text(
                            "Número de descargas mensuales",
                            font_size=Size.EXTRA_DEFAULT.value,
                            font_weight="bold",
                        ),
                        class_name="flex items-center justify-center w-1/5 h-[350px]",
                        bg=BackgroundColor.CAJAS.value,
                        spacing=Size.BIG.value  
                    ),
                        class_name="justify-center items-center w-full",
                        margin_top=Size.EXTRA_BIG.value,
                    ),
                    padding_y=Size.GIGANTIC.value,
                    bg=f"{BackgroundColor.PATTERN_URL.value}, {BackgroundColor.GRADIENT.value}"
                ),

                # Solo falta el footer y el dinamismo ahora lo anado



            
    )

# se aclara que de momento solo esta el contenido de pc y no de movil, tambien que el dinamismo (movimiento de los patrones, animaciones y otros componentes) no fueron implementados el dia de hoy
