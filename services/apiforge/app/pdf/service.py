from io import BytesIO

from reportlab.lib.pagesizes import letter

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from app.pdf.exceptions import (
    PDFGenerationException
)


class PDFService:

    async def generate_pdf(
        self,
        title: str,
        content: str
    ) -> BytesIO:

        try:

            buffer = BytesIO()

            document = SimpleDocTemplate(
                buffer,
                pagesize=letter
            )

            styles = getSampleStyleSheet()

            elements = [
                Paragraph(
                    title,
                    styles["Title"]
                ),
                Spacer(1, 12),
                Paragraph(
                    content,
                    styles["BodyText"]
                )
            ]

            document.build(
                elements
            )

            buffer.seek(0)

            return buffer

        except Exception as e:
            raise PDFGenerationException() from e