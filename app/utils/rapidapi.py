import requests
from app.config import settings

headers = {
    "X-RapidAPI-Key": settings.RAPIDAPI_KEY,
    "X-RapidAPI-Host": "latest-mutual-fund-nav.p.rapidapi.com"
}

BASE_URL = "https://latest-mutual-fund-nav.p.rapidapi.com"

# def fetch_fund_family_schemes(fund_family: str):
#     response = requests.get(f"{BASE_URL}/open-ended", headers=headers, params={"fund_family": fund_family})
#     response.raise_for_status()
#     return response.json()


# Fetch mutual fund schemes for a specific fund family
def fetch_fund_family_schemes(fund_family: str):
    try:
        # Define the endpoint and parameters
        endpoint = "/master"
        params = {
            "Define Mutual Fund Family": fund_family,
        }
        # Make the GET request
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching fund family schemes: {e}")
        raise
