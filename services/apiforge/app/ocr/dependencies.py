from app.ocr.service import OCRService

ocr_service = OCRService()


def get_ocr_service() -> OCRService:
    return ocr_service