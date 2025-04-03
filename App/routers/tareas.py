from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.dataBase.dataBase import get_db
from App.dataBase import models
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


# @router.get("/bienvenida")
# def obtener_tareas():
#     return {"mensaje": "Lista de tareas"}

@router.get("/")
def obtener_tareas(db:Session = Depends(get_db)):
    data = db.query(models.Tarea).all()
    return data

@router.get("/{tarea_id}")
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not tarea:
        return {"error": "Tarea no encontrada"}
    return tarea

class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    prioridad: models.PrioridadEnum
    estado: models.EstadoEnum

@router.post("/")
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    nueva_tarea = models.Tarea(
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        prioridad=tarea.prioridad,
        estado=tarea.estado
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea


@router.delete("/{tarea_id}")
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(tarea)
    db.commit()
    return {"mensaje": "Tarea eliminada correctamente"}

@router.put("/{tarea_id}")
def actualizar_tarea(tarea_id: int, tarea_actualizada: TareaCreate, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tarea.titulo = tarea_actualizada.titulo
    tarea.descripcion = tarea_actualizada.descripcion
    tarea.prioridad = tarea_actualizada.prioridad
    tarea.estado = tarea_actualizada.estado

    db.commit()
    db.refresh(tarea)
    return tarea
