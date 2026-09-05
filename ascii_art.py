#!/usr/bin/env python3
"""Print stylized ASCII art for 'stunning-goggles' using only the standard library."""

FONT = {
    "S": [
        ".####",
        "#....",
        ".###.",
        "....#",
        "####.",
    ],
    "T": [
        "#####",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
    ],
    "U": [
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        ".###.",
    ],
    "N": [
        "#...#",
        "##..#",
        "#.#.#",
        "#..##",
        "#...#",
    ],
    "I": [
        "#####",
        "..#..",
        "..#..",
        "..#..",
        "#####",
    ],
    "G": [
        ".###.",
        "#....",
        "#..##",
        "#...#",
        ".###.",
    ],
    "-": [
        ".....",
        ".....",
        "#####",
        ".....",
        ".....",
    ],
    "O": [
        ".###.",
        "#...#",
        "#...#",
        "#...#",
        ".###.",
    ],
    "L": [
        "#....",
        "#....",
        "#....",
        "#....",
        "#####",
    ],
    "E": [
        "#####",
        "#....",
        "###..",
        "#....",
        "#####",
    ],
    " ": [
        "...",
        "...",
        "...",
        "...",
        "...",
    ],
}

HEIGHT = 5


def render(text):
    """Return a multi-line ASCII art banner for text using FONT."""
    letters = text.upper()
    rows = [""] * HEIGHT
    for letter in letters:
        glyph = FONT.get(letter, FONT[" "])
        for i in range(HEIGHT):
            rows[i] += glyph[i] + " "
    return "\n".join(rows).replace(".", " ")


def main():
    print(render("stunning-goggles"))


if __name__ == "__main__":
    main()
