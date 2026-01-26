# Proyecto-API-REST---Sistema-de-Reservas-de-Canchas-Deportivas-1
API REST para gestionar reservas de canchas deportivas (fútbol, tenis, básquet). Permite a los usuarios ver disponibilidad, reservar canchas y administrar sus reservas. Resuelve el problema de la desorganización en la reserva de espacios deportivos.

Usuario objetivo: Personas que practican deportes regularmente y necesitan reservar canchas.

Recursos principales:

Canchas (courts)

Reservas (bookings)

Usuarios (users)

Horarios (schedules)

🎯 Alcance (MVP)
Recursos y operaciones planeadas:
Canchas (/courts)

GET /courts - Listar todas las canchas disponibles

GET /courts/{id} - Obtener detalles de una cancha

GET /courts/{id}/availability - Ver disponibilidad por fecha

Reservas (/bookings)

POST /bookings - Crear nueva reserva

GET /bookings - Listar mis reservas

PUT /bookings/{id}/cancel - Cancelar reserva

GET /bookings/upcoming - Ver próximas reservas

Usuarios (/users)

POST /users/register - Registrarse

POST /users/login - Iniciar sesión

GET /users/profile - Ver mi perfil

📋 Reglas de Negocio
No se puede reservar una cancha ya reservada - Validación de solapamiento de horarios

Reserva mínima de 1 hora, máxima de 3 horas - Límites de tiempo

Cancelación con al menos 24 horas de anticipación - No se puede cancelar el mismo día

Máximo 2 reservas activas por usuario - Evitar acaparamiento

No se puede reservar en el pasado - Solo fechas futuras

<img width="452" height="455" alt="image" src="https://github.com/user-attachments/assets/4217b4fd-504d-4e91-a177-e829f54a4866" />


🛠 Tecnologías Elegidas
Framework Principal: FastAPI
Justificación: Seleccioné FastAPI por su simplicidad, alto rendimiento y documentación automática. Perfecto para APIs REST modernas donde la claridad y velocidad de desarrollo son importantes.

Stack Tecnológico:
Lenguaje: Python 3.9+

Framework Web: FastAPI

Base de Datos: SQLite (desarrollo) / PostgreSQL (producción)

ORM: SQLAlchemy

_______________________________________________________________________________________________________________________________________________________________________________________________________________
Responsabilidades de Cada Módulo
main.py - Coordinador Principal

Inicializa la aplicación FastAPI

Configura metadatos (título, descripción, versión)

Registra y monta todos los routers

Define middleware y configuraciones globales

routers/ - Gestor de Rutas HTTP

Define los endpoints disponibles

Especifica métodos HTTP (GET, POST, PUT, DELETE)

Valida parámetros de ruta y query

Maneja códigos de estado HTTP

Responsabilidad única: Enrutamiento HTTP

controllers/ - Ejecutor de Lógica de Negocio

Contiene la lógica de procesamiento

Manipula datos (CRUD operations)

Aplica reglas de negocio

Prepara respuestas para los routers

Responsabilidad única: Procesamiento de datos

models/ - Definidor de Estructuras

Define esquemas de datos con Pydantic

Valida tipos y formatos de datos

Documenta la estructura de entrada/salida

Responsabilidad única: Definición de datos

🔄 ¿Por Qué Separar Rutas y Controladores?
Principio de Responsabilidad Única (SRP):

Routers: Solo saben sobre HTTP (rutas, métodos, códigos de estado)

Controladores: Solo saben sobre lógica de negocio (datos, reglas, procesamiento)

Beneficios:

✅ Mantenibilidad: Cambios en rutas no afectan lógica de negocio

✅ Testabilidad: Controladores se pueden testear sin HTTP

✅ Reusabilidad: Lógica se puede usar en diferentes contextos

✅ Claridad: Código más fácil de entender y depurar

Autenticación: JWT (JSON Web Tokens)

Paso a Paso Técnico
🛠️ 1. Creación de la Estructura Base
# Crear directorios principales
mkdir -p app/routers app/controllers app/models

# Inicializar paquetes Python
touch app/__init__.py
touch app/routers/__init__.py
touch app/controllers/__init__.py
touch app/models/__init__.py

🛣️ 2. Creación de un Router
Archivo: app/routers/users.py
from fastapi import APIRouter, HTTPException
from app.controllers import user_controller
from app.models.schemas import UserCreate, UserResponse

# Crear router con prefijo y tags para documentación
router = APIRouter(prefix="/users", tags=["users"])

