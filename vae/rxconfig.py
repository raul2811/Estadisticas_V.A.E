import reflex as rx
from dbconfig import MYSQL_HOST,MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
# Configuración de la conexión MySQL

config = rx.Config(
    app_name="vae",
    db_url=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}",
)