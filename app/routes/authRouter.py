# auth
from fastapi import APIRouter, status
from fastapi.responses import Response, JSONResponse
from app.models.authModel import authModel
from app.db.otpDb import validateOtp
from app.db.userDb import read_user, create_user

router = APIRouter(prefix="/auth", tags=["Auth"])


# signin
@router.post("/signin")
def signin(body: authModel):
    body = body.dict()

    if validateOtp(otp=body["otp"], phone_no=body["phone"]) == False:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    res = read_user(body["phone"])
    if not res:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(res)


# signup
@router.post("/signup")
def signup(body: authModel):
    body = body.dict()
    if validateOtp(otp=body["otp"], phone_no=body["phone"]) == False:
        # if validateOtp(body["otp"]) == False:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    res = create_user(body["phone"])

    if not res:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse({"inserted_id": res})
