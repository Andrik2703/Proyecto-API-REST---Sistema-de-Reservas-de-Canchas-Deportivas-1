from datetime import datetime

def get_health_status():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "service": "reservas-api",
        "version": "1.0.0"
    }