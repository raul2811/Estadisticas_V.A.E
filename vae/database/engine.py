from sqlalchemy import create_engine
from database.dbconfig import url_object

engine = create_engine(url_object,)# echo=True se agrega para ver las consultas SQL que se ejecutan

