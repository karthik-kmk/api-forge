from pydantic import BaseModel, HttpUrl


class ScreenshotRequest(BaseModel):

    url: HttpUrl

    full_page: bool = False

    width: int = 1280

    height: int = 720