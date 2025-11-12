from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")


@app.get("/api/photos")
def get_random_photos(per_page: int = Query(10, ge=1, le=30)):
    url = "https://api.unsplash.com/photos/random"
    params = {
        "count": per_page,
        "client_id": UNSPLASH_ACCESS_KEY,
    }
    response = httpx.get(url, params=params, verify=False)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
