from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Replace with your IPQualityScore API key
IPQS_API_KEY = os.getenv("IPQS_API_KEY")

class IPRequest(BaseModel):
    ip: str

class IPResponse(BaseModel):
    ip: str
    country: str
    city: str
    region: str
    isp: str
    is_vpn: bool
    risk_score: int

@app.post("/lookup_ip", response_model=IPResponse)
def lookup_ip(request: IPRequest):
    ip = request.ip

    # Step 1: IP geolocation (using ipapi.co)
    geo = requests.get(f"https://ipapi.co/{ip}/json/").json()

    # Step 2: Risk score + VPN check (IPQualityScore)
    risk = requests.get(
        f"https://ipqualityscore.com/api/json/ip/{IPQS_API_KEY}/{ip}"
    ).json()

    return IPResponse(
        ip=ip,
        country=geo.get("country_name", "Unknown"),
        city=geo.get("city", "Unknown"),
        region=geo.get("region", "Unknown"),
        isp=geo.get("org", "Unknown"),
        is_vpn=risk.get("vpn", False),
        risk_score=risk.get("fraud_score", 0)
    )
