from App.dataBase.dataBase import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM  # IMPORTANTE para usar los ENUMs de PostgreSQL
import enum

# Definir el ENUM para prioridad
class PrioridadEnum(str, enum.Enum):
    urgente = "urgente"
    alta = "alta"
    normal = "normal"

# Definir el ENUM para estado
class EstadoEnum(str, enum.Enum):
    pendiente = "pendiente"
    trabajando = "trabajando"
    completada = "completada"

# Modelo de la tabla TAREAS
class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(String)
    prioridad = Column(ENUM(PrioridadEnum, name="prioridad_tarea", create_type=False), nullable=False)  # IMPORTANTE
    estado = Column(ENUM(EstadoEnum, name="estado_tarea", create_type=False), nullable=False)  # IMPORTANTE
