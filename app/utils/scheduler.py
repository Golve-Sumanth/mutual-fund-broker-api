from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.portfolio import Portfolio
from app.utils.rapidapi import fetch_fund_family_schemes

scheduler = BackgroundScheduler()

def update_portfolio():
    db: Session = SessionLocal()
    try:
        # Fetch all portfolio entries
        portfolios = db.query(Portfolio).all()
        
        for portfolio in portfolios:
            # Fetch updated NAV for the fund
            try:
                fund_data = fetch_fund_family_schemes(portfolio.fund_name)
                updated_nav = fund_data.get("nav")

                if updated_nav:
                    # Update NAV in the database
                    portfolio.nav = updated_nav
                    db.commit()
                    print(f"Updated NAV for {portfolio.fund_name} to {updated_nav}")

            except Exception as e:
                print(f"Failed to update NAV for {portfolio.fund_name}: {str(e)}")

    finally:
        db.close()

scheduler.add_job(update_portfolio, "interval", hours=1)
scheduler.start()