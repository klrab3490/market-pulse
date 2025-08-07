from newsapi import NewsApiClient
from datetime import date, timedelta


newsapi = NewsApiClient(api_key="a5ebc344d56f4d4a9118ab741c4833ca")

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
