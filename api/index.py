from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 154.49,
    "uptime_pct": 97.142,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 218.77,
    "uptime_pct": 99.378,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 193.28,
    "uptime_pct": 97.889,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 220.92,
    "uptime_pct": 98.382,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 165.91,
    "uptime_pct": 98.592,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 201.8,
    "uptime_pct": 99.008,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 223.6,
    "uptime_pct": 99.287,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 112.22,
    "uptime_pct": 97.463,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 150.19,
    "uptime_pct": 97.88,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 209.83,
    "uptime_pct": 99.073,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 128.99,
    "uptime_pct": 97.896,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 195.46,
    "uptime_pct": 98.051,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 180.35,
    "uptime_pct": 98.218,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 185.73,
    "uptime_pct": 98.194,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 222.02,
    "uptime_pct": 97.271,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 201.98,
    "uptime_pct": 97.448,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 220.14,
    "uptime_pct": 97.689,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 151.88,
    "uptime_pct": 99.045,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 135.81,
    "uptime_pct": 99.461,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 218.17,
    "uptime_pct": 97.274,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 206.89,
    "uptime_pct": 98.003,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 189.33,
    "uptime_pct": 98.304,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 234.61,
    "uptime_pct": 97.2,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 223.54,
    "uptime_pct": 98.324,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 169.28,
    "uptime_pct": 99.303,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 156.33,
    "uptime_pct": 98.867,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 132.22,
    "uptime_pct": 97.801,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 122.06,
    "uptime_pct": 98.409,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 135.07,
    "uptime_pct": 97.655,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 230.52,
    "uptime_pct": 99.396,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 113.58,
    "uptime_pct": 97.934,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 219.41,
    "uptime_pct": 97.705,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 137.29,
    "uptime_pct": 97.345,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 212.54,
    "uptime_pct": 99.191,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 178.32,
    "uptime_pct": 97.394,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 181.52,
    "uptime_pct": 97.654,
    "timestamp": 20250312
  }
]""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
