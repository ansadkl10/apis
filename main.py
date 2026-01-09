from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

EXTERNAL_API = "https://eypz-bypass.vercel.app/api/terabox"
API_KEY = "eypz-pvt"

@app.get("/")
def home():
    return {"status": "API is running on Koyeb!"}

@app.get("/bypass")
def bypass(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL missing!")

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    payload = {
        "url": url,
        "apikey": API_KEY
    }

    try:
        response = requests.post(EXTERNAL_API, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
