# auth
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


# signin
@router.post("/signin")
def signin():
    return "ok"


# signup
@router.post("/signup")
def signin():
    return "ok"
