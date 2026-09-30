# profile
from fastapi import APIRouter, Request, status, Header
from fastapi.responses import Response, JSONResponse
from app.models.profileModel import profileModel, dpSchema, profileUpdateModel
from app.db.userDb import (
    validateUser,
    create_profile_db,
    update_profile_db,
    delete_profile_db,
    update_dp_db,
    read_profile_db,
)
from typing import Annotated
from app.db.otpDb import validateOtp

router = APIRouter(prefix="/profile", tags=["Profile"])


# create
@router.post("/create")
def create_profile(
    body: profileModel, Authorization: Annotated[str | None, Header()] = None
):
    print(Authorization)
    body = body.dict()

    if not validateUser(phone=body["phone"], token=Authorization):
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    print(body)

    res = create_profile_db(body)
    print(res)

    if not res:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(res)


# update
@router.put("/update")
def update_profile(
    body: profileUpdateModel, Authorization: Annotated[str | None, Header()] = None
):

    if not validateUser(phone=body["phone"], token=Authorization):
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    body = body.dict(exclude_none=True, exclude_unset=True)

    res = update_profile_db(body)

    if not res:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(res)


# delete
@router.delete("/delete")
def delete_profile(phone: str, otp: str):

    if validateOtp(otp=otp, phone_no=phone) == False:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    res = delete_profile_db(phone)

    if not res:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(res, status_code=status.HTTP_204_NO_CONTENT)


# dp update
@router.put("/dp")
def update_dp(
    body: dpSchema, phone: str, Authorization: Annotated[str | None, Header()] = None
):
    if not validateUser(phone=phone, token=Authorization):
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    body = body.dict()

    res = update_dp_db(body, phone)

    if not res:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(res)


@router.get("/")
def get_profile(phone: str | None = None):

    res = read_profile_db(phone)

    if not res:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(res)
    # return "ok"
