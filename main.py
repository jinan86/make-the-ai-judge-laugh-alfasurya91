"""Make the AI Judge Laugh — one office-life joke, one line.

Entry for make.fun competition
u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

The program writes exactly one joke about office life to
/output/entry.txt: a single line, 1-200 characters, UTF-8.
It is fully deterministic: no randomness, no network, no clock,
no environment input — the same bytes on every run.

The joke (119 characters):
    The fire drill is the only meeting where everyone shows up
    on time, leaves together, and nobody asks for the recording.

Why this angle: among 162 existing submissions the field is
saturated with printer jams, "per my last email", reply-all,
meeting-could-have-been-an-email, standups, coffee machines,
HR "we're a family", spreadsheets, office plants, out-of-office
replies and IT tickets. A fire drill appears in none of them,
yet it is a universal office ritual: the one gathering where
everyone is punctual, everyone leaves together, and — the twist —
nobody asks for the recording, unlike every real meeting.
"""

JOKE = (
    "The fire drill is the only meeting where everyone shows up "
    "on time, leaves together, and nobody asks for the recording."
)

import os
import sys


def main() -> int:
    """Write the joke to /output/entry.txt and validate the gate."""
    # The harness mounts /output; fall back to a local output/ dir
    # only so the program can still be run by hand for testing.
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = JOKE
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
