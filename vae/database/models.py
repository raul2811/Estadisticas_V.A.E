from sqlalchemy import Column, String, Float, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker ,declarative_base,relationship
from database.engine import engine

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
    
    #*issues es el elemento que se relaciona con la tabla Issues , back_populates es el nombre de la relación en la tabla Issues ,journal_id_ref es el nombre de la relación en la tabla Journals
    issues = relationship("Issues",uselist=False,back_populates="journal") # Relación con la tabla issues

    def __repr__(self):
        return f"<journal_id=(id={self.journal_id}, path='{self.path}', seq='{self.seq}',primary_locale='{self.primary_locale}',enabled='{self.enabled}'))>" # Representación de la tabla


class Issues(Base):
    __tablename__ = 'issues' # Nombre de la tabla

    issue_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False) # Columna issue_id
    #*el foreign key es para relacionar la tabla Journals con la tabla Issues pero el argumento es el nombre de la tabla y el nombre de la columna
    journal_id = Column(BigInteger,ForeignKey("journals.journal_id"), nullable=False) # Columna journal_id
    volume = Column(String(6), nullable=False) # Columna volume
    number = Column(String(40), nullable=False) # Columna number
    year = Column(String(6), nullable=False) # Columna year
    current = Column(Integer, nullable=False) # Columna current
    date_published = Column(String(10), nullable=False) # Columna date_published
    date_notified = Column(String(10), nullable=False) # Columna date_noified
    last_modified = Column(String(10), nullable=False) # Columna last_modified
    access_status = Column(Integer, nullable=False) # Columna access_status
    open_access_date = Column(String(10), nullable=False) # Columna open_access_date
    show_volume = Column(Integer, nullable=False) # Columna show_volume
    show_number = Column(Integer, nullable=False) # Columna show_number
    show_year = Column(Integer, nullable=False) # Columna show_year
    show_title = Column(String(255), nullable=False) # Columna show_title
    style_file_name = Column(String(90), nullable=False) # Columna style_file_name
    original_style_file_name = Column(String(255), nullable=False) # Columna original_style_file_name
    url_path = Column(String(64), nullable=False) # Columna url_path

    #*Jounarl "variable declarativa " es el elemento que se relaciona con la tabla Journals , back_populates es el nombre de la relación en la tabla Journals ,Journal_id_ref es el nombre de la relación en la tabla Issues
    journal = relationship("Journals", back_populates="issues") # Relación con la tabla journals

    def __repr__(self):
        return f"<issue_id=(id={self.issue_id}, journal_id='{self.journal_id}', volume='{self.volume}',number='{self.number}',year='{self.year}',current='{self.current}',date_published='{self.date_published}',date_notified='{self.date_notified}',last_modified='{self.last_modified}',access_status='{self.access_status}',open_access_date='{self.open_access_date}',show_volume='{self.show_volume}',show_number='{self.show_number}',show_year='{self.show_year}',show_title='{self.show_title}',style_file_name='{self.style_file_name}',original_style_file_name='{self.original_style_file_name}',url_path='{self.url_path}'))>"

