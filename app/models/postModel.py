from pydantic import BaseModel


class blog_schema(BaseModel):
    title: str
    desc: str
    blog: str
    phone: str
    username: str
