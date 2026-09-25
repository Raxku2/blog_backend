from fastapi import APIRouter

router = APIRouter(prefix="/imagekit", tags=["Imagekit"])


@router.get("/token")
def create_imagekit_auth():
    return "ok"
