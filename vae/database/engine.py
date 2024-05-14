from sqlalchemy import create_engine
from database.dbconfig import url_object

engine = create_engine(url_object)
