# Changelog

## 2.2.13 — packaging and developer experience

- Added explicit `spluspy.selfbot` and `spluspy.bot` entry points.
- Added `Bot` and `BotClient` aliases for the official HTTP `Robot` client.
- Made root-level exports lazy so the official HTTP client does not initialize the self-bot crypto stack on import.
- Added package metadata and explicit runtime dependencies (`aiohttp`, `pyaes`, `pydantic`).
- Added architecture, API, development and extracted method-catalog documentation.
- Added examples, source-integrity tests and a Python-version CI workflow.
- Preserved the existing root-level import names for compatibility.

### Notes

- No unverified Soroush Plus server endpoints were fabricated. Group moderation methods should only be added after the server-side endpoint and payload are confirmed.
- End-to-end integration against a live Soroush Plus account/API was not run in this environment.
