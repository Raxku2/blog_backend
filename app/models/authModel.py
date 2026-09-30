from pydantic import BaseModel


class authModel(BaseModel):
    phone: str
    otp: str
