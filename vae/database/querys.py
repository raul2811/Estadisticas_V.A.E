from database.models import Statistics, Submission_downloads_top,Submissions_recents, Session# Importar las tablas y el Session
from typing import List


class Querys_return: # Clase para retornar los querys osea los resultados de cada una de la consultasks
    ''' #motivo de depuracion
    def querys():
        Querys_return.mostrar_colum_variables()
    
    def mostrar_colum_variables ():
        with Session() as session:
            try:
                cont = 0
                print('Variables a usar en la estadistica\n----------------------------------')
                registro = session.query(Statistics).all()
                for i in registro:
                    cont += 1
                    registro= session.query(Statistics).filter(Statistics.name == i.name).first()
                    print(f'{cont}. {i.name} . {registro.total}')
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
    '''
    def mostrar_statistics (name):# Mostrar el total de la estadistica ingresando una variable name para retornar el valor de la columna total.
        with Session() as session:
            try:
               registro= session.query(Statistics).filter(Statistics.name == name).first()
               return registro.total
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")

    def mostrar_submission_download_top(num, name):
        with Session() as session:
            try:
                # Consultar todos los registros
                registro = session.query(Submission_downloads_top).all()
                
                # Convertir registros en una lista de diccionarios
                data = []
                for i in registro:
                    data.append({
                        "context_id": i.context_id,
                        "submission_id": i.submission_id,
                        "path": i.path,
                        "publication_id": i.publication_id,
                        "clean_title": i.cleantitle,  # Asegúrate de que 'clean_title' sea el nombre correcto
                        "issue_id": i.issueid,  # Asegúrate de que 'issue_id' sea el nombre correcto
                        "total_metric": i.total_metric
                    })

                # Verificar si el índice 'num' está dentro de los límites
                if num >= len(data) or num < 0:
                    raise IndexError("El índice 'num' está fuera del rango de los datos disponibles.")
                
                # Verificar si 'name' es una clave válida en el diccionario
                if name not in data[num]:
                    raise KeyError(f"La clave '{name}' no existe en los datos.")

                return data[num][name]
            
            except (IndexError, KeyError) as e:
                # Captura errores específicos para índices fuera de rango y claves inválidas
                print(f"Error de acceso a datos: {e}")
                return None
            except Exception as e:
                # Captura cualquier otro tipo de error
                print(f"Ocurrió un error inesperado: {e}")
                return None

    def mostrar_submission_recents (num, name):
        with Session() as session:
            try:
                registro = session.query(Submissions_recents).all()
                data = []
                for i in registro:
                    data.append({
                        "publication_id": i.publication_id,
                        "date_published": i.date_published,
                        "title": i.title,
                        "issue_id": i.issue_id,
                        "journal_id": i.journal_id
                    })
                # Verificar si el índice 'num' está dentro de los límites
                if num >= len(data) or num < 0:
                    raise IndexError("El índice 'num' está fuera del rango de los datos disponibles.")
                
                # Verificar si 'name' es una clave válida en el diccionario
                if name not in data[num]:
                    raise KeyError(f"La clave '{name}' no existe en los datos.")
                
                return data [num][name] # Retorna la lista de diccionarios
                
            except (IndexError, KeyError) as e:
                # Captura errores específicos para índices fuera de rango y claves inválidas
                print(f"Error de acceso a datos: {e}")
                return None
            except Exception as e:
                # Captura cualquier otro tipo de error
                print(f"Ocurrió un error inesperado: {e}")
                return None