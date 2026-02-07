from fastapi import FastAPI
from app.routers import health, users, courts

app = FastAPI(
    title="Sistema de Reservas de Canchas Deportivas API",
    description="API para gestionar reservas de canchas deportivas",
    version="1.0.0"
)

# Registrar routers
app.include_router(health.router)
app.include_router(users.router)
app.include_router(courts.router)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la API de Reservas de Canchas Deportivas",
        "docs": "Visita /docs para la documentación interactiva"
    }