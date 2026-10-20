# Security Policy

## Scope

This repository is a **single-player trainer** for *Star Trek: Voyager - Across the Unknown*.
It attaches to the local game process via `OpenProcess`/`ReadProcessMemory` and
writes to a small set of signature-located addresses.

## What we do NOT do

- No kernel drivers.
- No network exfiltration.
- No persistence outside `%APPDATA%/AcrossTheUnknownTrainer/`.
- No bundled binaries — everything is Python source, auditable.

## Reporting

If you find a vulnerability (e.g. an unsafe pointer chain that could crash
the game, or an unintended write outside the game's heap), open a private
security advisory on GitHub. Do not file a public issue for memory-safety
problems.

## Verifying releases

Every release tag is signed. Compare the `SHA256SUMS` file against the
attached artifact before running.