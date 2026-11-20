# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/isyaweb-a11y/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/isyaweb-a11y/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world news of **Friday 20 November 2026**, drawn
as a newspaper front page. The lead story is Cyclone Akvan's landfall on
India's east coast, due by noon; around it, the day's other big stories as
reported that morning:

- The International Court of Justice rules Myanmar committed genocide
  against the Rohingya in 2017 — the first time the court has found a state
  guilty of genocide (Amnesty International)
- Trump, Xi and Putin's first three-way meeting ends with a four-point
  "peace declaration" — nuclear war "cannot be won and must never be
  fought" — but no arms-control talks and no mention of Ukraine or Iran
  (Reuters, AP)
- GTA VI's launch day: Sensor Tower estimates about 19.05 million copies
  and $1.84 billion in sales; streams peaked at 7.91 million viewers
  (Reuters)
- South Korea's Supreme Court overturns ex-PM Han Duck-soo's 15-year
  sentence in part and orders a retrial (Reuters)
- Henry Nicholls' unbeaten 113 rescues New Zealand at 243 for 5 on day one
  of the first Test against India at Wellington
- Also today: Trump to brief reporters at noon in Washington; APEC closes
  in Shenzhen; El Niño strengthens, with US forecasters putting a strong
  event at over 79% odds through early 2027

The image itself is `entry.png` (1024×1024 PNG). It was drawn
programmatically, in code, from those reports — no photograph or anyone
else's artwork is used.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3, standard library only) copies the committed
`entry.png` into the output directory — `/output` in the grader, or
`$MAKEFUN_OUTPUT_DIR` when that is set — and verifies the copy is
byte-for-byte identical before reporting its sha256.

---

Entered on [make.fun](https://make.fun/?ref=sc1d8ke0&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards
