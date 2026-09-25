# profile
from fastapi import APIRouter
from app.models.profileModel import profileModel, dpSchema

router = APIRouter(prefix="/profile", tags=["Profile"])


# create
@router.post("/create")
def create_profile(body: profileModel):
    return "ok"


# update
@router.put("/update")
def update_profile(body: profileModel):
    return "ok"


# delete
@router.delete("/delete")
def delete_profile(user_id: str):
    return "ok"


@router.get("/profile/{phone}")
def get_profile(phone: str):
    return "ok"


# dp update
@router.put("/dp")
def update_dp(body: dpSchema):
    return "ok"
