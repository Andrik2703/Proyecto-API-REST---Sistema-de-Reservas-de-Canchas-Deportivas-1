from fastapi import APIRouter, HTTPException
from app.controllers import user_controller
from app.models.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserResponse])
def get_users():
    return user_controller.get_all_users()

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    return user_controller.create_user(user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = user_controller.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user