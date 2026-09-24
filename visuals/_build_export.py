#!/usr/bin/env python3
"""Assemble every deliverable and source document into one exportable markdown file."""
import os, re, datetime

BASE = '/home/user/claude-stuff'
OUT  = os.path.join(BASE, 'ABYSSAL-NETWORK-APPLICATION-FULL-EXPORT.md')

def read(rel):
    with open(os.path.join(BASE, rel)) as f:
        return f.read().rstrip()

def demote(md, levels=1):
    """Push every heading down N levels so the combined doc nests correctly."""
    out = []
    fence = False
    for line in md.split('\n'):
        if line.lstrip().startswith('```'):
            fence = not fence
        if not fence and re.match(r'^#{1,6} ', line):
            line = '#' * levels + line
        out.append(line)
    return '\n'.join(out)

# ---------- slide index ----------
SLIDES = [
 ("the-collapse.png","Q1","Peak to now — AD1 −93%, AO −90%, AD2 −78%, same measure and scale."),
 ("the-volume-question.png","Q1","Uploads vs views scatter, 61 channel-months, coloured by year. Shows the time confound."),
 ("curiosity-to-close.png","Q1","Early topics vs recent topics. Why Fishing Encounters did 65K."),
 ("the-35-case-trap.png","Q1","The arithmetic that makes the runtime pick the topics. The 'protecting for the wrong reasons' answer."),
 ("sequel-decay.png","Q1","Seven multi-volume series, −50% to −96%, averaging −85%. Plus the one that grew."),
 ("the-eight-video-cliff.png","Q1","Total monthly views by exact upload count. 7 → 3.01M, 8 → 1.09M."),
 ("convergence.png","Q1","494K / 274K / 123K subscribers → 138K / 127K / 110K views. Two panels, not one axis."),
 ("the-ask.png","Q1","~17 hrs/month asked vs Chilling Scares' 1.1. Plus 59 min against the ~28 min outlier band."),
 ("per-channel.png","Q1","AO / AD / AD2 in the order the brief asks for them."),
 ("five-changes.png","Q1","The five recommendations with the evidence for each."),
 ("next-format.png","Q1","The one-case format as a hypothesis to test, with its risk stated."),
 ("five-invariants.png","Q2","The premise doc's five, with the third argued as the product."),
 ("the-document-axis.png","Q2","Every segment ends on the paperwork — and why defining the level that way fails."),
 ("pitch-collapses.png","Q2","AD — Structural Collapses. 44 cases, 55 min. The engineering report."),
 ("pitch-lifts.png","Q2","AD2 — Lift & Cable Failures. 40 cases, 48 min. The inspection certificate."),
 ("pitch-casting.png","Q2","AO — Reality TV Casting. 42 cases, 50 min. The background check."),
]

today = datetime.date.today().strftime('%d %B %Y')

parts = []
A = parts.append

