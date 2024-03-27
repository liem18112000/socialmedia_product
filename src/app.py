from typing import Annotated

import uvicorn
from fastapi import FastAPI, HTTPException, Path

from src.models import CreatPostResponse, CreatePostRequest, GetOrdersRequest
from src.services import get_post_orders_by_id, send_post

app = FastAPI(
    title="LocalFoody SocialMedia Integration",
    root_path="/api/v1",
)


@app.get("/")
def health_check():
    return {
        "service": "LocalFoody SocialMedia Integration",
        "version": "0.0.1",
        "maintainers": ["Pham Ngoc Thanh" "Doan Van Thanh Liem"],
    }


@app.post(path="/posts", status_code=201)
async def create_post(request_body: CreatePostRequest):
    post_id = send_post(request_body)
    if post_id is None:
        raise HTTPException(status_code=400, detail="Post processed failed")
    return CreatPostResponse(post_id=post_id)


@app.post(path="/orders", status_code=200)
async def get_order(request_body: GetOrdersRequest):
    return get_post_orders_by_id(request_body)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
