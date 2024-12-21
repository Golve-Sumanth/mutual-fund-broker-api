from fastapi import APIRouter, HTTPException, Depends
from app.utils.rapidapi import fetch_fund_family_schemes
from app.schemas.funds import FundFamilyRequest

router = APIRouter()

@router.get("/master")
def master_endpoint(Define_Mutual_Fund_Family: str):
    try:
        schemes = fetch_fund_family_schemes(Define_Mutual_Fund_Family)
        return {"fund_family": Define_Mutual_Fund_Family, "schemes": schemes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching mutual fund schemes: {str(e)}")


@router.post("/fetch")
def fetch_funds(request: FundFamilyRequest):
    try:
        funds = fetch_fund_family_schemes(request.fund_family)
        return funds
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
