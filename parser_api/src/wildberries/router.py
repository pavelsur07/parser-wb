from fastapi import APIRouter

from src.wildberries.schemas import GetWildberriesPostData, WildberriesPostData
from src.wildberries.service import get_wildberries_post_data_by_url


router = APIRouter(
    prefix='/wildberries',
    tags=['wildberries']
)


@router.get('/')
async def get_wildberries_post_by_url(
    wildberries_post: GetWildberriesPostData
) -> WildberriesPostData:
    post_data = await get_wildberries_post_data_by_url(wildberries_post.post_url)
    return post_data