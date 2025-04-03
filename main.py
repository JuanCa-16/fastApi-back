from fastapi import FastAPI
from App.dataBase.dataBase import engine, Base
from App.routers.tareas import router as tareas_router  # Importa el router de tareas

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

# uvicorn main:app --reload
