from twelvedata import TDClient
from statistics import mean
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Twelve Data client
td = TDClient(apikey="71a9440fcde34ad9a93fc38d13e5d748")

async def get_momentum(ticker: str):
    try:
        # Get the last 6 closing prices (so we can calculate 5 returns)
        ts = td.time_series(
            symbol=ticker,
            interval="1day",
            outputsize=6,
            order="desc"
        ).as_json()

        # Extract closing prices
        closes = [float(entry["close"]) for entry in ts]

        if len(closes) < 6:
            raise ValueError("Not enough data to calculate momentum")

        # Calculate 5 daily returns
        returns = [
            round((closes[i] - closes[i + 1]) / closes[i + 1], 2)
            for i in range(5)
        ]
        score = round(mean(returns), 3)

        return {
            "returns": returns,
            "score": score
        }

    except Exception as e:
        print("Twelve Data error:", e)
        return {
            "returns": [],
            "score": 0.0,
            "error": str(e)
        }
