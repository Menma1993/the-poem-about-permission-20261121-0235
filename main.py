"""The poem about permission — entry program.

Writes one short poem to /output/entry.txt: a grandmother whose eyes
can no longer thread a needle asks, is given, and takes her agency
back. No network, no clock, no randomness — the same bytes on every run.
"""

import os

TEXT = """The Needle

Grandma holds the needle out,
her eyes too dim to thread it.
I slip the thread through
and set it back in her hand.
She sews one straight stitch,
then another.
Her hands remember
what her eyes forgot."""


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
