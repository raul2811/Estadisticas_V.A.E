from multiprocessing import context
import re
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
    submission_id = Column(BigInteger,primary_key=True, nullable=False)
    total_metric = Column(Float, nullable=False)

    def __repr__(self):
        return f"<submission_id=(submission_id={self.submission_id}, total='{self.total_metric}'))>" # Representación de la tabla

class Context_Downloads(Base):
    __tablename__ = 'context_downloads' # Nombre de la tabla
    context_id = Column(BigInteger, primary_key=True, nullable=False)
    total_metric = Column(Float, nullable=False)

    def __repr__(self):
        return f"<context_id=(context_id={self.context_id}, total='{self.total_metric}'))>" # Representación de la tabla

class Month_Downloads(Base):
    __tablename__ = 'month_downloads' # Nombre de la tabla
    month = Column(BigInteger,primary_key=True, nullable=False)
    total_metric = Column(Float, nullable=False)

    def __repr__(self):
        return f"<month=(month={self.month}, total='{self.total_metric}'))>" # Representación de la tabla

class Submission_downloads_top (Base):
    __tablename__ = 'submission_downloads_top' # Nombre de la tabla
    submission_id = Column(BigInteger,primary_key=True, nullable=False)
    context_id = Column(BigInteger, nullable=False)
    path = Column(String(32), nullable=False)
    publication_id = Column(BigInteger, nullable=False)
    cleantitle = Column(String(32), nullable=False)
    issueid = Column(Integer, nullable=False)
    total_metric = Column(Float, nullable=False)

    def __repr__(self):
        return f"<submission_id=(submission_id={self.submission_id}, context_id='{self.context_id}', path='{self.path}', publication_id='{self.publication_id}', cleantitle='{self.cleantitle}', issueid='{self.issueid}', total_metric='{self.total_metric}'))>" # Representación de la tabla

class Submissions_recents (Base):
    __tablename__ = 'submissions_recents'
    publication_id = Column (BigInteger, primary_key=True, nullable=False)
    date_published = Column (BigInteger, nullable=False)
    title = Column(String, nullable=False)
    issue_id = Column(BigInteger, nullable=False)
    journal_id = Column(BigInteger, nullable=False)

    def __repr__(self):
            return f"<publication_id=(publication_id={self.publication_id}, date_published='{self.date_published}', title='{self.title}', issue_id='{self.issue_id}', journal_id='{self.journal_id}'))>" # Representación de la tabla