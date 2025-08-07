import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from momentum import get_momentum

@pytest.mark.asyncio
async def test_get_momentum_valid():
    result = await get_momentum("AAPL")
    assert "returns" in result
    assert "score" in result
    assert isinstance(result["score"], float)

@pytest.mark.asyncio
async def test_get_momentum_invalid():
    result = await get_momentum("INVALID_TICKER_123")
    assert "error" in result
