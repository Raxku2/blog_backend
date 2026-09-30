from pydantic import BaseModel


class profileModel(BaseModel):
    name: str
    role: str
    organization: str | None = None
    phone: str
    dp_id: str | None = None
    dp_url: str | None = None


class profileUpdateModel(BaseModel):
    name: str | None = None
    role: str | None = None
    organization: str | None = None
    phone: str
    dp_id: str | None = None
    dp_url: str | None = None


class dpSchema(BaseModel):
    dp_id: str
    dp_url: str
