"""make.fun bounty u-suga-everyday-things-two-lines-longer-run-f8734479:
Everyday Things, Two Lines, Longer Run.

Writes two lines to /output/entry.txt in the grading sandbox (or to
./output/entry.txt when run locally where /output does not exist).

Line 1 explains a queue to a 10-year-old in a single vivid sentence
built on one analogy. Line 2 says in one sentence why that analogy
works: what it maps and what it leaves out. Nothing else.

Deterministic: no network, no randomness, no model calls, no time
or environment dependence. Both runs write the same bytes.
"""

import os

LINE_1 = (
    "A queue is a row of dominoes that refuses to fall, each person "
    "shuffling forward one small step at a time."
)

LINE_2 = (
    "It maps the single-file line and the slow forward shuffle, but "
    "leaves out that one nudge topples a domino, while people step "
    "forward only when they decide to, never because something pushed them."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def output_dir() -> str:
    if os.path.isdir("/output"):
        return "/output"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output")


def main() -> None:
    out = output_dir()
    # Create the output directory first, before any file is written.
    os.makedirs(out, exist_ok=True)
    # Clear only the directory's contents, never the directory itself.
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
