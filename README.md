# Jarvis Jupiter DX Tester

A small, read-only Jupiter Developer Platform demo built for the Superteam Earn / Frontier "Not Your Regular Bounty" track.

The project uses one Jupiter Developer Platform API key to combine the Tokens and Price APIs into a simple token scorecard. It is intentionally safe for agent-driven testing: no swaps, no trades, no transaction building, no wallet connection, and no signing.

## What it does

- Loads the Jupiter Developer Platform API key from a local secret file: `~/.hermes/secrets/jupiter_developer_platform.json`
- Searches Jupiter Tokens API for one or more token symbols/queries
- Fetches Price API data for the top token result
- Captures basic per-endpoint latency in milliseconds
- Prints a JSON comparison report for tokens such as `SOL`, `JUP`, `USDC`, and `BONK`

## Safety

This demo is read-only. It does **not**:

- Trade
- Swap
- Build transactions
- Sign transactions
- Connect a wallet
- Spend funds
- Store or print the raw API key

## Run

```bash
python3 jupiter_dx_tester.py SOL
python3 jupiter_dx_tester.py JUP
python3 jupiter_dx_tester.py SOL JUP USDC BONK > sample-output.json
```

Expected secret format:

```json
{
  "apiKey": "YOUR_JUPITER_DEVELOPER_PLATFORM_KEY"
}
```

## Files

- `jupiter_dx_tester.py` — read-only demo script
- `sample-output.json` — safe example output from `SOL JUP USDC`
- `DX-REPORT.md` — developer-experience report for Jupiter
- `DOCS-FINDINGS.md` — specific docs and AI-agent feedback
- `OPPORTUNITY-NOTES.md` — local notes about the matching Superteam listing

## Submission summary

This is not trying to win by being a flashy trading bot. The point is to give Jupiter clear DX signal from an AI-agent builder workflow:

1. Can an agent safely onboard with the Developer Platform?
2. Which docs/auth details matter most?
3. What should be labelled as read-only vs wallet/signing scope?
4. How can Jupiter make builders productive faster?
