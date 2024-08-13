from enum import Enum

class BackgroundColor(Enum):
    DEFAULT = "#FFFFFF"
    AZUL = "#031749"
    GRADIENT = "linear-gradient(to bottom, #96C2EC 0%, #E5F2FC 50%)"
    PATTERN_URL = "url('/pattern.svg')"

    
class TextColor(Enum):
    WHITE = "#FFFFFF"
    DEFAULT = "#031749"
    HOVER = "#475A72"
