from sqlalchemy.engine import URL

# Configuración de la conexión MySQL

url_object = URL.create(
    "mysql+pymysql",
    username="ojs",  
    password="prueba123",
    host="localhost",
    database="ojs",
)