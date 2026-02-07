from fastapi import APIRouter
from app.controllers import health_controller

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check():
    return health_controller.get_health_status()