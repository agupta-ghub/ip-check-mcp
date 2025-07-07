from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import requests
import os

app = FastAPI()

IPQS_API_KEY = os.getenv("IPQS_API_KEY")
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")

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

    # Get geolocation info from ipinfo.io
    geo_res = requests.get(f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}")
    geo = geo_res.json()

    # Get risk score and VPN check from IPQualityScore
    risk_res = requests.get(f"https://ipqualityscore.com/api/json/ip/{IPQS_API_KEY}/{ip}")
    risk = risk_res.json()

    return IPResponse(
        ip=ip,
        country=geo.get("country", "Unknown"),
        city=geo.get("city", "Unknown"),
        region=geo.get("region", "Unknown"),
        isp=geo.get("org", "Unknown"),
        is_vpn=risk.get("vpn", False),
        risk_score=risk.get("fraud_score", 0)
    )

@app.get("/mcp-manifest.json")
def get_manifest():
    return FileResponse("mcp-manifest.json", media_type="application/json")
