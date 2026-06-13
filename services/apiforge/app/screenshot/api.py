from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import Response

from app.core.api_key_auth import (
    get_current_api_key
)

from .schemas import ScreenshotRequest

from .service import ScreenshotService


router = APIRouter(

    prefix="/v1/screenshot",

    tags=["Screenshot"]

)


@router.post(
    "",
    dependencies=[
        Depends(get_current_api_key)
    ]
)
async def capture_screenshot(
    payload: ScreenshotRequest
):

    service = ScreenshotService()

    image = await service.capture(

        url=str(payload.url),

        full_page=payload.full_page,

        width=payload.width,

        height=payload.height
    )

    return Response(

        content=image,

        media_type="image/png"
    )