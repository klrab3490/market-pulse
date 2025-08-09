import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from news import get_news

@pytest.mark.asyncio
@pytest.mark.parametrize("symbol,expected_min_length", [
    ("AAPL", 1),
    ("aapl", 1),
    ("", 0),
    (None, 0),
    ("INVALID", 0),
])
async def test_get_news_various_symbols(symbol, expected_min_length):
    """
    Test get_news with various symbols and check for expected results.
    """
    news = await get_news(symbol)
    assert isinstance(news, list)
    assert len(news) >= expected_min_length
    for item in news:
        assert isinstance(item, dict)
        assert "title" in item and isinstance(item["title"], str) and item["title"]
        assert "url" in item and isinstance(item["url"], str) and item["url"]

@pytest.mark.asyncio
async def test_get_news_structure():
    """
    Test that all news items have the required structure.
    """
    news = await get_news("AAPL")
    for item in news:
        assert set(["title", "url"]).issubset(item.keys())
        assert isinstance(item["title"], str)
        assert isinstance(item["url"], str)
