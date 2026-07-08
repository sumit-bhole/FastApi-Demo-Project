from pydantic import BaseModel, AnyUrl, Field
from typing import Dict, List, Annotated

# class Post(BaseModel):
#     title: str = Field(
#         min_length=10,
#         max_length=30,
#         title="Title of your post",
#     )
#     desc: str = Field(min_length=15, max_length=100, title="Description of the post")
#     img_url: AnyUrl


class PostCreate(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    title: str
    content: str
