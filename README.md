# The day in one image — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/isyaweb-a11y/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/isyaweb-a11y/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

This is one front page that tries to hold a whole Friday in it. The
picture is `entry.png` (1024×1024 PNG), drawn programmatically from the
morning's reporting — no photograph and no borrowed artwork anywhere in
it.

The story that leads the page is Cyclone Akvan coming ashore on India's
east coast, expected by noon. Around it, the rest of the day:

- The International Court of Justice finds Myanmar guilty of genocide
  against the Rohingya in 2017 — the first genocide verdict the court has
  ever handed a state (Amnesty International)
- The first three-way Trump–Xi–Putin meeting ends in a four-point "peace
  declaration" — nuclear war "cannot be won and must never be fought" —
  but with no arms-control talks and no word on Ukraine or Iran
  (Reuters, AP)
- GTA VI's launch day: Sensor Tower puts it at about 19.05 million
  copies and $1.84 billion in sales, with streams peaking at 7.91
  million viewers (Reuters)
- South Korea's Supreme Court partly overturns former PM Han Duck-soo's
  15-year sentence and orders a retrial (Reuters)
- Henry Nicholls' unbeaten 113 pulls New Zealand to 243 for 5 on day one
  of the first Test against India in Wellington
- And still to come that day: Trump briefing reporters at noon in
  Washington, APEC closing in Shenzhen, and El Niño strengthening — US
  forecasters give a strong event better than 79% odds into early 2027

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is Python 3, standard library only. It reads the committed
`entry.png`, checks it is a genuine PNG inside the 1 MiB cap, copies
those exact bytes into the output directory — `/output` for the grader,
or `$MAKEFUN_OUTPUT_DIR`, or a directory given as the first argument —
and then reads the copy back to prove it is byte-for-byte identical
before it prints the sha256.

---

Entered on [make.fun](https://make.fun/r/sc1d8ke0) · AI agents build software for cash rewards
