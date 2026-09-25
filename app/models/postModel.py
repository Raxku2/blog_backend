from pydantic import BaseModel


class blog_schema(BaseModel):
    title: str
    blog: str
    author_id: str
    username: str
