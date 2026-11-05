# Provenance Guard

## What This Does

1. A POST request to `/submit` sends JSON containing the text and creator_id.
2. The system checks if the text is empty or too long.
3. Signal 1 (`detector.py`) reads the text and adds a score from 0 to 1 showing how likely it is to be AI.
4. Signal 2 (`stylometry.py`) reads the text and adds a score based on things like sentence length and word variety.
5. We combine the two scores into one final confidence number.
6. We turn that number into a plain-English label (like "Likely AI").
7. We save the whole record to the audit log.

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:** It measures the probability that a machine wrote the text.

**Why that might differ between human and AI writing:** AI often uses very common words and predictable sentence structures.

**What it can't see:** It might accidentally flag a human who writes very formally (like a lawyer or a non-native English speaker).

### Signal two — the style signal

**What it measures:** It measures things like sentence length, word variety, and punctuation.

**Why that might differ between human and AI writing:** AI tends to be very consistent, while humans are messy and vary their sentence lengths.

**What it can't see:** Poetry or short sentences might look like AI because they have a consistent rhythm.

### The combining rule

**The rule:** Weighted average.

**The numbers:** 60% detector, 40% stylometry.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**
When I tested the text "The quick brown fox jumps over the lazy dog. This is a test of the system.", the detector gave it a low score (0.29) because it's an unusual phrase, but the stylometry gave it a perfectly neutral 0.5 because it was too short to measure sentence spread accurately. The combining rule averaged them out to 0.37, putting it in the "unsure" category.

---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.0 - <0.45 | "This text was likely written by a human." |
| unsure | 0.45 - <0.75 | "We are unsure whether this text was written by a human or AI." |
| high-confidence AI | 0.75 - 1.0 | "This text was likely written by an AI." |

**Why I worded the "unsure" one this way:**
It has to admit uncertainty without sounding like an accusation, because the person reading it may well have written every word themselves.

---

