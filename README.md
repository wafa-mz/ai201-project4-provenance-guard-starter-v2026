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
| high-confidence human | 0.0 - 0.35 | "This text was likely written by a human." |
| unsure | 0.35 - 0.65 | "We are unsure whether this text was written by a human or AI." |
| high-confidence AI | 0.65 - 1.0 | "This text was likely written by an AI." |

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

```

**The single worst outcome** — the one I'd least want to explain to a writer whose work got caught by it:


---

## Run Log and Verdicts

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. |  |  |  |  |  |
| 2. |  |  |  |  |  |
| 3. |  |  |  |  |  |
| 4. |  |  |  |  |  |
| 5. |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function that produced it:

```json

```

**Diagnoses**


---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

**Did it help, and how do I know:**


---

## What's Still Broken

**The trade I'd make if this ran for real:**
