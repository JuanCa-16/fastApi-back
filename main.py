from fastapi import FastAPI
from App.dataBase.dataBase import engine, Base
from App.routers.tareas import router as tareas_router  # Importa el router de tareas
import uvicorn
import os
# Crear tablas en la base de datos
def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI()

# Registrar rutas
app.include_router(tareas_router, prefix="/tareas", tags=["Tareas"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Toma puerto de entorno o usa 8000 por defecto
    uvicorn.run("main:app", host="0.0.0.0", port=port)

# uvicorn main:app --reload
