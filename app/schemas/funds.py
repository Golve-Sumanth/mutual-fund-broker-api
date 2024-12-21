from pydantic import BaseModel

class FundFamilyRequest(BaseModel):
    fund_family: str
