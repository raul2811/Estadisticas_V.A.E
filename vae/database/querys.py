from database.models import Statistics, Session# Importar las tablas y el Session
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
    def mostrar_colum_total (name):# Mostrar el total de la estadistica ingresando una variable name para retornar el valor de la columna total.
        with Session() as session:
            try:
               registro= session.query(Statistics).filter(Statistics.name == name).first()
               return registro.total
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")