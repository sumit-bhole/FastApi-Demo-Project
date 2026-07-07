from fastapi import FastAPI, HTTPException
from app.schema.post import Post, PostCreate, PostResponse
from typing import Optional, List, Dict

app = FastAPI()

text_posts = {
    1: {
        "title": "Morning Motivation",
        "content": "Start your day with a positive mindset and a clear goal.",
    },
    2: {
        "title": "Python Tips",
        "content": "Use list comprehensions to write cleaner and more efficient code.",
    },
    3: {
        "title": "FastAPI Basics",
        "content": "FastAPI makes it easy to build high-performance REST APIs.",
    },
    4: {
        "title": "Healthy Living",
        "content": "Drink enough water and exercise regularly to stay healthy.",
    },
    5: {
        "title": "Travel Diary",
        "content": "Exploring new places helps you learn about different cultures.",
    },
    6: {
        "title": "Book Recommendation",
        "content": "Atomic Habits is a great book for building better daily routines.",
    },
    7: {
        "title": "Tech News",
        "content": "Artificial Intelligence continues to transform various industries.",
    },
    8: {
        "title": "Photography",
        "content": "Golden hour lighting can make your photos look stunning.",
    },
    9: {
        "title": "Music Playlist",
        "content": "Listening to relaxing music can improve your focus while working.",
    },
    10: {
        "title": "Weekend Plans",
        "content": "A short hike with friends is a perfect way to recharge.",
    },
}


@app.get("/posts")
def get_all_posts(limit: Optional[int] = None) -> Dict:
    if limit is not None:
        posts = list(text_posts.values())[:limit]
        return posts
    return text_posts


@app.get("/post/{id}")
def get_post_by_id(id: int) -> Dict:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post Not Found")
    post = text_posts.get(id)
    return post


@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    post = text_posts[max(text_posts.keys()) + 1] = {
        "title": post.title,
        "content": post.content,
    }
    return post


@app.delete("/post/{id}")
def delete_post(id: int) -> Dict:
    if id not in text_posts.keys():
        raise HTTPException(status_code=404, detail="Post Not Found")
    post = text_posts.pop(id)
    return post
