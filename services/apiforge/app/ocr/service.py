import tempfile

import pytesseract

from PIL import Image

from fastapi import UploadFile

from app.ocr.exceptions import (
    UnsupportedFileTypeException,
    OCRProcessingException
)


class OCRService:

    async def extract_text(
        self,
        file: UploadFile
    ) -> str:

        allowed_extensions = (
            ".png",
            ".jpg",
            ".jpeg"
        )

        if not file.filename.lower().endswith(
            allowed_extensions
        ):
            raise UnsupportedFileTypeException()

        try:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=file.filename
            ) as temp_file:

                content = await file.read()

                temp_file.write(content)

                temp_path = temp_file.name

            image = Image.open(temp_path)

            text = pytesseract.image_to_string(
                image
            )

            return text.strip()

        except Exception as e:
            raise OCRProcessingException() from e