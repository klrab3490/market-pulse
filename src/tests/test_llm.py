import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from llm import get_market_pulse

@pytest.mark.asyncio
async def test_prompt_response_format():
    sample_momentum = {"returns": [0.01, -0.02, 0.01, 0.00, 0.03], "score": 0.006}
    sample_news = [{"title": "Growth in stock", "description": "Stock is climbing", "url": "http://example.com"}]

    sentiment, explanation = await get_market_pulse("AAPL", sample_momentum, sample_news)

    assert sentiment.lower() in ["bullish", "bearish", "neutral"]
    assert isinstance(explanation, str)
    assert len(explanation) > 0
