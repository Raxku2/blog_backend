# post
from fastapi import APIRouter
from app.models.postModel import blog_schema

router = APIRouter(prefix="/post", tags=["Blog Post"])


# create
@router.post("/blog")
def create_blog(body: blog_schema):
    return "ok"


# update
@router.patch("/blog")
def update_blog(body: blog_schema):
    return "ok"


# delete
@router.delete("/blog")
def delete_blog(user_id: str, blog_id: str):
    return "ok"


@router.get("/blog")
def get_blog(blog_id: str = None):
    return "ok"


# like
@router.post("/like")
def add_like(blog_id: str, user_id: str):
    return "ok"


# dislike
@router.delete("/like")
def remove_like(blog_id: str, user_id: str):
    return "ok"


# feed
@router.get("/feed")
def get_feed():
    return "ok"
