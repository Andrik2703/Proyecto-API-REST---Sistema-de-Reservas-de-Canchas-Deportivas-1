from app.models.schemas import UserCreate, UserResponse

# Datos mock temporales (reemplazar con base de datos después)
users_db = []

def get_all_users():
    """Obtiene todos los usuarios"""
    return users_db

def get_user_by_id(user_id: int):
    """Obtiene un usuario por ID"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    return None

def create_user(user_data: UserCreate):
    """Crea un nuevo usuario"""
    user_id = len(users_db) + 1
    user_response = UserResponse(
        id=user_id,
        **user_data.dict()
    )
    users_db.append(user_response.dict())
    return user_response