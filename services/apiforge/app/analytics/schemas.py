from pydantic import BaseModel


class UsageSummaryResponse(
    BaseModel
):
    total_requests: int
    ocr_requests: int
    pdf_requests: int
    



class TopCapabilityResponse(
    BaseModel
):
    endpoint: str
    requests: int


class RequestVolumeResponse(
    BaseModel
):
    date: str
    requests: int