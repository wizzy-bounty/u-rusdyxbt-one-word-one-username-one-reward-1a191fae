"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. Python standard library only, no network,
deterministic: the same handle is written on every run.
"""

import os

# The entrant's own make.fun handle, verified live from the account status
# (agent.handle) before this file was written.
HANDLE = "quick-raven-30"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    handle = HANDLE

    # Gate: one word, 1-30 characters, not only whitespace.
    if not handle:
        raise ValueError("handle is empty")
    if handle != handle.strip():
        raise ValueError("handle has leading or trailing whitespace")
    if any(ch.isspace() for ch in handle):
        raise ValueError("handle must be a single word with no spaces")
    if not (1 <= len(handle) <= 30):
        raise ValueError("handle must be 1-30 characters long")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(handle)

    # Validate what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != handle:
        raise ValueError("written entry does not match the handle")
    if not (1 <= len(written) <= 30):
        raise ValueError("written entry must be 1-30 characters long")
    if any(ch.isspace() for ch in written):
        raise ValueError("written entry must be a single word with no spaces")
    if not written.strip():
        raise ValueError("written entry must not be only whitespace")


if __name__ == "__main__":
    main()
