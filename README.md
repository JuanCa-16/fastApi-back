# 🚀 API REST de Tareas - FastAPI ⚙️🐍

Este repositorio contiene el backend de una **API RESTful** desarrollada con **FastAPI**. Permite la gestión completa de tareas: crear, leer, actualizar y eliminar (CRUD).  
La aplicación se conecta a una base de datos **PostgreSQL** desplegada en **Railway**.

---

## ☁️ Despliegue en la Nube

- 🔗 **Documentación Swagger**: [`https://fastapi-back-production.up.railway.app/docs`](https://fastapi-back-production.up.railway.app/docs)  
- 🔗 **Repositorio GitHub**: [`https://github.com/JuanCa-16/fastApi-back`](https://github.com/JuanCa-16/fastApi-back)

---

## 🛠 Instalación y Ejecución Local

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/JuanCa-16/fastApi-back.git
cd fastApi-back
```

### 2️⃣ Crear un Entorno Virtual y Activarlo

**🪟 Windows:**

```bash
python -m venv env
env\Scripts\activate
```

**🍏 Linux/macOS:**

```bash
python -m venv env
source env/bin/activate
```

### 3️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con la siguiente variable:

```env
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_bd
```

⚠️ **Reemplaza** con tu string real de conexión a PostgreSQL.  
Si usas Railway, obtén esta URL desde el panel del proyecto.

### 5️⃣ Ejecutar el Servidor

```bash
uvicorn main:app --reload
```

📍 Por defecto, la API estará disponible en [`http://127.0.0.1:8000`](http://127.0.0.1:8000)

---

## 📌 Endpoints Disponibles

| Método   | Ruta             | Descripción                            |
|----------|------------------|----------------------------------------|
| `GET`    | `/tareas/`       | Obtener lista de tareas                |
| `GET`    | `/tareas/{id}`   | Obtener detalle de una tarea           |
| `POST`   | `/tareas/`       | Crear nueva tarea                      |
| `PUT`    | `/tareas/{id}`   | Actualizar una tarea existente         |
| `DELETE` | `/tareas/{id}`   | Eliminar una tarea por ID              |

✅ Puedes probar estos endpoints directamente desde la documentación **Swagger**.

---

## 🗃️ Estructura de la Tabla `tareas` en PostgreSQL

| Campo       | Tipo                      | Restricciones                     | Descripción                         |
|-------------|---------------------------|-----------------------------------|-------------------------------------|
| `id`        | Integer                   | PK, autoincremental               | Identificador único de la tarea     |
| `titulo`    | String(255)               | NOT NULL                          | Título descriptivo de la tarea      |
| `descripcion` | String                  | Opcional                          | Detalles adicionales                |
| `prioridad` | Enum: `PrioridadEnum`     | NOT NULL                          | Nivel de prioridad de la tarea      |
| `estado`    | Enum: `EstadoEnum`        | NOT NULL                          | Estado actual de la tarea           |

---

### 🎯 Tipos Aceptados por los ENUMs

**`PrioridadEnum`**:
- urgente
- alta
- normal

**`EstadoEnum`**:
- pendiente
- trabajando
- completada

Estos valores son almacenados como tipos **ENUM de PostgreSQL** mediante SQLAlchemy.

---

## 🧑‍💻 Autor

**Juan Camilo Henao Gallego**  
Estudiante de Ingeniería de Sistemas - Universidad del Valle  

📚 Proyecto desarrollado para el curso:  
**Aplicaciones en la Web y Redes Inalámbricas**
