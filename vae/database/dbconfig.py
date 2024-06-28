from sshtunnel import SSHTunnelForwarder
from sqlalchemy.engine import URL

# Configuración de la conexión SSH "eliminar esto en caso de ejecutar en local XD"
SSH_HOST = '10.0.1.235'
SSH_USER = 'edgar.perez'
SSH_PASSWORD = 'eperez2022'

# Configuración de la conexión MySQL
MYSQL_HOST = 'localhost'
MYSQL_USER = 'ojs'
MYSQL_PASSWORD = 'prueba123'
MYSQL_DB = 'ojs'
MYSQL_PORT = 3306

# Configuración de la conexión MySQL
try:
    # Configura el túnel SSH
    tunnel = SSHTunnelForwarder(
        (SSH_HOST, 22),
        ssh_username=SSH_USER,
        ssh_password=SSH_PASSWORD,
        remote_bind_address=(MYSQL_HOST, MYSQL_PORT)
    )
    tunnel.start()
    
    # Obtiene el puerto local del túnel
    local_port = tunnel.local_bind_port

    # Configura la URL de conexión a MySQL
    url_object = URL.create(
        "mysql+pymysql",
        username=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host="127.0.0.1",
        port=local_port,
        database=MYSQL_DB,
    )

except (Exception) as e:
    print(f"Error al establecer la conexión: {e}")
    if 'tunnel' in locals():
        tunnel.stop()
    raise e