A(f"""# Abyssal Network — Creative Strategist Application
## Complete export

*Assembled {today}. Everything produced for this application, plus the source documents it was
built against and the log of every conclusion that was reversed along the way.*

**The deliverable is Part 3** — the Loom script. Parts 4 to 6 are the working that backs it.

---

## Contents

1. **The brief** — job description and Core Premise doc, as supplied
2. **Decision log** — every reversal, in order
3. **The script** — the ~24 minute Loom answer *(the deliverable)*
4. **The visuals** — 16 slides, what each one carries
5. **Fact-check log** — every correction with its primary source
6. **JD alignment audit** — the work checked against the brief
7. **Appendix** — channel data, superseded files, how the visuals were built

---

## The short version

**Q1.** The network isn't failing because the format aged. It's failing because the
**35–50 case, 45–60 minute requirement quietly took over topic selection**. To fill fifty filmed
segments you need a topic broad enough that nobody has pre-existing morbid curiosity about it —
which is how a slate that once ran *CCTV Incidents* at 3.17M ended up running *Fishing
Encounters* at 65K. Two comfortable explanations were tested and discarded: titles (a constant
through the peak) and volume (confounded with time).

**Q2.** Topic-level novelty is unwinnable — Kitchen Nightmares, child stars, India and Telegram
were all tested and all already carry multi-million-view videos. So rather than three new topics,
one change applied where it fits: **every segment ends on the document.** The inspection that was
failed, the report that was filed, the background check that was run and ignored. Levels still
escalate on harm; the paperwork is the signature of every case.

| Channel | Pitch | The document | Cases | Runtime |
|---|---|---|---|---|
| Abyssal Detective | Structural Collapses | the engineering report | 44 | 55 min |
| Abyssal Detective 2 | Lift & Cable Failures | the inspection certificate | 40 | 48 min |
| Abyssal Observer | Reality TV Casting | the background check | 42 | 50 min |

**Four conclusions in this work were reversed after being written down.** All four are spoken
aloud in the script rather than quietly patched, because the brief says a retention curve should
be able to prove you wrong.

---
---

# Part 1 — The brief

Both documents are reproduced as supplied. Everything in Parts 2 to 6 is checked against them.

---
""")

A(demote(read('source-documents/job-description.md'), 1))
A("\n---\n")
A(demote(read('source-documents/core-premise.md'), 1))

A("""
---
---

# Part 2 — Decision log

---
""")
A(demote(read('decision-log.md'), 1))

A("""
---
---

# Part 3 — The script

*This is the deliverable. `[SLIDE: x.png]` cues the visual listed in Part 4. Roughly 24 minutes
spoken.*

---
""")
A(demote(read('presentation-script.md'), 1))

A("""
---
---

# Part 4 — The visuals

16 PNGs at 3200×1800, in `visuals/`. Each is cued by name in the script. They are designed as a
backdrop to talk over, not as a document — one chart or one idea per slide, minimal text.

The colour palette was validated for colour-vision separation and contrast against the dark
surface before anything was drawn (`#e66767` decline, `#3987e5` neutral, `#199e70` positive on
`#1a1a19`). `visuals/_source.html` regenerates all sixteen.

| # | File | Part | What it carries |
|---|---|---|---|""")
for i, (fn, part, desc) in enumerate(SLIDES, 1):
    A(f"| {i} | `{fn}` | {part} | {desc} |")

A("""
---
---

# Part 5 — Fact-check log

*Every factual correction, with the primary source. Open this if a number is challenged.*

---
""")
A(demote(read('fact-check-corrections.md'), 1))

A("""
---
---

# Part 6 — JD alignment audit

*The work checked against the job description (Part 1) and then against the Core Premise doc.
Part 2 of this audit corrects three of its own Part 1 findings.*

---
""")
A(demote(read('jd-alignment-audit.md'), 1))

