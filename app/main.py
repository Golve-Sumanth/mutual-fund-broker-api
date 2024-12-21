from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.funds import router as funds_router
from app.routes.portfolio import router as portfolio_router
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(funds_router, prefix="/funds", tags=["Funds"])
app.include_router(portfolio_router, prefix="/portfolio", tags=["Portfolio"])

@app.get("/")
def read_root():
    return {"message": "Mutual Fund Broker API is running"}
