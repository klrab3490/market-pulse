from time import time

CACHE = {}
# TTL = 600  # 10 minutes
TTL = 86400  # 24 hours

def get_cached_response(ticker, data=None):
    now = time()
    key = ticker.upper()

    if data:
        CACHE[key] = {"data": data, "timestamp": now}
        return

    if key in CACHE and (now - CACHE[key]["timestamp"]) < TTL:
        return CACHE[key]["data"]

    return None
