from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from time import time
import random

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


RATE_LIMIT = 5
TIME_WINDOW = 60  
client_requests = {}

quotes = [
    "Stay hungry, stay foolish.",
    "Believe you can and you're halfway there.",
    "Dream big and dare to fail.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Everything you can imagine is real."
]

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    client_ip = request.client.host
    current_time = time()

    requests = client_requests.get(client_ip, [])
    requests = [r for r in requests if current_time - r < TIME_WINDOW]

    if len(requests) >= RATE_LIMIT:
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded. Please wait a minute."}
        )

    requests.append(current_time)
    client_requests[client_ip] = requests
    return await call_next(request)

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}
