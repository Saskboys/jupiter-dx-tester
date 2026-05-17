# Jupiter Developer Platform Docs Findings

These notes come from building the read-only Jarvis Jupiter DX Tester with the Jupiter Developer Platform Tokens and Price APIs.

## What worked well

- A single Developer Platform API key worked across both Tokens and Price APIs.
- `x-api-key` authentication was easy to automate once the exact header name was known.
- The Tokens API response gave enough metadata to build a useful token scorecard: symbol, name, mint id, decimals, verification signal, and organic score.
- The Price API gave usable market fields for downstream decision support: USD price, liquidity, 24h price change, and block id.
- Read-only endpoints are ideal for AI-agent onboarding because they let an agent validate auth and data access without wallet signing or funded actions.

## Friction found

- Auth/header clarity is the highest-value docs item. For agent builders, examples should repeatedly show the exact header:

```text
x-api-key: <Jupiter Developer Platform API key>
```

- The docs should clearly separate read-only endpoints from endpoints that can build/sign/execute transactions.
- AI agents benefit from copy-pasteable, non-interactive `curl` examples and minimal JSON output examples for each endpoint.
- Error examples would help: missing key, invalid key, rate limit, malformed token mint/id, and no token search results.
- It would be useful to have one "first 10 minutes" tutorial that starts with Tokens + Price, then safely introduces transaction-building endpoints only after a human explicitly approves wallet scope.

## Suggested improvements

1. Add an "Agent-safe quickstart" path:
   - Step 1: create API key.
   - Step 2: run a read-only Tokens search.
   - Step 3: run a read-only Price lookup.
   - Step 4: only then explain transaction-building APIs and wallet/signing boundaries.
2. Add a copy-paste multi-token example: `SOL`, `JUP`, `USDC`.
3. Add a docs table marking each API as:
   - Read-only/no wallet.
   - Builds transaction but does not sign.
   - Requires wallet/signing/funded action.
4. Add LLM/agent snippets for Python, Node, and `curl` with explicit timeout/error handling.
5. Add a tiny public sample app/repo that demonstrates Developer Platform auth without storing or logging secrets.

## AI stack feedback

The AI-agent path works best when the agent can:

- Read a compact skill/instruction file.
- Use CLI/curl examples non-interactively.
- Run a smoke test and capture redacted JSON evidence.
- Produce a DX report without exposing keys.

The missing piece is a first-party "agent safety contract" in the docs: which endpoints are safe for autonomous read-only testing, which endpoints require human wallet approval, and how an agent should phrase that approval gate.
