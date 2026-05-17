#!/usr/bin/env python3
"""Read-only Jupiter Developer Platform API demo.

No trading, no signing, no wallet access. Uses Tokens + Price APIs only.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

SECRET_PATH = Path.home() / ".hermes" / "secrets" / "jupiter_developer_platform.json"
API_BASE = "https://api.jup.ag"


def load_key():
    with open(SECRET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    key = data.get("apiKey")
    if not key:
        raise RuntimeError(f"Missing apiKey in {SECRET_PATH}")
    return key


def get_json(path, api_key):
    url = API_BASE + path
    req = urllib.request.Request(
        url,
        headers={
            "x-api-key": api_key,
            "User-Agent": "Jarvis-Saskboys-Jupiter-DX-Tester/0.2",
        },
    )
    start = time.perf_counter()
    with urllib.request.urlopen(req, timeout=20) as r:
        payload = json.loads(r.read().decode("utf-8"))
    elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
    return payload, {"path": path.split("?")[0], "elapsed_ms": elapsed_ms}


def score_token(query, api_key):
    tokens, token_timing = get_json("/tokens/v2/search?" + urllib.parse.urlencode({"query": query}), api_key)
    if not tokens:
        return {
            "query": query,
            "found": False,
            "message": "No token results",
            "timings": [token_timing],
        }

    top = tokens[0]
    token_id = top.get("id")
    prices, price_timing = get_json("/price/v3?" + urllib.parse.urlencode({"ids": token_id}), api_key)
    price = prices.get(token_id, {})

    return {
        "query": query,
        "found": True,
        "token": {
            "symbol": top.get("symbol"),
            "name": top.get("name"),
            "id": token_id,
            "decimals": top.get("decimals"),
            "verified": top.get("isVerified") or top.get("verified"),
            "organicScore": top.get("organicScore"),
        },
        "price": {
            "usdPrice": price.get("usdPrice"),
            "liquidity": price.get("liquidity"),
            "priceChange24h": price.get("priceChange24h"),
            "blockId": price.get("blockId"),
        },
        "timings": [token_timing, price_timing],
    }


def main():
    queries = sys.argv[1:] or ["SOL"]
    api_key = load_key()
    results = [score_token(query, api_key) for query in queries]

    report = {
        "mode": "read_only_tokens_price_comparison",
        "queries": queries,
        "results": results,
        "dx_notes": [
            "x-api-key header worked for api.jup.ag Tokens and Price endpoints.",
            "Read-only Price and Tokens APIs are safe for agent testing because they do not require wallet signing.",
            "Multi-token comparison now captures basic endpoint latency for DX/reporting evidence.",
            "Next DX step: document docs links, auth/header clarity, error messages, and AI-stack usefulness.",
        ],
        "safety": "No trading, swaps, transaction building, wallet connection, signing, or funded actions.",
    }
    print(json.dumps(report, indent=2))
    return 0 if all(item.get("found") for item in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
