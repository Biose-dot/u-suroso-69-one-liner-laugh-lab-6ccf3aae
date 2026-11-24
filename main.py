#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

The excuse a robot vacuum gives after eating a sock: it did not eat it, it adopted it — and the sock has never been happier under the couch.
"""
import os

ENTRY = "I didn't eat your sock. I adopted it. It lives under the couch now, and frankly, it has never looked happier."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
