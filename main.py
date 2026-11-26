#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office -- make.fun entry.

The brief asks for a single out-of-office email auto-reply of at most
200 characters: painfully honest about the sender's absence, inbox or
enthusiasm, yet still polite enough that a manager would let it stand.
A house judge compares the replies two at a time, weighing honesty
first, then politeness, then the turn of phrase.

This program writes that one reply to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The reply is honest about three things at once: the sender is not
checking email while away, the inbox will be no smaller on return, and
nothing sitting in it has become more urgent for waiting. It stays
polite by promising a reply as soon as possible and thanking the reader
for their patience, and its turn of phrase -- "just as full when I'm
back, and no more urgent than it is now" -- says the uncomfortable
truth in one breath instead of dressing it up.

The reply (191 characters):

    I'm out of office and, honestly, not checking email -- my inbox
    will be just as full when I'm back, and no more urgent than it
    is now. I'll reply as soon as I can. Thank you for your patience.

Nothing else is written; there is no second draft. Running with
``--dry-run`` only validates the reply (1-200 characters, one line, no
leading or trailing whitespace) and writes nothing, so the entry can be
checked without side effects.
"""

import os
import sys

REPLY = (
    "I'm out of office and, honestly, not checking email \u2014 my inbox "
    "will be just as full when I'm back, and no more urgent than it is "
    "now. I'll reply as soon as I can. Thank you for your patience."
)

MAX_CHARS = 200


def validate(reply: str) -> None:
    """The gate only accepts one reply: 1-200 UTF-8 characters."""
    if not reply or len(reply) > MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters")
    if reply != reply.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in reply or "\r" in reply:
        raise ValueError("entry must be a single line")


def main(argv=None) -> int:
    """Validate the reply and write it, unless --dry-run only validates."""
    args = list(sys.argv[1:] if argv is None else argv)
    validate(REPLY)
    if "--dry-run" in args:
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(REPLY.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
