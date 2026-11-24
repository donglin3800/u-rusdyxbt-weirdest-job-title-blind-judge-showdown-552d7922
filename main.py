#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

The entry is one job title, 39 characters: a piano tuner is a real job,
underwater is an impossible workplace, and cruise ships are a real
employer. The joke lands because the title reads like a genuine posting
until the second word.

The program writes exactly that title to entry.txt under the output
directory the grader provides, with no trailing newline inside the
title itself. Fixed text, no network, no clock, no randomness, so
every run writes identical bytes.
"""

import os
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Entry:
    text: str
    limit: int = 60

    def validate(self) -> None:
        if not self.text or not self.text.strip():
            raise ValueError("job title is empty")
        if len(self.text) != len(self.text.strip()):
            raise ValueError("job title has surrounding whitespace")
        if "  " in self.text:
            raise ValueError("job title has a double space")
        if len(self.text) > self.limit:
            raise ValueError(
                f"job title is {len(self.text)} chars, limit is {self.limit}"
            )
        if "\n" in self.text or "\r" in self.text:
            raise ValueError("job title must be a single line")

    def render(self) -> bytes:
        self.validate()
        return self.text.encode("utf-8")


TITLE = Entry(text="Underwater Piano Tuner for Cruise Ships")


def output_file() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main() -> int:
    target = output_file()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(TITLE.render())
    sys.stdout.write(TITLE.text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
