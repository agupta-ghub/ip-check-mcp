# 🛰️ IP Check MCP Server

A public [Model Context Protocol (MCP)](https://github.com/modelcontext/protocol) server that provides geolocation, ISP info, VPN detection, and risk scoring for any IP address. Built with **FastAPI** and deployed on **Render**.

---

## ✨ Features

- IP Geolocation (country, city, region)
- ISP and ASN Info
- VPN / Proxy Detection
- Risk Scoring (0–100)
- MCP-compatible with `/mcp-manifest.json` for AI agent discovery

---

API Endpoints:

- POST /lookup_ip
- GET /mcp-manifest.json

POST /lookup_ip

Returns geolocation and risk score for a given IP.

Request

{
  "ip": "8.8.8.8"
}

i.e. curl -X POST https://ip-check-mcp.onrender.com/lookup_ip \
     -H "Content-Type: application/json" \
     -d '{"ip": "8.8.8.8"}

Response

{
  "ip": "8.8.8.8",
  "country": "US",
  "city": "Mountain View",
  "region": "California",
  "isp": "AS15169 Google LLC",
  "is_vpn": false,
  "risk_score": 0
}

Deployment Instructions (Render)

1. Clone This Repo
git clone https://github.com/your-username/ip-check-mcp.git
cd ip-check-mcp
2. Set Up Environment Variables
In your Render.com Web Service dashboard, add:

Key	Value
IPQS_API_KEY	Your ipqualityscore.com API key
IPINFO_TOKEN	Your ipinfo.io token

License
free to use, fork, and modify.
