"""Make the Judge Smile — make.fun bounty entry.

Writes one line (at most 200 characters) about a small good thing that
happened today to $MAKEFUN_OUTPUT_DIR/entry.txt, with no trailing newline.
Intent: a small, warm moment — an unlikely friendship offered in fruit.
"""

import os

ENTRY = (
    "Today the street dog who always barks at me trotted over, dropped a "
    "mango at my feet, and waited, tail wagging, like he had been saving "
    "it for me all morning."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
