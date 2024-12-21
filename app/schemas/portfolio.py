from pydantic import BaseModel

class PortfolioRequest(BaseModel):
    user_id: int
    fund_name: str
    units: float
    nav: float