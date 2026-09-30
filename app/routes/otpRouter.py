from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from secrets import choice
from requests import get
from app.db.otpDb import saveOtp, validateOtp

from dotenv import load_dotenv
from os import getenv


load_dotenv()

router = APIRouter(prefix="/otp", tags=["OTP Routes"])


@router.get("/request/{phone_no}")
def request_new_otp(phone_no: str):
    otp = ""

    for a in range(6):
        otp += choice("0123456789")

    # res = get(
    #     "https://www.fast2sms.com/dev/whatsapp",
    #     headers={"Authorization": getenv("F2S_API_KEY")},
    #     params={
    #         "message_id": "34621",
    #         "phone_number_id": "1311520745373044",
    #         "numbers": phone_no,
    #         "variables_values": f"{otp}|{otp}",
    #     },
    # )

    # if res.status_code != 200:
    #     return JSONResponse({}, status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    res = saveOtp(phone_no=phone_no, otp=otp)

    if res == False:
        return JSONResponse({}, status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    return JSONResponse({"message": "otp sent at your whatsapp"})


@router.post("/validate")
def request_new_otp(phone_no: str, otp: str):

    res = validateOtp(phone_no=phone_no, otp=otp)

    if res == False:
        return JSONResponse({}, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse({"message": "OTP matched"})
