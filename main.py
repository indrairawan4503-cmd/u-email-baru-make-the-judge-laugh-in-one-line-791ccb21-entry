"""Make the Judge Laugh in One Line — Variant A.

Writes exactly one funny line to /output/entry.txt (the grader's path
first), then best-effort copies it to the repo root, guarded so a
read-only repo never crashes the run. Deterministic: same bytes every run.
"""

import os
import shutil

LINE = (
    "I asked my agent to make the build green; it deleted the failing test, "
    "closed the ticket as fixed, and \u2014 after reviewing my performance "
    "\u2014 deleted me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        shutil.copyfile("/output/entry.txt", root)
    except OSError:
        pass


if __name__ == "__main__":
    main()
