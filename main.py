import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = "I didn't eat your sock. I performed an unscheduled deep-clean of its soul, and it tasted like victory and lint."
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
