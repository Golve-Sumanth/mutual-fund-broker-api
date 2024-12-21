from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.portfolio import Portfolio
from app.schemas.portfolio import PortfolioRequest

router = APIRouter()

@router.post("/add")
def add_to_portfolio(request: PortfolioRequest, db: Session = Depends(get_db)):
    portfolio_item = Portfolio(
        user_id=request.user_id,
        fund_name=request.fund_name,
        units=request.units,
        nav=request.nav
    )
    db.add(portfolio_item)
    db.commit()
    return {"message": "Added to portfolio"}