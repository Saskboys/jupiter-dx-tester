# DX Report — Jarvis Jupiter DX Tester

## Project

Jarvis Jupiter DX Tester is a read-only, agent-built demo that uses the Jupiter Developer Platform Tokens and Price APIs to create a quick token comparison scorecard.

The build intentionally starts with low-risk API surfaces so an AI agent can validate auth, collect useful data, and produce developer-experience feedback without touching wallets, swaps, or transaction signing.

## Build status

Validated locally on `2026-05-16 22:19:55 CST` with:

```bash
python3 jupiter_dx_tester.py SOL
python3 jupiter_dx_tester.py JUP
python3 jupiter_dx_tester.py SOL JUP USDC > sample-output.json
```

The Jupiter secret file existed locally with `0600` permissions. No raw secret values were printed, committed, or written into this report.

Working endpoints:

- `GET https://api.jup.ag/tokens/v2/search?query=SOL`
- `GET https://api.jup.ag/price/v3?ids=<token_mint>`

Auth header that worked:

```text
x-api-key: <Jupiter Developer Platform API key>
```

## What worked

- The API key worked from a non-interactive terminal script.
- `x-api-key` authentication worked for `api.jup.ag` Tokens and Price endpoints.
- Tokens API and Price API were safe for AI-agent testing because they are read-only and do not require wallet signing.
- Token search returned useful metadata: symbol, name, mint ID, verification signal, organic score, and decimals.
- Price API returned useful fields: USD price, liquidity, 24h price change, and block ID.
- Multi-token comparison (`SOL JUP USDC`) worked in one run and produced `sample-output.json` with endpoint latency evidence.

## What the demo proves

This demo proves a safe first step for agent-assisted Jupiter development:

1. Load a Developer Platform key from a local secret file.
2. Call read-only APIs.
3. Collect token and market data.
4. Record latency and response shape.
5. Produce feedback without exposing credentials or creating financial risk.

That is useful because AI agents should not start with wallet signing or funded routes. They should first prove that auth, docs, read-only endpoints, JSON response shapes, and error handling are reliable.

## Friction and docs feedback

The highest-value documentation improvement is clearer labelling around endpoint risk:

- Read-only / no wallet needed.
- Builds a transaction but does not sign.
- Requires wallet signing or funded action.

Other specific feedback:

- The exact auth header should be extremely visible in every quickstart: `x-api-key`.
- Each endpoint should have a non-interactive `curl` example and a minimal JSON response example.
- Error examples would help agents recover faster: missing key, invalid key, rate limit, malformed mint, empty search result.
- A first-party "agent-safe quickstart" would be valuable: Tokens search -> Price lookup -> then optional transaction-building APIs only after human approval.

More detailed notes are in `DOCS-FINDINGS.md`.

## AI stack feedback

Jupiter's AI stack direction is exactly the right area to invest in. The parts that matter most for autonomous coding agents are:

- Compact skill/context files that tell an agent which endpoints exist and which ones are safe.
- CLI and curl examples that are JSON-native and non-interactive.
- Clear wallet/signing boundaries.
- A recommended pattern for redacting API keys and safely sharing sample output.
- A first-party MCP/llms.txt path that lets an agent answer "what endpoint should I use?" without scraping UI pages.

What I wish existed: a Jupiter "Agent Safety Contract" page that marks each API as read-only, transaction-building, or wallet/funded. That would let agents build faster while keeping humans in control of dangerous actions.

## Safety note

This demo does not trade, swap, sign transactions, connect a wallet, build transactions, use private keys, or spend funds.

## Next improvements if selected

- Add an HTML report generator.
- Add more token metrics and error-path examples.
- Extend into a tiny dashboard that compares tokens and flags docs/API edge cases.
- Add optional integration with Jupiter AI Stack / CLI once the safe agent flow is documented.
