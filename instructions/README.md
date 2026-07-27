# Instruction Infrastructure

This directory is the **single source of truth** for all AI assistant instructions.
Every instruction update is versioned, traceable, and independently reviewable.

## Philosophy

- **GitHub is the master copy.** Every durable instruction change must be committed to this repo.
- **Versions are immutable.** Once a version is tagged, it never changes. New updates create new versions.
- **Current is a symlink to the latest version.** AI assistants always read from `current/`.
- **Changelog is mandatory.** Every change must be documented in `CHANGELOG.md`.

## Directory Structure

```
instructions/
├── README.md                 # This file
├── CHANGELOG.md              # All instruction changes, dated and signed
├── current/                  # Symlink or copy of the latest version
│   ├── 01-agents.md
│   ├── 02-operating-instructions.md
│   ├── 03-desk-memory.md
│   ├── 04-sync-protocol.md
│   ├── 05-methodology.md
│   └── 06-data-policy.md
└── versions/
    ├── v1.0.0-2026-07-27/
    │   ├── 01-agents.md
    │   ├── 02-operating-instructions.md
    │   └── ...
    ├── v1.1.0-2026-08-15/
    │   └── ...
    └── v2.0.0-2026-09-01/
        └── ...
```

## Versioning Rules

| Version bump | Trigger |
|-------------|---------|
| **Major (X.0.0)** | Fundamental workflow change, new AI assistant type, or breaking change to read order |
| **Minor (x.Y.0)** | New instruction file added, new section to existing file, or methodology upgrade |
| **Patch (x.y.Z)** | Clarification, typo fix, or non-breaking refinement |

## AI Assistant Read Order

Every new session must read files in `current/` in **strict numeric order**:

1. `01-agents.md` — Continuity rules and source-of-truth policy
2. `02-operating-instructions.md` — Session startup, readback rules, verification gates
3. `03-desk-memory.md` — Durable user preferences and workflow memory
4. `04-sync-protocol.md` — GitHub-master sync protocol
5. `05-methodology.md` — FCN screening and ranking methodology
6. `06-data-policy.md` — Market data hierarchy, source discovery, and calculation rules

After reading instructions, read:
- `watchlist.csv`
- `daily/latest.md`
- `daily/index.md`
- `data-sources/registry.json`
- `issuer-mimicry/assumptions/default.json`
- Relevant `daily/archive/` files

## How to Update Instructions

1. Create a new version directory under `versions/` with the new version number and date.
2. Copy all files from the previous version.
3. Apply your changes. Each file change must be atomic and documented.
4. Update `CHANGELOG.md` with:
   - Version number and date
   - Author (AI assistant name + session date)
   - Summary of changes per file
   - Breaking changes (if any)
   - Migration notes for future sessions
5. Update `current/` to mirror the new version (or use a symlink if your platform supports it).
6. Commit to GitHub with message: `instructions: bump to vX.Y.Z — [brief summary]`.

## Commit Hygiene

- Never commit instruction changes without updating `CHANGELOG.md`.
- Never modify a version directory after it is committed.
- Never leave `current/` out of sync with the latest version.
- Use atomic commits: one logical change per commit, not bulk dumps.
