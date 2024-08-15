from sqlalchemy import Column, String, Float, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker ,declarative_base,relationship
from database.engine import engine

# Definir la sesión y la base
Session = sessionmaker(bind=engine) # Crear la sesión  # noqa: F811
session = Session() # Crear la sesión
Base    = declarative_base() # Crear la base

# Modelo de la tabla Statistics
class Statistics (Base):
    __tablename__ = 'statistics' # Nombre de la tabla
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False) 
    name = Column(String(20), nullable=False) 
    total = Column(BigInteger, nullable=False) 
    updated_at = Column(BigInteger, nullable=False)
    
    def __repr__(self):
        return f"<id=(id={self.id}, name='{self.name}', total='{self.total}', updated_at='{self.updated_at}'))>" # Representación de la tabla


