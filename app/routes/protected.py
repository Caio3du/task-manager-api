from fastapi import APIRouter, Depends
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api", tags=["Protected"])

@router.get("/protected")
def protected_route(current_user: User = Depends(get_current_user)):
    return {
        "message": "You are authenticated!",
        "user": current_user.email
    }