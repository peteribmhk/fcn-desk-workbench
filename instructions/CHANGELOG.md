# Instruction Changelog

All instruction updates are logged here. Future AI assistants must read this file
after `current/` to understand what has changed since the last session.

---

## v1.0.0 — 2026-07-27
**Author:** Kimi Chat (initial infrastructure setup)
**Type:** Major

### Summary
Initial instruction infrastructure. Migrated all legacy root-level instruction files
(`AGENTS.md`, `assistant-operating-instructions.md`, `desk-memory.md`, `SYNC_PROTOCOL.md`,
`methodology.md`) into a versioned, numbered, traceable directory structure.

### Files Added
- `instructions/README.md` — Infrastructure philosophy and rules
- `instructions/CHANGELOG.md` — This file
- `instructions/current/01-agents.md` — Merged from `AGENTS.md`
- `instructions/current/02-operating-instructions.md` — Merged from `assistant-operating-instructions.md`
- `instructions/current/03-desk-memory.md` — Merged from `desk-memory.md`
- `instructions/current/04-sync-protocol.md` — Merged from `SYNC_PROTOCOL.md`
- `instructions/current/05-methodology.md` — Merged from `methodology.md`
- `instructions/current/06-data-policy.md` — **NEW** — Market data discovery, hierarchy, and calculation policy

### Breaking Changes
- AI assistants must now read from `instructions/current/` in numeric order, not from root-level `.md` files.
- Root-level instruction files (`AGENTS.md`, etc.) are deprecated but retained for backward compatibility during transition.

### Migration Notes
- Future sessions: read `instructions/current/01-agents.md` first, not `AGENTS.md`.
- The root-level files will be removed in v2.0.0.

---

## Template for Future Entries

```
## vX.Y.Z — YYYY-MM-DD
**Author:** [AI name] (session date)
**Type:** Major / Minor / Patch

### Summary
[One-paragraph summary]

### Files Changed
- `current/XX-filename.md` — [what changed]

### Breaking Changes
- [if any]

### Migration Notes
- [if any]
```
