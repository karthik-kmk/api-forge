from app.analytics.repository import (
    AnalyticsRepository
)


class AnalyticsService:

    def __init__(
        self,
        repository: AnalyticsRepository
    ):
        self.repository = repository

    async def get_usage_summary(
        self
    ):

        total_requests = (
            await self.repository.get_total_requests()
        )

        ocr_requests = (
            await self.repository.get_ocr_requests()
        )

        pdf_requests = (
            await self.repository.get_pdf_requests()
        )

        return {
            "total_requests": total_requests,
            "ocr_requests": ocr_requests,
            "pdf_requests": pdf_requests
        }

    async def get_top_capabilities(
        self
    ):

        rows = await self.repository.get_top_capabilities()

        return [
            {
                "endpoint": row.endpoint,
                "requests": row.requests
            }
            for row in rows
        ]

    async def get_request_volume(
        self
    ):

        rows = await self.repository.get_request_volume()

        return [
            {
                "date": str(
                    row.date
                ),
                "requests": row.requests
            }
            for row in rows
        ]