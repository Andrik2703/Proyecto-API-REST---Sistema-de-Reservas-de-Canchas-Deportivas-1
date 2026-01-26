from app.models.schemas import CourtCreate, CourtResponse

# Datos mock temporales
courts_db = [
    {
        "id": 1,
        "name": "Cancha de Fútbol 1",
        "sport_type": "futbol",
        "location": "Zona Norte",
        "price_per_hour": 15000,
        "is_available": True,
        "description": "Cancha de fútbol 11 con césped sintético"
    },
    {
        "id": 2,
        "name": "Cancha de Tenis 1",
        "sport_type": "tenis",
        "location": "Zona Sur",
        "price_per_hour": 8000,
        "is_available": True,
        "description": "Cancha de tenis con superficie dura"
    }
]

def get_all_courts():
    """Obtiene todas las canchas"""
    return courts_db

def get_court_by_id(court_id: int):
    """Obtiene una cancha por ID"""
    for court in courts_db:
        if court["id"] == court_id:
            return court
    return None

def create_court(court_data: CourtCreate):
    """Crea una nueva cancha"""
    court_id = len(courts_db) + 1
    court_response = CourtResponse(
        id=court_id,
        **court_data.dict()
    )
    courts_db.append(court_response.dict())
    return court_response