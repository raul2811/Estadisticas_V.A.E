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

class Submission_Downloads(Base):
    __tablename__ = 'submission_downloads' # Nombre de la tabla
    submission_id = Column(BigInteger, ForeignKey('submissions.id'), nullable=False)
    total_metric = Column(BigInteger, nullable=False)

    def __repr__(self):
        return f"<submission_id=(submission_id={self.submission_id}, total='{self.total_metric}'))>" # Representación de la tabla

class Context_Downloads(Base):
    __tablename__ = 'context_downloads' # Nombre de la tabla
    context_id = Column(BigInteger, ForeignKey('contexts.id'), nullable=False)
    total_metric = Column(BigInteger, nullable=False)

    def __repr__(self):
        return f"<context_id=(context_id={self.context_id}, total='{self.total_metric}'))>" # Representación de la tabla

class Month_Downloads(Base):
    __tablename__ = 'month_downloads' # Nombre de la tabla
    month = Column(BigInteger, nullable=False)
    total_metric = Column(BigInteger, nullable=False)

    def __repr__(self):
        return f"<month=(month={self.month}, total='{self.total_metric}'))>" # Representación de la tabla
    
    