from enum import StrEnum

from fastapi import APIRouter
from pydantic import BaseModel

from src.calculate_service import calculate as cal


class Operator(StrEnum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "**"

class CalculateRequest(BaseModel):
    a: float
    b: float
    op: Operator

def get_api_router() -> APIRouter:

    router = APIRouter(prefix="/api")

    @router.post("/calculate")
    async def calculate(request: CalculateRequest):
        result = cal(a=request.a, b=request.b, operator=request.op)
        return result

    return router