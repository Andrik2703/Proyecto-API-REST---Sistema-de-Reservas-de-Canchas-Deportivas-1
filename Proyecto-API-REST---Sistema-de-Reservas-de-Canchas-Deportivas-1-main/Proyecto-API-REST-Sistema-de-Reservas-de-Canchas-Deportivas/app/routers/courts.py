from fastapi import APIRouter, HTTPException
from app.controllers import court_controller
from app.models.schemas import CourtCreate, CourtResponse

router = APIRouter(prefix="/courts", tags=["courts"])

@router.get("/", response_model=list[CourtResponse])
def get_courts():
    return court_controller.get_all_courts()

@router.get("/{court_id}", response_model=CourtResponse)
def get_court(court_id: int):
    court = court_controller.get_court_by_id(court_id)
    if not court:
        raise HTTPException(status_code=404, detail="Cancha no encontrada")
    return court

@router.post("/", response_model=CourtResponse, status_code=201)
def create_court(court: CourtCreate):
    return court_controller.create_court(court)