from newsapi import NewsApiClient
from dotenv import load_dotenv
load_dotenv()
import os

# Initialize NewsAPI client
# Ensure you have set the NEWS_API_KEY environment variable
newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

# Function to get news articles for a given ticker
# This function fetches the latest news articles related to the ticker
async def get_news(ticker: str):
    try:
        # Fetch articles using the SDK
        response = newsapi.get_everything(
            q=ticker,
            language='en',
            sort_by='relevancy',
            page_size=5
        )

        articles = response.get("articles", [])
        return [
            {
                "title": article.get("title") or "No title available",
                "description": article.get("description") or "No description available",
                "url": article.get("url")
            }
            for article in articles
        ]
    except Exception as e:
        print("NewsAPI error:", e)
        return []
