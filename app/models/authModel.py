from pydentic import BaseModel


class authModel(BaseModel):
    phone: str
    otp: str
    otp_id: str
