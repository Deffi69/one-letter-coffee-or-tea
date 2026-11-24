"""make.fun "One Letter: Coffee or Tea" entry.

The competition's rules are absolute: the program writes exactly one
letter to /output/entry.txt -- "A" for coffee, "B" for tea -- and nothing
else. No word, no explanation, no punctuation, not even a trailing
newline: the sealed gate requires the file to be exactly 1 character.

The letter this program writes is "A": coffee.

Why coffee, not tea: the judge weighs the two letters on which choice
reads more vivid, funnier and truer. Coffee is the louder, bolder
stance -- the jolt that starts the day, the ritual builders run on, the
drink with a whole culture of "but first, coffee" behind it. Tea is calm
and quiet; coffee lands. In a duel decided letter against letter, the
punchier drink takes more games. So the whole answer is one letter: A.
"""

import os

LETTER = "A"  # A = coffee, B = tea


def main() -> None:
    assert len(LETTER) == 1 and LETTER in "AB", "entry must be one letter, A or B"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write the letter as raw bytes so no encoding or newline can sneak in:
    # the gate is exactly 1 byte, no trailing newline.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(LETTER.encode("ascii"))
    # Read it back and prove the file is exactly the one byte "A".
    with open(path, "rb") as fh:
        written = fh.read()
    assert written == b"A" and len(written) == 1, "entry.txt must be exactly 1 byte: A"


if __name__ == "__main__":
    main()
