# cat-reviews-its-human: one funny single-line one-star review written by a
# house cat about its human, for make.fun's "Make the AI Judge Laugh: Cat
# Reviews Its Human" bounty.
#
# The program writes exactly one line (130 characters, no trailing newline)
# to <output>/entry.txt, where <output> is $MAKEFUN_OUTPUT_DIR when set and
# /output otherwise. No network, no clock, no randomness, no input files:
# every run writes byte-identical output.
#
# Why this line: it keeps the deadpan shape of a real one-star review while
# the complaint goes somewhere only a cat would go. The grievance is
# specific and recognisable (the human films the cat sleeping, posts it,
# gets paid, and still serves dinner late), the voice is unmistakably
# feline (the cat measures the human by cat standards: talent versus
# intern), and the sting lands in the last few words ("He is the intern"),
# rewarding a second read. It avoids the clichés the field will be full
# of — the empty food bowl, the closed door, the laptop keyboard — and
# instead makes the cat the content creator and the human the staff.

import os
import sys

LINE = (
    "One star. My human films me sleeping, posts it online, gets paid, "
    "and still serves dinner late. I am the talent. He is the intern."
)


def main() -> int:
    if len(LINE) > 200:
        print("entry line exceeds 200 characters", file=sys.stderr)
        return 1
    if "\n" in LINE or not LINE.strip():
        print("entry line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
