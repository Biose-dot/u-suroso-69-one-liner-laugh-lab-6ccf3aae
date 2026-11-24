#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

The vacuum reframes the crime as a rescue mission: the sock was not eaten, it was saved from the floor — and life under the couch suits it far better.
"""
import os

ENTRY = "I didn't eat your sock — I rescued it from the floor. It lives under the couch now, and it has never been happier."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
