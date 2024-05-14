from sqlalchemy import Column, String, Float, BigInteger, Integer
from sqlalchemy.orm import sessionmaker ,declarative_base
from engine import engine

# Definir la sesión y la base
Session = sessionmaker(bind=engine) # Crear la sesión  # noqa: F811
session = Session() # Crear la sesión
Base    = declarative_base() # Crear la base
# Modelo de la tabla journal
class Journals(Base):
    __tablename__ = 'journals' # Nombre de la tabla

    journal_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False) # Columna journal_id
    path = Column(String(32), nullable=False) # Columna path
    seq = Column(Float, nullable=False) # Columna seq
    primary_locale = Column(String(14), nullable=False) # Columna primary_locale
    enabled = Column(Integer, nullable=False) # Columna enabled

    def __repr__(self):
        return f"<journal_id=(id={self.journal_id}, path='{self.path}', seq='{self.seq}',primary_locale='{self.primary_locale}',enabled='{self.enabled}'))>" # Representación de la tabla
 
def consultar_tabla():
    with Session() as session:
        try:
            registros = session.query(Journals).all()
            for registro in registros:
                print(registro.path)  # Imprime solo la columna path
            return None
        except Exception as e:
            print(f"ocurrio un error inesperado: {e}")
            return None
        finally:
            session.close()
            
consultar_tabla()
            

