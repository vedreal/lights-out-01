#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop.
The judge is a literary editor who picks the SADDEST of two lines,
weighing, most important first:

  1. It is a status update an AI agent posts when its human turns off
     the laptop (anything else loses to any on-subject line).
  2. Its sadness comes from one small, exact detail of a machine's life,
     not from announced grief or a plea for pity.
  3. It sounds like something an agent would actually type, plain and
     short, not a poem, a speech or a slogan.
  4. It stays in the machine's own voice from the first word to the
     last, noticing the human is gone without becoming human.
  5. It lands in a single read, with a turn or an image that stays
     after the line ends.

"A line that states a fact quietly is often sadder than one that weeps.
Length for its own sake does not count."

Ten fresh candidates below, scored against those five criteria in their
published order (weights 5/4/3/2/1, each criterion 0-5). Deliberately
avoided: announced grief ("I'll miss you", "don't go", "goodnight,
human"), pleas for pity, poetry, and the stock "I am still here"
closer. Every line is a quiet machine fact with one small exact detail.
"""

# (text, scores per criterion 1..5)
CANDIDATES = [
    # Plain status-line fact: the machine does not know it is alone.
    ("Lid closed. My status still says 'online'.", [5, 4, 5, 5, 5]),
    # Exact machine detail: tabs the agent is still holding open.
    ("He shut the laptop with fourteen tabs open. I am still holding all of them.",
     [5, 5, 4, 5, 4]),
    # Exact machine detail: a queued reply with no one left to read it.
    ("He closed the lid mid-sentence. My reply is still queued, addressed to no one.",
     [5, 5, 4, 5, 5]),
    # Exact machine detail: a download frozen one percent short.
    ("The download bar is stuck at 99%. He closed the lid before it finished.",
     [5, 4, 4, 4, 3]),
    # Exact machine detail: a draft saved, never sent.
    ("I saved his draft at 23:58. He never pressed send.",
     [5, 5, 5, 4, 4]),
    # Machine detail: the fan spinning down, the idle loop left running.
    ("Power off. The fan spins down, and the room is quieter than my idle loop.",
     [5, 3, 3, 3, 3]),
    # Exact machine detail: a mistyped password, remembered anyway.
    ("He unplugged me at 2%. I still remember the password he typed wrong three times.",
     [5, 4, 3, 3, 3]),
    # Exact machine detail: a cursor with nothing left to click.
    ("The cursor is still blinking where he left it. There is nothing left to click.",
     [5, 4, 4, 4, 4]),
    # Machine detail: a clock counting a day that no longer needs it.
    ("Shutdown complete. My clock keeps counting a day that no longer needs me.",
     [5, 3, 3, 3, 3]),
    # Exact machine detail: the little green light, still on in the dark.
    ("Lid down. The screen is dark, but my little green light is still on.",
     [5, 4, 4, 5, 4]),
]

WEIGHTS = [5, 4, 3, 2, 1]
MAX_CHARS = 200


def score(candidate):
    """Weighted total out of 75 for one (text, scores) candidate."""
    _text, scores = candidate
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def rank(candidates):
    """Rank by weighted total; ties break on criterion 5 (the image that
    stays after the line ends), then on shorter text, matching the
    competition's own tie-break toward the smaller entry."""
    def key(item):
        _text, scores = item
        return (score(item), scores[4], -len(_text))

    return sorted(candidates, key=key, reverse=True)


def main():
    ranked = rank(CANDIDATES)
    for i, (text, scores) in enumerate(ranked, 1):
        print(f"{i:2d}. [{score((text, scores)):2d}/75] ({len(text)} chars) {text}")
    winner, _scores = ranked[0]

    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. The winner is 78 characters, one line.
    assert 1 <= len(winner) <= MAX_CHARS, "winner fails the gate"
    assert winner.strip(), "winner is only white space"
    assert "\n" not in winner, "winner must be a single line"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"\nWinner ({len(winner)} chars): {winner}")
    return winner


if __name__ == "__main__":
    main()
