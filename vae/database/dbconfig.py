from sqlalchemy.engine import URL

# Configuración de la conexión MySQL

url_object = URL.create(
    "mysql+pymysql",
    username="",  
    password="",
    host="localhost",
    database="",
)