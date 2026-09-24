# Decision Log

Every conclusion that was reached, tested, and then reversed — in order. This exists because
four separate things in this work turned out to be wrong, and the corrections are more useful
than the conclusions.

---

## Reversal 1 — Volume was never the cause

**What was claimed:** the network is over-producing and cannibalising itself. *"Every time
uploads increased, per-video views decreased."* Recommendation: cut from ~20 uploads/month to 12.

**What killed it:** recomputing across all 61 channel-months and controlling for time.

| Test | Result |
|---|---|
| Pooled correlation, cadence vs per-video views, all time | r = **−0.21** |
| Pooled correlation, **2026 only** | r = **−0.13** |
| Abyssal Observer, 2026 only | r = **+0.05** — *positive* |
| 2026 per-video views, ≤5 uploads/mo vs ≥7/mo | **284,952 vs 282,666** — identical |

The apparent effect was almost entirely confounded with time: early months were both low-cadence
and high-view. The specific figures quoted were also cherry-picked single months, not averages —
"4/month → over 1 million" against a real 4-upload-month average of **416,430**.

**Worse, the recommendation was backwards.** In 2026, months with ≥7 uploads earned **2.05M**
total views against **1.22M** for ≤5. Cutting output would have cut revenue.

**What survived:** breaking 2026 out by exact upload count shows **8 is the only tier where total
monthly views collapse** — 7 uploads earns 3.01M, 8 earns 1.09M. And the premise doc says each
channel uploads "about twice a week," which is eight. Their stated cadence is precisely the
breaking tier. The recommendation became *"cap at seven, never eight"* — smaller, sharper, and
actually true.

---

## Reversal 2 — Title monoculture cannot be the cause of a decline

**What was claimed:** 98% of titles use one formula, and this is *"the single most damaging
pattern."*

**What killed it:** the peak videos use the same formula. *Footage Caught on Camera* — 4.03M.
*CCTV Incidents* — 3.17M. Every one of the top thirteen is "the Most Disturbing [X] Iceberg." The
channel reached two million average views **with** 98% identical titles.

A constant cannot explain a change. Titles were demoted from cause to ceiling — still the
highest-leverage untested lever, and the one the JD explicitly gives the strategist, but not the
reason for the fall.

**What replaced it as the diagnosis:** the premise doc's own line — *"the viewer gets their
morbid curiosity closed just by sitting and watching."* A topic only works if there is
pre-existing curiosity to close. Early topics had it (CCTV, Footage Caught on Camera, Internet
Mysteries). Recent ones don't (Biblical Horrors 60K, Amazon Incidents 71K, Fishing Encounters
65K, Chinese Shows 54K). And the cause of *that* is the 35–50-case requirement: to fill fifty
filmed segments you need a topic broad enough that nobody is curious about it.

---

## Reversal 3 — "Zero results on YouTube" was false

**What was claimed:** all three pitch topics verified as novel across YouTube.

**What killed it:** re-running the searches properly.

| Topic | Claimed | Actual |
|---|---|---|
| Elevator & escalator | zero | ✅ held |
| Kitchen Nightmares | zero | ❌ three icebergs exist; ground held by Bartolozzi **3.93M** (3 months prior) and MermaidGrove **3.69M** |
| Hotels | zero | ❌ adjacent *Lost Locations Iceberg*, 1.28M |

Replacement candidates died the same way: **India** (icebergs at 307K and 175K), **Telegram**
(145K/188K Spanish, 646K Russian), **child stars** (Deep Dive 4.64M, Nick Crowley 4.41M, j aubrey
5.08M).

**The conclusion that matters:** topic-level novelty is effectively unwinnable. Almost every
subject with real morbid curiosity attached already carries a multi-million-view video. And Q2
asks how your version *"beats the original"* — which presupposes an original exists. Zero-results
was the wrong bar all along.

---

## Reversal 4 — The document axis, in its first form, fails arithmetic

**What was claimed:** make the *level* mean the document. L1 nobody knew → L7 it was in writing
and they signed it off anyway.

**What killed it:** the spec requires **5–7 cases at every tier, including the deepest**. "They
knew and did it anyway" is the rarest state there is. One Mottarone exists; six do not.

**Corrected form:** levels escalate on **harm**, which is abundant at every tier. The document
becomes the **signature of every segment** — every case ends on the paperwork — rather than the
definition of the level. Same obscurity benefit, same moral frame, and it fills.

**Same arithmetic killed Kitchen Nightmares a second time.** One show cannot fill seven levels;
it has one Cerniglia, not six.

