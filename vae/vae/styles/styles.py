import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import BackgroundColor, TextColor

class Size(Enum):
    SMALL = "0.5em"
    EXTRA_SMALL = "0.25em"
    DEFAULT = "1em"
    EXTRA_DEFAULT = "1.125em"
    LARGE = "1.25em"
    MEDIUM = "1.5em"
    BIG = "2em"
    EXTRA_BIG = "3em" 
    HUGE = "3.5em"
    EXTRA_HUGE = "4em"
    GIGANTIC = "5em"
    EXTRA_GIGANTIC = "6em"  
    MASSIVE = "7em"         


STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Raleway&display=swap",
    "css/animaciones.css",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background": BackgroundColor.DEFAULT.value,
    "color": TextColor.DEFAULT.value,
}