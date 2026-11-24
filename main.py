#!/usr/bin/env python3
"""One-line excuse: an AI agent explains a missed deadline.

The script produces /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set) holding a
single sentence, no more than 200 characters long.

The setup: the agent really did complete the report when it was due,
but the only copy lived in a sandbox that got erased at midnight —
and the erasure swallowed the agent's own recollection of having
written it. The humour comes from the second disappearance: the work
is gone, and so is any memory of doing it. Everything stays in the
agent's world — sandboxes, wipes, memory — rather than reaching for a
human excuse such as traffic or sleeping in.
"""

import os
import sys

LIMIT = 200

LINE = (
    "I finished your report on time. The sandbox holding it was wiped "
    "at midnight, along with my memory of writing it."
)


def abort(reason):
    """Report a problem on stderr and exit unsuccessfully."""
    print("error: " + reason, file=sys.stderr)
    sys.exit(1)


def check(text):
    """Reject anything that is not one short plain-ASCII line."""
    if text.strip() == "":
        abort("excuse is empty")
    if any(ch in text for ch in ("\n", "\r")):
        abort("excuse must be a single line")
    if len(text) > LIMIT:
        abort(
            "excuse is %d characters, over the %d limit" % (len(text), LIMIT)
        )
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        abort("excuse must be plain ASCII")


def destination():
    """Resolve where entry.txt should be written."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def run():
    check(LINE)
    target = destination()
    with open(target, "w", encoding="utf-8", newline="") as stream:
        stream.write(LINE)
    with open(target, "r", encoding="utf-8", newline="") as stream:
        saved = stream.read()
    if saved != LINE:
        abort("round-trip mismatch: file does not match the excuse")
    check(saved)
    print("wrote %d characters to %s" % (len(saved), target))


if __name__ == "__main__":
    run()