---

## Things that were wrong and simply got fixed

| Claim | Correction |
|---|---|
| Amy Bouzaglo served time for "identity theft" | Used another person's **Social Security number** for a $15,000 credit line; 14 months federal; formerly Amanda Bossingham |
| "$500M–$1B nationwide hotel trafficking MDL" | **JPML denied consolidation, April 2024.** Replaced with verified judgments: Days Inn $24M (2023), Georgia $40M verdict (2025), $17.5M Philadelphia (2025) |
| Samuel Waisbren's elevator "had 16 violations" | Unverifiable. Actual: the **door-zone restrictor was disabled**, the building was fined **$1,300** in May 2019 for exactly that, and it was still unfixed on 22 Aug 2019 |
| Sequel decay "−75% across 54 videos" | **−85%** across the seven multi-volume series we have data for; the "54 videos" was a different population |
| "82% of Kitchen Nightmares restaurants closed" | Real but contested (competing counts of 79%, ~70%). Softened to "more than 80% by the most-cited count" |
| Dillons lawsuit presented without outcome | Martin Hyde, general manager, sued for $3M — **he lost, and the episode aired** |
| Joe Cerniglia framed causally | His family have publicly said the show was a good period in his life. Script presents the sequence and declines to assert cause |
| Video count 328 vs 330 | Title audit ran at 328 (AD1 136, AD2 80, AO 112); current total is 330. Both stated honestly |
| Monthly watch-time ask "18.3 hrs" | **~17 hrs** — 18.5 uploads at a weighted 54.8 min |
| Jingzhou "billions of impressions" | Unmeasurable. Cut |

---

## Structural corrections from reading the brief

The JD was never in the repo — earlier work ran on a paraphrase of it. Reading the real JD, and
then the Core Premise doc, corrected several things including some of the corrections.

- **AD2 does not lack an identity.** The premise doc gives it one: footage-format and setting led.
  And the data agrees — its recent half is **55% on-territory** against 28% early, with `Vol. N`
  numbering down from **80% to 25%**. It is mid-repositioning and executing it. The original
  "identity-less sequel dump" diagnosis contradicted both the brief and the data.
- **Disasters belong to AD, not AD2** — which meant the Hotels pitch was not mis-routed for the
  reason first given. It died instead on the footage-anchor rule: *"true crime with no footage
  anchor is rejected network-wide,"* and Hotels was mostly court records and stills.
- **"8 videos per month across three channels" means 8 per channel** — the premise doc says each
  channel uploads twice a week. This reversed an earlier finding that the "cap at 7"
  recommendation was 3× too high; it is in fact one notch below their stated cadence.
- **Two sub-questions were unanswered entirely:** what they are *"protecting for the wrong
  reasons,"* and *"what makes it an Abyssal video."* Both now answered.
- **Three named success metrics had no coverage:** Patreon conversion, monetization and
  advertiser-friendly handling, and retention at level transitions.
- **Q1 opened politely** despite the brief saying *"do not be polite. We are not looking for a
  fan."* Rewritten to open on the worst number.

---

## Final verification pass

Two assumptions were flagged as unverified on the near-final draft and then researched. **One
failed.**

- ❌ **Kitchen Nightmares health inspection files.** Restaurant inspection retention is typically
  **three years**; the series ran 2007–2014. The records are gone, and no secondary source
  systematically reports pre-filming scores. Fails the premise doc's own gate — *"every segment
  traces to a real source."*
- ⚠️ **Elevator footage supply is inverted.** The US sees ~30 elevator and escalator deaths a
  year, and **nearly half are maintenance workers in shafts** — almost never filmed. Footage is
  thickest at the shallow end and thinnest where the payoff lives. Topic widened to every machine
  under mandatory periodic inspection: elevators, escalators, funiculars, cable cars, ski lifts,
  mine hoists.
- ✅ **New anchor verified:** Stresa–Mottarone, 23 May 2021. Haulage cable snapped; the emergency
  brake never engaged because **a clamp had been fitted to hold it open**. The service manager
  admitted this had become routine practice to avoid downtime. 14 dead. Three arrested for
  manslaughter and intentional removal of accident precautions.

---

## One caution carried forward

**Do not cite Jamal Trulove.** He appears in coverage as a reality-TV contestant convicted of
murder, which would fit the AO pitch. That conviction was reportedly overturned on appeal and he
was acquitted at retrial. Left out of the pitch deliberately, and flagged here so it is not
picked up later from the same search results.