# Definir endpoint GET /users
@router.get("/", response_model=list[UserResponse])
def get_users():
    """Obtiene todos los usuarios registrados"""
    return user_controller.get_all_users()

# Definir endpoint POST /users
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    """Crea un nuevo usuario"""
    return user_controller.create_user(user)

⚙️ 3. Creación de un Controlador
Archivo: app/controllers/user_controller.py
from app.models.schemas import UserCreate, UserResponse

# Datos mock (temporal - será reemplazado por base de datos)
users_db = []

def get_all_users():
    """Obtiene todos los usuarios"""
    return users_db

def create_user(user_data: UserCreate):
    """Crea un nuevo usuario con validación automática"""
    # Generar ID único
    user_id = len(users_db) + 1
    
    # Crear respuesta con datos validados
    user_response = UserResponse(
        id=user_id,
        **user_data.dict()
    )
    
    # Almacenar en "base de datos" temporal
    users_db.append(user_response.dict())
    
    return user_response

    📦 4. Creación de Modelos (Esquemas)
Archivo: app/models/schemas.py
from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., pattern=r'^\+569\d{8}$')
    role: UserRole = UserRole.USER

class UserResponse(UserCreate):
    id: int

    🔗 5. Registro de Routers en la Aplicación Principal
Archivo: app/main.py
from fastapi import FastAPI
from app.routers import health, users, courts

# Crear aplicación FastAPI
app = FastAPI(
    title="Sistema de Reservas de Canchas Deportivas API",
    description="API para gestionar reservas de canchas deportivas",
    version="1.0.0"
)

# Registrar todos los routers
app.include_router(health.router)
app.include_router(users.router)
app.include_router(courts.router)

# Ruta raíz
@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la API de Reservas de Canchas Deportivas",
        "docs": "Visita /docs para documentación interactiva"
    }

    📤 6. Exportación de Módulos
Archivo: app/routers/__init__.py
from .health import router as health_router
from .users import router as users_router
from .courts import router as courts_router

__all__ = ["health_router", "users_router", "courts_router"]

Archivo: app/controllers/__init__.py
from .health_controller import get_health_status
from .user_controller import get_all_users, create_user
from .court_controller import get_all_courts, create_court

__all__ = [
    "get_health_status",
    "get_all_users",
    "create_user",
    "get_all_courts",
    "create_court"
]

🔌 Endpoints
🩺 Health Check
Método: GET

Ruta: /health

Descripción: Verifica el estado del servicio

Respuesta JSON:
{
  "status": "healthy",
  "timestamp": "2024-03-20T15:30:45.123456Z",
  "service": "reservas-api",
  "version": "1.0.0"
}


👥 Usuarios
Listar Usuarios
Método: GET

Ruta: /users

Descripción: Obtiene todos los usuarios registrados

Respuesta JSON:
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "+56912345678",
    "role": "user"
  }
]

Crear Usuario
Método: POST

Ruta: /users

Descripción: Registra un nuevo usuario en el sistema

Request Body:
{
  "name": "María González",
  "email": "maria@example.com",
  "phone": "+56987654321",
  "role": "user"
}

⚽ Canchas
Listar Canchas
Método: GET

Ruta: /courts

Descripción: Obtiene todas las canchas disponibles

Respuesta JSON:
[
  {
    "id": 1,
    "name": "Cancha de Fútbol 1",
    "sport_type": "futbol",
    "location": "Zona Norte",
    "price_per_hour": 15000,
    "is_available": true,
    "description": "Cancha de fútbol 11 con césped sintético"
  }
]

Obtener Cancha por ID
Método: GET

Ruta: /courts/{court_id}

Descripción: Obtiene los detalles de una cancha específica

Parámetros Ruta:

court_id (integer): ID de la cancha

Códigos de Estado:

200 OK: Cancha encontrada

404 Not Found: Cancha no existe

Respuesta JSON:
{
  "id": 1,
  "name": "Cancha de Fútbol 1",
  "sport_type": "futbol",
  "location": "Zona Norte",
  "price_per_hour": 15000,
  "is_available": true,
  "description": "Cancha de fútbol 11 con césped sintético"
}

🧪 Cómo Probar los Endpoints
🚀 1. Levantar el Servidor
Opción A: Desarrollo con Recarga Automática
# Navegar al directorio del proyecto
cd Proyecto-API-REST-Sistema-de-Reservas-de-Canchas-Deportivas

# Activar entorno virtual
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Navegar a la carpeta app y ejecutar
cd app
uvicorn main:app --reload
