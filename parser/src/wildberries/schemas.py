from pydantic import BaseModel, HttpUrl


class GetWildberriesPostData(BaseModel):
    post_url: HttpUrl


class WildberriesPostData(BaseModel):
    post_id: int
    created_at: float
    updated_at: float
    post_url: HttpUrl
    name: str
    description: str
    price: float
    sale_price: float
    category: str
    photos: list[HttpUrl]
    options: list[str]
    colors: list[str]
    sizes: list[str]
    brand: str