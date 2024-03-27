import os

import requests

from src.models import Order, CreatePostRequest, GetOrdersRequest


def send_post(request_body: CreatePostRequest):
    metadata = request_body.metadata
    base_url = metadata.endpoint_url
    page_id = metadata.page_id
    access_token = metadata.access_token
    payload = request_body.payload
    post_url = base_url.format(page_id)
    data = {
        "message": payload.message,
        "link": payload.link,
        "caption": payload.caption,
        "formatting": payload.formatting,
        "access_token": access_token,
    }
    r = requests.post(post_url, data=data)
    print(f"HTTP status {r.status_code}")
    if r.status_code == 200:
        return r.json()["id"]
    return None


def convert_message_to_order(msg: str, crt_time: str, pid: str, delimiter=" "):
    if msg is None or len(msg) == 0:
        return None
    raw_sections = msg.split(delimiter)
    cleaned_sections = [s for s in raw_sections if s is not None and s.strip()]
    if len(cleaned_sections) != 3:
        return None
    return Order(
        created_time=crt_time,
        product_code=cleaned_sections[0],
        quantity=cleaned_sections[1],
        contact=cleaned_sections[2],
        post_id=pid,
    )


def get_post_orders_by_id(request_body: GetOrdersRequest):
    base_url = request_body.endpoint_url
    access_token = request_body.access_token
    post_id = request_body.post_id
    url = base_url.format(post_id)
    params = {"access_token": access_token, "summary": 1, "filter": "toplevel"}

    r = requests.get(url, params=params)
    print(f"HTTP status {r.status_code}")
    if r.status_code not in [200, 201]:
        print(r.text)
        return []
    json_res = r.json()
    orders: list[Order] = []
    for item in json_res["data"]:
        message = item["message"]
        created_time = item["created_time"]
        order = convert_message_to_order(message, created_time, post_id)
        if order is not None:
            orders.append(order)
    return orders
