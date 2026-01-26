from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    MANAGER = "manager"

class SportType(str, Enum):
    FUTBOL = "futbol"
    TENIS = "tenis"
    BASKETBALL = "basketball"
    VOLLEYBALL = "volleyball"
    PADDLE = "paddle"

# Esquemas para Usuarios
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., pattern=r'^\+569\d{8}$')
    role: UserRole = UserRole.USER

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Canchas
class CourtBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    sport_type: SportType
    location: str
    price_per_hour: int = Field(..., gt=0)
    description: Optional[str] = Field(None, max_length=500)
    is_available: bool = True

class CourtCreate(CourtBase):
    pass

class CourtResponse(CourtBase):
    id: int

    class Config:
        from_attributes = True