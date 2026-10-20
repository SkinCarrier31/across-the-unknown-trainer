# Contributing to Across the Unknown Trainer

Thanks for your interest in the **Star Trek: Voyager - Across the Unknown** trainer project.

## Ground rules

- This is a hobbyist, educational trainer for a single-player game. Do not submit anything targeting multiplayer, anti-cheat protected titles, or other players.
- All offsets live in `signatures/` and must be re-dumped after each game patch.
- Keep handlers modular — one feature per file in `handlers/`.

## Workflow

1. Fork the repo, create a branch: `feat/crew-stat-editor` or `fix/overlay-dpi`.
2. Match the existing style: `loguru` for logging, `pydantic` for configs.
3. Add a test stub under `tests/` — even a smoke import is fine.
4. Open a PR describing the game build you tested on (e.g. `v1.0.4-steam`).

## Offset updates

When the game patches, run:

```
python -m tools.dump_offsets --process AcrossTheUnknown.exe --out signatures/current.json
```

Then update `signatures/current.json` and bump `signatures/version.txt`.

## Reporting bugs

Include the game version, trainer version, and a `logs/trainer.log` snippet.