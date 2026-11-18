# The World in One Day — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/knownmyface/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/knownmyface/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image that sums up Tuesday 17 November 2026's world news, built as a
newspaper front page: **48 stories, 15 illustrated, six continents**.

The masthead names the day — TUESDAY 17 NOVEMBER 2026 — above three lead
photo panels (the burning gas tanker Tara Gas in the Strait of Hormuz, the
collapsed Kerch Bridge, and Trump landing in Manila), a labelled world map,
a "Day at a Glance" box with the day's key numbers, and a three-column story
grid grouped by region (Middle East & Africa, Europe & Asia-Pacific,
Americas & Global). Every headline and label is drawn in code, so the text
stays crisp; the three lead photos and the map are the only AI-generated
images, and the other illustrated stories use small flat pictograms drawn in
code (a chip, a gavel, a plane, a lock, a golf flag, and more).

## Stories (48)

Lead captions: US strikes Iran / tanker Tara Gas ablaze in Hormuz; Kerch
Bridge hit again; Trump lands in Manila for the Quad summit.

Grid — Middle East & Africa: "dirty bomb" plot claim; Houthi drones on the
Saudi pipeline; Gaza's winter rains worsen the crisis; West urges Israel to
open Gaza aid; Israel strikes south Lebanon; Houthis advance in Yemen;
Turkey seeks defence pacts; militia defies Baghdad deadline; Iran strikes
Bahrain; third US carrier reaches the Gulf; Iraq oil flows resume; UK
sanctions settlement builders; Ebola "out of control" in DR Congo; Guinea
gold-mine crackdown; IFC pledges $500M for Africa.

Grid — Europe & Asia-Pacific: Russia hits Kyiv bridges; Depardieu pleads
guilty; EU states plan a Rwanda returns hub; Equinor hit by cyberattack;
Russian drones over Moldova; tanker sinks in the Black Sea; Czech rail
crashes; assassination plot arrests; Berlin raids Hezbollah-linked group;
Zaporizhzhia toll rises to 40; Trump–Xi–Putin summit set; US closes chip
loophole; Japan scrambles jets; Pakistan cuts fuel prices.

Grid — Americas & Global: US loses measles status; NSA network goes down;
Epstein death "was murder"; Wall Street falls; C-130 destroyed, activist
charged; ethanol plant bomb plot; Tiger Woods returns; Waymo pulled from
freeways; California landfill blast; Florida floods, western storm; Nvidia
spy scandal; NatGeo Pictures of the Year; Apple outages resolved; Dubai
traffic drops 28%; Nigeria inflation eases.

All 48 stories happened or were first reported on 17 November 2026, as
reported by Reuters, AP, CNN, PAHO, the UN, Euronews and allAfrica. Nothing
is invented; claims that were unverified at the time (for example the
"dirty bomb" plot) are labelled as claims.

## How it is built

`render.py` draws the whole front page with Python PIL (DejaVu fonts) and
writes `entry.png` (1024x1024, under 1 MiB). `main.ts` is the entry program:
it copies `entry.png` into `MAKEFUN_OUTPUT_DIR` and validates it — PNG
magic bytes, IEND trailer, dimensions from the IHDR chunk (max 1024x1024),
and file size (max 1 MiB). It uses only the Node standard library, needs no
network, and writes identical bytes on every run.

## Run it

```sh
python3 render.py        # rebuild entry.png from the assets (optional)
mkdir -p out
MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/entry.png` is the entry image.

## License

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?ref=1d5x2a29&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
