from sqlalchemy import (
    select,
    func,
    desc,
    cast,
    Date
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.api_usage import APIUsage


class AnalyticsRepository:

    def __init__(
        self,
        db: AsyncSession
    ):
        self.db = db

    async def get_total_requests(
        self
    ) -> int:

        result = await self.db.execute(
            select(
                func.count(
                    APIUsage.id
                )
            )
        )

        return result.scalar() or 0

    async def get_ocr_requests(
        self
    ) -> int:

        result = await self.db.execute(
            select(
                func.count(
                    APIUsage.id
                )
            ).where(
                APIUsage.endpoint
                == "/v1/ocr/extract"
            )
        )

        return result.scalar() or 0

    async def get_pdf_requests(
        self
    ) -> int:

        result = await self.db.execute(
            select(
                func.count(
                    APIUsage.id
                )
            ).where(
                APIUsage.endpoint
                == "/v1/pdf/generate"
            )
        )

        return result.scalar() or 0

    async def get_top_capabilities(
        self
    ):

        result = await self.db.execute(
            select(
                APIUsage.endpoint,
                func.count(
                    APIUsage.id
                ).label(
                    "requests"
                )
            )
            .group_by(
                APIUsage.endpoint
            )
            .order_by(
                desc(
                    "requests"
                )
            )
        )

        return result.all()

    async def get_request_volume(
        self
    ):

        result = await self.db.execute(
            select(
                cast(
                    APIUsage.created_at,
                    Date
                ).label(
                    "date"
                ),
                func.count(
                    APIUsage.id
                ).label(
                    "requests"
                )
            )
            .group_by(
                cast(
                    APIUsage.created_at,
                    Date
                )
            )
            .order_by(
                cast(
                    APIUsage.created_at,
                    Date
                )
            )
        )

        return result.all()