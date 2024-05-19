from database.models import Journals , Issues, Session # Importar las tablas y el Session
from typing import List


class Querys_return: # Clase para retornar los querys osea los resultados de cada una de la consultasks
    total_r_journals = 0 # Variable para almacenar el total de registrosuerys_return: 
    journals_r_content :List[str]=[] # Lista de registros de la tabla journals
    total_r_issues = 0 # Variable para almacenar el total de registros
    issues_r_content :List[str]=[] # Lista de registros de la tabla issues
    
    def querys():
        Querys_return.total_registros_journal() #Llamamos a la función total_registros
        Querys_return.journals_Content() #Llamamos a la función journal_Content
        Querys_return.total_registros_issues() #Llamamos a la función total_registros_issues
        Querys_return.issues_Content() #Llamamos a la función issues_Content


    def total_registros_journal():
            with Session() as session:  # Crear la sesión
                try:#intentamos
                    total = session.query(Journals).count() #Contamos los registros
                    Querys_return.total_r_journals = total #Guardamos el total de registros
                    #! comentario con fines de depuracion
                    #print(f"Total de registros: {total}") #Imprimimos el total de registros
                except Exception as e:
                    #! comentario con fines de depuracion
                    print(f"Ocurrió un error inesperado: {e}")
                finally:
                    session.close()          
    def journals_Content(): # Función para consultar la tabla joural y retornar su contenido
        #while True:  # Bucle infinito
            with Session() as session:  # Crear la sesión
                try:  # Intentar
                    registros = session.query(Journals).all()  # Consultar todos los registros
                    for registro in registros:  # Recorrer los registros
                        #print(registro.path)  # Imprime solo la columna path
                        Querys_return.journals_r_content.append(registro.path)  # Añadir la columna path a la lista
                    #break  # Salir del bucle si todo va bien
                except Exception as e:  # Excepción
                    #! comentario con fines de depuracion
                    print(f"Ocurrió un error inesperado: {e}")  # Imprime el error
                    # Aquí no hacemos break para que el bucle vuelva a intentar la operación
                #? Creo que este finally esta de mas debido al que metodo with siempre cierra la sesion XD
                finally:  # Finalmente
                    session.close()  # Cerrar la sesión
                    #! comentario con fines de depuracion
                    print("Sesión cerrada, se completó el proceso")  # Imprime "Sesión cerrada"


    def total_registros_issues():
            with Session() as session:
                try:
                    total = session.query(Issues).count()
                    Querys_return.total_r_issues = total
                    #! comentario con fines de depuracion
                    #print(f"Total de registros: {total}")
                except Exception as e:
                    #! comentario con fines de depuracion
                    print(f"Ocurrió un error inesperado: {e}")
                finally:
                    session.close()
    def issues_Content():
        #while True:
            with Session() as session:
                try:
                    registros = session.query(Issues).all()
                   # print(f"issue_id\tjournal_id\tdate_published")
                    for registro in registros:
                        #print(f"{registro.issue_id}\t{registro.journal_id}\t{registro.date_published}")
                        Querys_return.issues_r_content.append(registro.date_published)
                    #break
                except Exception as e:
                    #! comentario con fines de depuracion
                    print(f"Ocurrió un error inesperado: {e}")
                finally:
                    session.close()
                    #! comentario con fines de depuracion
                    print("Sesión cerrada, se completó el proceso")