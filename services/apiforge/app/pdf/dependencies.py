from app.pdf.service import PDFService


def get_pdf_service() -> PDFService:
    return PDFService()