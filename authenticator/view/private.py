from fastapi import APIRouter, Depends

from authenticator.authentication.auth import get_user

router = APIRouter(prefix="/private")

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return "Inside private window"
