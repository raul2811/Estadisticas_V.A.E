from sqlalchemy import create_engine
from dbconfig import url_object

engine = create_engine(url_object,echo=True)

