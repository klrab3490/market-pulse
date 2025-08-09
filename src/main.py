from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

# Importing Custom Modules
from momentum import get_momentum
from news import get_news
from llm import get_market_pulse
from cache import get_cached_response

app = FastAPI()

# ✅ Allow CORS for frontend on localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "https://market-pulse-murex.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Market Pulse API"}

@app.get("/api/v1/market-pulse")
async def market_pulse(ticker: str = Query(..., min_length=1)):
    # Check in-memory cache
    cached = get_cached_response(ticker)
    if cached:
        return cached

    # Fetch signals
    momentum = await get_momentum(ticker)
    # print("Momentum data:", momentum)
    news = await get_news(ticker)
    # print("News data:", news)

    # Get LLM output
    pulse, explanation = await get_market_pulse(ticker, momentum, news)
    # print("LLM Pulse:", pulse, "Explanation:", explanation)

    response = {
        "ticker": ticker.upper(),
        "as_of": str(date.today()),
        "momentum": momentum,
        "news": news,
        "pulse": pulse,
        "llm_explanation": explanation
    }

    # Store in cache
    get_cached_response(ticker, response)

    return response