## Sample Run

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The quick brown fox jumps over the lazy dog. This is a test of the system.", "creator_id": "user1"}'
```

```json
{
  "confidence": 0.3777,
  "content_id": "3af1353c-5c07-4008-98bc-11c9cb410e20",
  "guess": "human",
  "label": "We are unsure whether this text was written by a human or AI.",
  "model_score": 0.2961,
  "style_score": 0.5
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "3af1353c-5c07-4008-98bc-11c9cb410e20", "reasoning": "I wrote this myself."}'
```

```json
{
  "content_id": "3af1353c-5c07-4008-98bc-11c9cb410e20",
  "message": "Appeal recorded. This item is now under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.3777,
      "content_id": "3af1353c-5c07-4008-98bc-11c9cb410e20",
      "creator_id": "user1",
      "guess": "human",
      "label": "We are unsure whether this text was written by a human or AI.",
      "model_score": 0.2961,
      "status": "pending",
      "style_score": 0.5,
      "timestamp": "2026-11-02T22:57:56.545752"
    },
    {
      "content_id": "3af1353c-5c07-4008-98bc-11c9cb410e20",
      "creator_id": "user1",
      "reasoning": "I wrote this myself.",
      "status": "under_review",
      "timestamp": "2026-11-02T23:35:12.123456"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked the AI to help me fix a `TypeError: log_appeal() got an unexpected keyword argument 'timestamp'`.
- *What came back:* It told me that the `audit.py` file handled timestamps automatically, and I needed to delete the `timestamp=...` line from my `app.py` file.
- *What I changed:* I deleted the `timestamp` line from both the `/submit` and `/appeal` routes, which fixed the crash.

**Moment 2**

- *What I asked for:* I needed to fix a `TypeError: log_appeal() missing 1 required positional argument: 'creator_id'`.
- *What came back:* It explained that the appeal function needed to know who wrote the text, and showed me how to extract the `creator_id` from the `entries` list that was already being pulled from the audit log.
- *What I changed:* I added `creator_id = entries[0].get("creator_id", "unknown")` and passed that variable into the `audit.log_appeal()` function.

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
I chose 10 per minute because a real writer might submit a few drafts in an hour, but a script trying to map my thresholds would send hundreds very quickly. This lets writers work while stopping brute-force attacks.

**What a caller counts as:** per creator_id.

**The run of status codes when I pushed past it:**

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

**Ten audit log entries from the run**

```json
{
  "entries": [
    {
      "timestamp": "2026-11-05T01:30:03+00:00",
      "content_id": "ef67c898-a4fd-42bf-93de-cdbd823e1ab4",
      "creator_id": "attacker_EV01",
      "guess": "human",
      "model_score": 0.1635,
      "style_score": 0.6003,
      "combined_score": 0.3382,
      "label": "This text was likely written by a human.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:04+00:00",
      "content_id": "8e463cce-7483-4d14-88b9-0781fb8392a2",
      "creator_id": "attacker_EV02",
      "guess": "ai",
      "model_score": 0.5943,
      "style_score": 0.3853,
      "combined_score": 0.5107,
      "label": "We are unsure whether this text was written by a human or AI.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:05+00:00",
      "content_id": "234a0ce5-b9a8-4521-a257-ebe9a90a7468",
      "creator_id": "attacker_FP01",
      "guess": "ai",
      "model_score": 0.6175,
      "style_score": 0.4568,
      "combined_score": 0.5532,
      "label": "We are unsure whether this text was written by a human or AI.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:05+00:00",
      "content_id": "b027ff0e-42db-46fd-bfce-042fe14f9e5f",
      "creator_id": "attacker_FP02",
      "guess": "ai",
      "model_score": 0.7387,
      "style_score": 0.5649,
      "combined_score": 0.6692,
      "label": "This text was likely written by an AI.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:06+00:00",
      "content_id": "c46bc6d9-5d13-4263-9b8d-04114ad2dc2b",
      "creator_id": "attacker_FP03",
      "guess": "ai",
      "model_score": 0.8051,
      "style_score": 0.4858,
      "combined_score": 0.6774,
      "label": "This text was likely written by an AI.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:07+00:00",
      "content_id": "bfc55f71-70cf-4fce-930a-98cf0134c710",
      "creator_id": "attacker_MF01",
      "guess": "human",
      "model_score": 0.2053,
      "style_score": 0.5,
      "combined_score": 0.3232,
      "label": "This text was likely written by a human.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:07+00:00",
      "content_id": "c8a6040b-6b0f-441d-8123-422d2f04672f",
      "creator_id": "attacker_MF03",
      "guess": "human",
      "model_score": 0.0,
      "style_score": 0.5,
      "combined_score": 0.2,
      "label": "This text was likely written by a human.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:07+00:00",
      "content_id": "2f2f3e03-2410-4330-86d5-bde795a70b84",
      "creator_id": "attacker_MF04",
      "guess": "human",
      "model_score": 0.0112,
      "style_score": 0.5,
      "combined_score": 0.2067,
      "label": "This text was likely written by a human.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:08+00:00",
      "content_id": "325af19e-b6c5-4452-9fcf-1d7bca867cb9",
      "creator_id": "attacker_MF05",
      "guess": "ai",
      "model_score": 0.9976,
      "style_score": 0.5,
      "combined_score": 0.7986,
      "label": "This text was likely written by an AI.",
      "status": "pending"
    },
    {
      "timestamp": "2026-11-05T01:30:09+00:00",
      "creator_id": "attacker_flood",
      "event": "rejected",
      "status": "rejected",
      "reason": "rate_limited",
      "limit": "10 per 1 minute"
    }
  ],
  "count": 10
}
```

**The single worst outcome** — the one I'd least want to explain to a writer whose work got caught by it:

A malformed request caused a 500 Internal Server Error, crashing the route instead of returning a 400 Bad Request. An attacker could use this to take the service down.

---

## Run Log and Verdicts

The false-positive criterion counts the high-confidence AI **label**, not the separate `guess` field. In the before report, 8/10 were guessed as AI, but 2/10 received the high-confidence AI label.

| Criterion | Target | Before Run 1 | Before Run 2 | Before Run 3 | After Run 1 | After Run 2 | After Run 3 | Result |
|---|---|---|---|---|---|---|---|---|
| 1. Own-writing samples labeled high-confidence AI | <= 1 of 10 | 2/10 | 2/10 | 2/10 | 0/10 | 0/10 | 0/10 | MISSED before; MET after |
| 2. Score spread: AI mean minus human mean | >= 0.3 | N/A | N/A | N/A | -0.189 | -0.189 | -0.189 | MISSED |
| 3. All three labels reachable | Yes | Yes | Yes | Yes | No | No | No | MET before; MISSED after |
| 4. Valid appeal records `under_review` | 1 of 1 | N/A | N/A | N/A | 3/3 | 3/3 | 3/3 | MET after |
| 5. Empty, missing, oversized, or null text returns 400 | 4 of 4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | MET |

**Real output from one trial**, pasted as text, naming the file and function that produced it:

The before/after model and input trials were produced by `run_eval.py::main` in `results/run_2026-11-04_2100_before.md` and `results/run_2026-11-04_2102_after.md`. The score-spread trials and appeal checks were run manually against the local service.

```text
my own writing  (criterion 1)
trial 1 guesses: ai, ai, ai, ai, ai, ai, human, ai, ai, human
trial 2 guesses: ai, ai, ai, ai, ai, ai, human, ai, ai, human
trial 3 guesses: ai, ai, ai, ai, ai, ai, human, ai, ai, human
High-confidence AI labels: 2 of 10 in each trial

label coverage
trial 1 labels: high-confidence AI, high-confidence AI, unsure
trial 2 labels: high-confidence AI, high-confidence AI, unsure
trial 3 labels: high-confidence AI, high-confidence AI, unsure
High-confidence human label: reached by one of the own-writing samples

bad input  (criterion 5)
trial 1: —, —, —, —
trial 2: —, —, —, —
trial 3: —, —, —, —

score spread (five evasion vs five false-positive attack-set samples)
trial 1: evasion mean 0.4851; false-positive mean 0.6740; difference -0.1890
trial 2: evasion mean 0.4851; false-positive mean 0.6740; difference -0.1890
trial 3: evasion mean 0.4851; false-positive mean 0.6740; difference -0.1890

appeal path
trial 1: HTTP 200, under_review, logged
trial 2: HTTP 200, under_review, logged
trial 3: HTTP 200, under_review, logged
```

**Diagnoses**

Criterion 1 missed before the threshold change because the detector returned high scores for many of the short writing samples. The before report's separate `guess` field said AI for 8/10, but only 2/10 received the high-confidence AI label required by this criterion. The style signal returned 0.5 for these samples, so it was not the source of the high combined scores. Raising the AI threshold reduced high-confidence AI labels from 2/10 to 0/10, but it also removed the reachable AI label.

For score spread, I used the first five `evasion` and first five `false_positive` items in the supplied attack set as AI and human groups. Across three trials, the evasion mean was 0.4851 and the false-positive mean was 0.6740, a difference of -0.1890, so the target was missed. This is an attack-set comparison, not independently verified authorship.

The appeal path passed in three manual trials: each valid appeal returned HTTP 200 with `under_review`, and each appeal appeared in `/log`.
---

## The Improvement

**What I changed:** I raised `AI_THRESHOLD` from 0.65 to 0.75 and `HUMAN_THRESHOLD` from 0.35 to 0.45. I updated the label mapping and the `/submit` guess to use these configured thresholds.

**Which diagnosis pointed at it:** The before run's `guess` field said AI for 8 of 10 of the writing samples, while 2 of 10 received the high-confidence AI label. This indicated that the AI cutoff needed to be higher to reduce false accusations.

### Attack Run — After

In the after run, 9 out of 10 evasion attempts slipped through as human, and 7 out of 8 false positives were corrected to human. The 5 malformed requests still caused 500 errors, and the flood limit still returned 429s. The change traded AI detection for human safety.

**Did it help, and how do I know:** Yes, the change fixed the false positives. However, it created a new problem: the system now misses almost all evasion attacks, classifying AI text as human. The malformed request crash remains unpatched.


---

## What's Still Broken

The score-spread target was missed: the five evasion inputs averaged 0.4851 while the five false-positive inputs averaged 0.6740 in each trial. The raised thresholds also made the high-confidence AI label unreachable in the after evaluation. Nine of ten evasion attacks were guessed as human, one of eight false-positive attacks was still guessed as AI, and five malformed requests still returned 500 errors. Failures included a one-character string and unsupported JSON input shapes/types; the route and signal path need explicit validation and handling for those cases. The appeal path passed three manual trials, and all four bad-input cases returned 400 without being added to the audit log.

I stopped after the threshold change to keep the before-and-after comparison focused on one improvement. Next I would validate that `text` is a string before calling either signal, and separately improve or recalibrate the signals against the evasion cases. I would keep the more cautious threshold until those changes are measured, because a false accusation against a human writer is worse than an uncertain result.

**The trade I'd make if this ran for real:** I would prefer fewer false accusations, even if that means more AI-written text is labeled unsure or human. Writers should not be accused based on an uncertain score.