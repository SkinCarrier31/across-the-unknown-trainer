"""Dev tool: dump candidate offsets from a running game."""
import argparse
import json
from pathlib import Path
from core.process_attach import GameProcess


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--process", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    proc = GameProcess.attach(args.process)
    base = proc.base
    data = {
        "build": "dev-dump",
        "base": base,
        "note": "manual verification required",
    }
    Path(args.out).write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Dumped base=0x{base:X} to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())