A("""
---
---

# Part 7 — Appendix

## The load-bearing numbers

**Peak → now**

| Channel | Peak | Now (Sep 2026) | Change |
|---|---|---|---|
| Abyssal Detective | 2,035,346 (Mar 2025) | 138,757 | **−93%** |
| Abyssal Observer | 1,390,590 (Feb 2026) | 141,082 | **−90%** |
| Abyssal Detective 2 | 601,402 (Oct 2025) | 133,382 | **−78%** |

**Convergence** — 494K / 274K / 123K subscribers → **138K / 127K / 110K** average views.

**The 8-video cliff, 2026 totals per month** — 4 → 1.12M · 5 → 1.29M · 6 → 2.07M ·
**7 → 3.01M** · **8 → 1.09M**. Per-video at seven: 429K. At eight: **136K**.

**Volume caveat** — r = −0.21 all-time, **−0.13 in 2026**. 2026 per-video: ≤5/mo 284,952 vs
≥7/mo 282,666. 2026 totals: ≤5/mo 1.22M vs ≥7/mo **2.05M**.

**Sequel decay** — seven series, −50% to −96%, averaging **−85%**. Exception: *Things on Asian
Internet*, **+94%** (602K → 1.17M).

**Titles** — 321 of 328 audited = **98%**. The one exception, *4chan Threads That Triggered FBI
Investigations*, did **407,000** — about 3× the current average.

**Topic collapse** — Footage Caught on Camera 4.03M · CCTV 3.17M · Internet Mysteries 2.2M →
Amazon Incidents 71K · Fishing Encounters 65K · Biblical Horrors 60K · Chinese Shows 54K.

**Duration** — AD 59 min · AO 57 · AD2 48 · outlier sweet spot **~28 min**. Monthly ask **~17
hrs** against Chilling Scares' 1.1.

**Abyssal Observer** — $7.72 RPM, ~$26,700/mo. Named shows **777,580** vs generic **49,930** =
**15.6×**. (TLC 1.44M · To Catch a Predator 954K · Intervention 631K · My Strange Addiction 614K ·
90 Day Fiancé 528K | Marvel 39.5K · Anime 45.6K · Chinese Shows 54.4K · Directors 60.2K.)

**AD2 transition** — recent half **55%** on-territory vs **28%** early; `Vol. N` numbering
**80% → 25%**.

**Format spec** — 7 levels · 5–7 cases per level · **35–50 cases** · 45–60 min · 60–120 s per
case · **30+ seconds of usable footage per case** · no true crime without a footage anchor.

**Channel IDs** — AD1 `UCnBbQHNiSYbLqH8nybUSH8Q` · AD2 `UCT4AXeTk6x2j1085ZaKargg` ·
AO `UCNT9_G9lMgToVfKoLJwn-Dw`. Totals: 137 + 80 + 113 = **330 videos**.

## Files in the repository

**Current — use these**

| File | What it is |
|---|---|
| `presentation-script.md` | The script. Part 3 above. |
| `visuals/*.png` | 16 slides. Part 4 above. |
| `visuals/_source.html` | Regenerates all 16 slides. |
| `decision-log.md` | Part 2 above. |
| `fact-check-corrections.md` | Part 5 above. |
| `jd-alignment-audit.md` | Part 6 above. |
| `source-documents/` | The JD and Core Premise as supplied. |
| `README.md` | Repository index. |

**Superseded — do not quote from these.** Kept for the raw channel data only. Each contains at
least one claim later disproven; see Part 2 for which.

`where-are-we-failing-brand-analysis.md` · `where-are-we-failing-synthesis.md` (contains the
impossible "351 out of 328") · `network-failure-diagnosis.md` · `abyssal-detective-analysis.md` ·
`abyssal-detective-2-analysis.md` (recommends merging channels — violates the tactical-only
constraint) · `abyssal-observer-analysis.md` · `competitive-benchmarking-analysis.md` ·
`chilling-scares-analysis.md` · `pitch-1-abyssal-detective.md` (Hotels — dead) ·
`pitch-2-abyssal-detective-2.md` · `pitch-3-abyssal-observer.md` · `full-chat-log.md` (its
summary of the JD is a paraphrase, not the JD).

## How the analysis was done

Channel data came from the applicant's own CSV exports of all three channels plus YouTube's
public figures, reconciled month by month. The cadence analysis recomputes Pearson correlations
across 61 channel-months and re-runs them restricted to 2026 to control for time. Novelty checks
ran against the full 330-video topic inventory and then against YouTube search per topic. External
facts were verified against primary reporting, court records and regulatory sources — every one
is cited in Part 5.

Where a number could not be verified, it was cut rather than softened. Where a conclusion was
contradicted by its own data, the reversal was kept in the script rather than removed.
""")

with open(OUT, 'w') as f:
    f.write('\n'.join(parts) + '\n')

words = len(open(OUT).read().split())
print(f"wrote {OUT}")
print(f"{os.path.getsize(OUT):,} bytes · ~{words:,} words")
