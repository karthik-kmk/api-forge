from pydantic import BaseModel


class PDFGenerateRequest(BaseModel):
    title: str
    content: str