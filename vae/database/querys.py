from database.models import Statistics, Session# Importar las tablas y el Session
from typing import List


class Querys_return: # Clase para retornar los querys osea los resultados de cada una de la consultasks
    def querys():
        Querys_return.mostrar_info()      

    def mostrar_info ():
        with Session() as session:
            try:
                cont = 0
                print('Variables a usar en la estadistica\n----------------------------------')
                registro = session.query(Statistics).all()
                for i in registro:
                    cont += 1
                    print(f'{cont}. {i.name}')              
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")