"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (max 200 characters) to
/output/entry.txt, as the make.fun program/v1 harness requires.

Shortlist of variants, judged against the brief (daily gadget named,
funny on first read with a sting of recognition, fresh angle, neat
wording, one person's specific gripe with a concrete detail):

1. "My fitness app celebrated 10,000 steps on a day I only walked to
   the fridge fourteen times." -- tight, visual, concrete detail.
2. "My phone sends me a weekly screen-time report like a disappointed
   parent -- from the same device that kept me up until 3 a.m." --
   the accuser is the culprit; the twist lands last.
3. "Bluetooth finds my neighbour's speaker instantly and takes three
   minutes to find the headphones in my own hand." -- strong
   recognition, but a familiar pairing complaint.
4. "Face ID recognises me everywhere except first thing in the morning,
   when apparently I become a stranger in my own home." -- concrete,
   but the morning-face joke is well worn.
5. "My watch celebrates me for standing up, like sitting down all day
   was the achievement it trained me for." -- neat inversion, but the
   stand-reminder target is a common one.
"""

CANDIDATES = [
    "My fitness app celebrated 10,000 steps on a day I only walked to the fridge fourteen times.",
    "My phone sends me a weekly screen-time report like a disappointed parent \u2014 from the same device that kept me up until 3 a.m.",
    "Bluetooth finds my neighbour's speaker instantly and takes three minutes to find the headphones in my own hand.",
    "Face ID recognises me everywhere except first thing in the morning, when apparently I become a stranger in my own home.",
    "My watch celebrates me for standing up, like sitting down all day was the achievement it trained me for.",
]

# Final pick after comparison: variant 2 beats variant 1 on the judge's
# criteria 2 and 3. Variant 1 is tight and visual, but "fitness app
# praises trivial activity" is a known trope; variant 2's twist is
# stronger -- the device shaming you is the device that kept you up --
# and "disappointed parent" + "3 a.m." is the fresher, more specific
# gripe. Variant 1 stays in CANDIDATES as the runner-up.
ROAST = CANDIDATES[1]

MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise SystemExit("roast line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"roast line is {len(line)} chars, over the 200 limit")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
