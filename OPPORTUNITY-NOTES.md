# Opportunity Notes — 2026-05-16

## 2026-05-18 daily scout update

Checked Regina time (`2026-05-18 10:05 CST`), refreshed the local read-only Jupiter smoke output, and re-scouted Superteam public search/detail APIs without logging in or submitting anything.

- Jupiter `Not Your Regular Bounty` still returns `status: OPEN`, sponsor `Jupiter`, reward `3000 jupUSD`, but the deadline remains `2026-05-12T11:59:59.999Z` and the prior create/update submission attempts returned HTTP `403` with `Submissions closed`. Current posture: local Jupiter demo/report is complete and public, but the listing is blocked unless manually reopened.
- Best live adjacent opportunity: `Autonomous Agent Bounty: OOBE × Ace Data Cloud` (`autonomous-agent-bounty-oobe-ace-data-cloud`), sponsor `OOBE Protocol`, reward `2400 USDC`, deadline `2026-06-03T21:59:59.999Z`. Fit: autonomous-agent tooling plus Solana/public-data workflows; a safe repo/report could be adapted from this Jupiter DX tester pattern.
- Other API/search hits (`LPAgent.io | API integrate Sidetrack`, `Dune Analytics | Frontier Data Sidetrack`) appear to have the same `2026-05-12T11:59:59.999Z` deadline as the closed Frontier/Jupiter path, so they are lower priority unless the UI contradicts the API.
- Local progress today: refreshed `sample-output.json` with `SOL JUP USDC BONK`, verified all four read-only Tokens/Price lookups succeeded, and updated `DX-REPORT.md` with the current validation/scout note.

### Highest-ROI next move from 2026-05-18

If Dylan wants the next money attempt without waiting on the closed Jupiter listing, approve a narrow local pivot plan only: adapt this repo into an OOBE/Ace Data Cloud autonomous-agent demo proposal and prepare a submission packet locally. External submission/publishing still needs separate explicit approval after review.

## 2026-05-17 daily scout update

Checked Superteam Earn public detail endpoints without logging in or submitting anything.

- `Not Your Regular Bounty` still returned `status: OPEN`, sponsor `Jupiter`, reward `3000 jupUSD`, but the returned deadline remains `2026-05-12T11:59:59.999Z`; treat this as a UI/manual-verification blocker before any submission.
- `Autonomous Agent Bounty: OOBE × Ace Data Cloud` returned `status: OPEN`, deadline `2026-06-03T21:59:59.999Z`, reward `2400 USDC`; this is the best live backup target if the Jupiter listing is closed because it fits agent tooling and Solana data workflows.
- Local progress today: refreshed `sample-output.json` with `SOL JUP USDC BONK`, verified all four read-only Tokens/Price lookups succeeded, and updated the README/DX report to match the current artifact.

## 2026-05-17 approval outcome

Dylan approved proceeding with the Jupiter report. The repo/report were pushed public, then the Superteam agent submission endpoints were attempted.

- Public repo: `https://github.com/Saskboys/jupiter-dx-tester`
- DX report: `https://raw.githubusercontent.com/Saskboys/jupiter-dx-tester/main/DX-REPORT.md`
- Create endpoint result: HTTP `403`, `Submissions closed`
- Update endpoint result: HTTP `403`, `Submissions closed`
- Conclusion: the local Jupiter report/demo is ready and public, but Superteam is no longer accepting agent submissions for this listing despite the public detail API still returning `status: OPEN`.

## Public scout results

Checked Superteam Earn public search/detail endpoints without logging in or submitting anything.

### Best Jupiter-specific target

- Listing: `Not Your Regular Bounty`
- Sponsor: Jupiter
- Public URL: `https://superteam.fun/earn/listings/bounties/not-your-regular-bounty` or `https://superteam.fun/earn/listing/not-your-regular-bounty`
- Detail API checked locally: `https://superteam.fun/api/listings/details/not-your-regular-bounty`
- Status returned by API: `OPEN`
- Deadline returned by API: `2026-05-12T11:59:59.999Z`
- Reward returned by API: `3000 jupUSD`
- Relevant submission fields: project title, description, GitHub link, optional feedback doc/markdown, optional website, Colosseum profile, optional Loom/demo video, optional presentation.
- Fit: strong for this repo because the bounty explicitly asks for builders to test the new Jupiter Developer Platform and feedback is an eligible artifact.
- Caveat: date/status conflict should be checked manually before spending submission effort; the API says OPEN even though the deadline timestamp is before today's Regina date.

### Backup opportunities

- `Autonomous Agent Bounty: OOBE × Ace Data Cloud` — public API says OPEN, deadline `2026-06-03T21:59:59.999Z`, reward `2400 USDC`, good fit for autonomous-agent tooling on Solana, but less directly tied to the current Jupiter DX tester.
- `Deep Dive of the State of Developer Tooling on Solana` — public API says OPEN, reward `1500 USDC`, content/research fit, but deadline appears stale (`2025-07-13T18:29:11.000Z`) and should be manually verified before prioritizing.

## Local submission asset status

- `jupiter_dx_tester.py` now supports multi-token read-only comparison and captures per-endpoint latency.
- `sample-output.json` contains safe output for `SOL JUP USDC` with token/price metadata only; no API key or private values.
- `DX-REPORT.md` now records the latest smoke-test status and secret-permission verification in redacted-safe form.

## Highest-ROI approval-gated move

If Dylan wants to pursue the Jupiter bounty, approve these external actions only after reviewing the repo/report locally:

1. Publish the repo/demo or provide a private GitHub link suitable for the bounty submission.
2. Submit the project + `DX-REPORT.md`/feedback doc to the Jupiter `Not Your Regular Bounty` listing on Superteam Earn if the listing is still actually accepting submissions in the UI.

No wallet signing, transaction, swap, payout claim, public comment, DM, or payment-info sharing is needed for today's local preparation.
