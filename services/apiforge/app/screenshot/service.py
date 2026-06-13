from playwright.async_api import async_playwright

from .exceptions import InvalidURLException


class ScreenshotService:

    def validate_url(
        self,
        url: str
    ):

        blocked = [

            "localhost",

            "127.0.0.1",

            "0.0.0.0",

            "10.",

            "192.168.",

            "172.16.",

            "file://",

            "ftp://"
        ]

        for item in blocked:

            if item in url:

                raise InvalidURLException()


    async def capture(
        self,
        url: str,
        full_page: bool,
        width: int,
        height: int
    ):

        self.validate_url(url)

        async with async_playwright() as p:

            browser = await p.chromium.launch()

            page = await browser.new_page(
                viewport={
                    "width": width,
                    "height": height
                }
            )

            await page.goto(
                url,
                wait_until="networkidle"
            )

            image = await page.screenshot(
                full_page=full_page
            )

            await browser.close()

            return image