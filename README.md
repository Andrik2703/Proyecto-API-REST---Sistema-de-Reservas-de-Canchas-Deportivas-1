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

Autenticación: JWT (JSON Web Tokens)

Validación: Pydantic
