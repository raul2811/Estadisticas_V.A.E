from database.models import Journals ,Session # Importar la tabla Journals
from typing import List

class Consultar: # Clase para consultar la tabla
     registro_lista :List[str]=[] # Lista de registros

def consultar_tabla(): # Función para consultar la tabla
        with Session() as session: # Crear la sesión
            try: # Intentar
                registros = session.query(Journals).all() # Consultar todos los registros
                for registro in registros: # Recorrer los registros
                    print(registro.path)  # Imprime solo la columna path
                    Consultar.registro_lista.append(registro.path) # Añadir la columna path a la lista
                return None # Retorna la columna path
            except Exception as e: # Excepción
                print(f"ocurrio un error inesperado: {e}") # Imprime el error
                return None  # Retorna None
            finally: # Finalmente
                session.close() # Cerrar la sesión

