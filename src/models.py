from typing import Optional

from pydantic import BaseModel


class Order(BaseModel):
    created_time: str
    contact: str
    quantity: int
    product_code: str
    post_id: str


class Post(BaseModel):
    message: str = "Test Post"
    link: Optional[str] = (
        "https://previews.123rf.com/images/aquir/aquir1311/aquir131100316/23569861-sample-grunge"
        "-red-round-stamp.jpg?fbclid=IwAR3fTjnWRlEGOYzwabAgFK67myClisbp3GEqD5lrl6FWLjhgxre5POBJDTo"
    )
    caption: Optional[str] = "Sample"
    formatting: str = "MARKDOWN"


class Metadata(BaseModel):
    endpoint_url: str = "https://graph.facebook.com/{}/feed"
    access_token: str = (
        "EAAVKWLETDpoBOZCgagtd0CCWXmTAZB3nQD5YhpchBzdqX4s8TULF0DdDWVZB6NXICsed3na3vlJEWyo4ZBKkbSjXr3MSO7qSFavM8ZBrCUzVA8rKPOb9thcrs5Y1wGYEGfA5fhn714zpS1HUDE06LUkzVMGKZB1MDV7P77z5spFGViKkAdboCz0JUtTsdR6ZAUZD"
    )
    app_id: str = "1489119671946906"
    app_secret: str = "4be7edba6ac41485e6a573ae03dc17e4"
    page_id: str = "111806027126333"


class CreatePostRequest(BaseModel):
    payload: Post
    metadata: Metadata


class CreatPostResponse(BaseModel):
    code: str = "SUCCESS"
    message: str = "Post processed successfully"
    post_id: str | None


class GetOrdersRequest(BaseModel):
    endpoint_url: str = "https://graph.facebook.com/{}/comments"
    access_token: str = (
        "EAAVKWLETDpoBOZCgagtd0CCWXmTAZB3nQD5YhpchBzdqX4s8TULF0DdDWVZB6NXICsed3na3vlJEWyo4ZBKkbSjXr3MSO7qSFavM8ZBrCUzVA8rKPOb9thcrs5Y1wGYEGfA5fhn714zpS1HUDE06LUkzVMGKZB1MDV7P77z5spFGViKkAdboCz0JUtTsdR6ZAUZD"
    )
    post_id: str
