# The World in One Day — Saturday 21 November 2026

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/chongphoshun/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/chongphoshun/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

Entry for the make.fun bounty **news-image-20261121**: sum up Saturday
21 November 2026's world news in one image.

The image is a newspaper front page — **37 stories across 9 regions,
all dated Saturday 21 November 2026**:

- **3 leads** — COP31 in record overtime in Antalya, Iran's claimed
  strikes on two US bases in Bahrain, and the M6.7 Peru quake.
- **12 mains** — Riyadh intercepts 3 Houthi missiles, BepiColombo enters
  Mercury orbit, Russia hits Kyiv again, Rutte in Warsaw, Mexico captures
  "El Chapo Isidro", Trump on the Shenzhen summit, the Gaza food-truck
  strike, Bitcoin's fall below $60,000, France's shrinking marches,
  Bolsonaro in ICU, the Nigeria boat toll, and the Manipur toxic-alcohol
  deaths.
- **A numbered world map** (pins 1–15), a **UTC timeline** strip (00:09 UTC
  Peru quake, 05:12 UTC aftershock, 18:24 UTC BepiColombo, late-Saturday
  COP31 text), a **BY THE NUMBERS** strip, and **22 more one-line
  briefs** — football results, an IG Metall strike call, Sudan
  displacement, Estonia's border shutdown, the Peru aftershock, and
  cricket in Wellington.
- **Date discipline, printed on the page**: a DATE CHECK line states every
  story happened or was first reported on 21 November 2026, and a LEFT OUT
  line names the big stories that belong to other days (the COP31 collapse
  on 22 Nov, South Korea's minister resigning on 22 Nov, GTA VI's $3.79bn
  sales announced 20 Nov, the Anthropic IPO debut on 19 Nov, and the
  Trump–Xi–Putin summit on 19 Nov).

## How it is built

`draw_20261121.py` renders `entry.png` (1024×1024) with Pillow from the
story data written in that file — no network, no clock, no randomness, so
every run writes the same bytes. `main.ts` (Node 22, standard library
only) checks the PNG is whole and 1024×1024 under the 1 MiB cap and
copies it to `/output/entry.png`.

```sh
python3 draw_20261121.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Every claim in the image is sourced in [SOURCES.md](SOURCES.md) — Reuters,
AP, BBC, AFP, UN, ESA, USGS, Xinhua and others. Claims that are disputed
are labelled CLAIM and attributed in the image itself.

## License

MIT — see [LICENSE](LICENSE).
