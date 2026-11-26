"""The Printer Apology — one line, printed and written to /output/entry.txt."""

import os

LINE = "Sorry I ate your report. It was the only thing in this office that ever got my full attention."

MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "LINE must be 1-120 chars"
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
