#!/usr/bin/env python3
"""Ship It Friday — make.fun entry.

Writes one git commit message line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python 3 standard library only.
"""

import os
from pathlib import Path

LINE = "feat: I shipped the untested Friday refactor to prod at 4:59pm, rollback is a Monday problem"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # Single line, valid UTF-8, no trailing newline.
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
