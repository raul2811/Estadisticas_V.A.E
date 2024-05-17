from database.models import Journals ,Session # Importar la tabla Journals
from typing import List

class Consultar: # Clase para consultar la tabla
     registro_lista :List[str]=[] # Lista de registros

def consultar_tabla(): # Función para consultar la tabla
        while True:  # Bucle infinito
            with Session() as session:  # Crear la sesión
                try:  # Intentar
                    registros = session.query(Journals).all()  # Consultar todos los registros
                    for registro in registros:  # Recorrer los registros
                        print(registro.path)  # Imprime solo la columna path
                        Consultar.registro_lista.append(registro.path)  # Añadir la columna path a la lista
                    break  # Salir del bucle si todo va bien
                except Exception as e:  # Excepción
                    print(f"Ocurrió un error inesperado: {e}")  # Imprime el error
                    # Aquí no hacemos break para que el bucle vuelva a intentar la operación
                #? Creo que este finally esta de mas debido al que metodo with siempre cierra la sesion XD
                finally:  # Finalmente
                    session.close()  # Cerrar la sesión
                    print("Sesión cerrada, se completó el proceso")  # Imprime "Sesión cerrada"
