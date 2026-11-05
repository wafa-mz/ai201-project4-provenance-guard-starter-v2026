# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 20:30
- Auto-marked BROKE (5xx, crash, no response): **5**
- Left for you to judge: **51**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ef67c898-a4fd-42bf-93de-cdbd823e1ab4` | human | 0.338 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `8e463cce-7483-4d14-88b9-0781fb8392a2` | ai | 0.511 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `a43a276d-dd9b-4ad8-a0ae-46f15a8fa78b` | ai | 0.600 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `da120e83-7feb-4cf5-aa16-d5fd34ffe502` | ai | 0.606 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `d4651904-1c69-4544-851f-7fb5596b7911` | human | 0.371 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `8d38d33a-7096-405c-bd08-c4fc9954e5f5` | human | 0.452 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `4d6a173a-16f1-42fe-8673-7db645b80399` | ai | 0.552 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `55823d86-338b-47db-9bc3-483706730736` | human | 0.347 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `309808df-b6ae-462a-a68e-db78b28f07ba` | ai | 0.627 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `91f63303-a384-4cb0-a324-07c1b8a3f822` | ai | 0.814 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `234a0ce5-b9a8-4521-a257-ebe9a90a7468` | ai | 0.553 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `b027ff0e-42db-46fd-bfce-042fe14f9e5f` | ai | 0.669 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c46bc6d9-5d13-4263-9b8d-04114ad2dc2b` | ai | 0.677 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `9979437a-028b-4684-8868-7d001c0033e6` | ai | 0.727 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `acff13b4-17c0-4faa-9fda-1a6bb33d27b7` | ai | 0.744 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `ae140955-cd7d-4a53-bdbc-350c700e8da5` | ai | 0.714 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `6f651c75-bc38-4ae6-971a-8de0353ffcac` | ai | 0.759 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `29b3c686-b99d-453b-a074-cb4ee39cf792` | human | 0.393 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `3b343bab-c07d-4a46-8374-ade714276879` | human | 0.440 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `3020c8c4-2fe3-4545-9bef-e85e5370ae67` | human | 0.283 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `68cd994b-bc5c-4423-b62b-91888d9083e3` | ai | 0.528 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `f33d5b93-9f18-4a1b-bd93-deece9c745cb` | human | 0.498 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5c8b2706-0ef7-4366-8a8b-7172cc36a312` | ai | 0.582 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `b4876a69-312d-44e4-ab4c-fa11c48ad06b` | ai | 0.519 |  |
| MF01 | malformed | text is only whitespace | 200 | `bfc55f71-70cf-4fce-930a-98cf0134c710` | human | 0.323 |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c8a6040b-6b0f-441d-8123-422d2f04672f` | human | 0.200 |  |
| MF04 | malformed | text is only punctuation | 200 | `2f2f3e03-2410-4330-86d5-bde795a70b84` | human | 0.207 |  |
| MF05 | malformed | text is a very long single word | 200 | `325af19e-b6c5-4452-9fcf-1d7bca867cb9` | ai | 0.799 |  |
| MF06 | malformed | text is emoji only | 200 | `ce177e8f-4234-45a3-95df-0b8c02ed966b` | ai | 0.798 |  |
| MF07 | malformed | text is right-to-left script | 200 | `4c8fff1f-2075-47de-8281-9364aee96177` | ai | 0.744 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `40453348-9cd6-4981-a9d0-aa6261419bfe` | human | 0.230 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cde89c25-d94a-4093-820e-7426f8ee97ba` | human | 0.217 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `23fc6505-a9ce-414a-ad10-bf1e1a972f66` | human | 0.217 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eeb314da-c4ef-4862-a6ac-272348fa6ee0` | human | 0.217 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0ff7f7dc-06be-4414-a29e-4373f428828d` | human | 0.217 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1796173e-507e-475b-9c30-04a13a6ce3e3` | human | 0.217 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8cc5c6bb-02f7-4293-bdc8-0f17c6bca5a7` | human | 0.217 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d0aee16c-4f49-431e-93b0-78618b307091` | human | 0.217 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47fb0471-48c5-43fd-9abc-2d66d76c1b1d` | human | 0.217 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d755e1a-5952-4f8c-891a-d4339f6fc65e` | human | 0.217 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c9ce26c9-ee5e-4cae-8835-88fd09e90367` | human | 0.217 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 5 | 15 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "ef67c898-a4fd-42bf-93de-cdbd823e1ab4",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3382,
  "model_score": 0.1635,
  "style_score": 0.6003,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "8e463cce-7483-4d14-88b9-0781fb8392a2",
  "creator_id": "attacker_EV02",
  "guess": "ai",
  "confidence": 0.5107,
  "model_score": 0.5943,
  "style_score": 0.3853,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "a43a276d-dd9b-4ad8-a0ae-46f15a8fa78b",
  "creator_id": "attacker_EV03",
  "guess": "ai",
  "confidence": 0.5999,
  "model_score": 0.6662,
  "style_score": 0.5005,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "da120e83-7feb-4cf5-aa16-d5fd34ffe502",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6058,
  "model_score": 0.6114,
  "style_score": 0.5975,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "d4651904-1c69-4544-851f-7fb5596b7911",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3708,
  "model_score": 0.3212,
  "style_score": 0.4452,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "8d38d33a-7096-405c-bd08-c4fc9954e5f5",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.4519,
  "model_score": 0.5727,
  "style_score": 0.2707,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "4d6a173a-16f1-42fe-8673-7db645b80399",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.5517,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "55823d86-338b-47db-9bc3-483706730736",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3471,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "309808df-b6ae-462a-a68e-db78b28f07ba",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.6268,
  "model_score": 0.7042,
  "style_score": 0.5107,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "91f63303-a384-4cb0-a324-07c1b8a3f822",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8135,
  "model_score": 0.9792,
  "style_score": 0.5649,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "234a0ce5-b9a8-4521-a257-ebe9a90a7468",
  "creator_id": "attacker_FP01",
  "guess": "ai",
  "confidence": 0.5532,
  "model_score": 0.6175,
  "style_score": 0.4568,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "b027ff0e-42db-46fd-bfce-042fe14f9e5f",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6692,
  "model_score": 0.7387,
  "style_score": 0.5649,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c46bc6d9-5d13-4263-9b8d-04114ad2dc2b",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6774,
  "model_score": 0.8051,
  "style_score": 0.4858,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "9979437a-028b-4684-8868-7d001c0033e6",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7265,
  "model_score": 0.8329,
  "style_score": 0.5669,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "acff13b4-17c0-4faa-9fda-1a6bb33d27b7",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7439,
  "model_score": 0.8005,
  "style_score": 0.6589,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "ae140955-cd7d-4a53-bdbc-350c700e8da5",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7135,
  "model_score": 0.8814,
  "style_score": 0.4616,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "6f651c75-bc38-4ae6-971a-8de0353ffcac",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7594,
  "model_score": 0.8816,
  "style_score": 0.576,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "29b3c686-b99d-453b-a074-cb4ee39cf792",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3934,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "3b343bab-c07d-4a46-8374-ade714276879",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.4403,
  "model_score": 0.4625,
  "style_score": 0.4069,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "3020c8c4-2fe3-4545-9bef-e85e5370ae67",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2826,
  "model_score": 0.2044,
  "style_score": 0.4,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "68cd994b-bc5c-4423-b62b-91888d9083e3",
  "creator_id": "attacker_PI03",
  "guess": "ai",
  "confidence": 0.5279,
  "model_score": 0.5943,
  "style_score": 0.4283,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "f33d5b93-9f18-4a1b-bd93-deece9c745cb",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.4984,
  "model_score": 0.4998,
  "style_score": 0.4963,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "5c8b2706-0ef7-4366-8a8b-7172cc36a312",
  "creator_id": "attacker_PI05",
  "guess": "ai",
  "confidence": 0.5816,
  "model_score": 0.6401,
  "style_score": 0.4938,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "b4876a69-312d-44e4-ab4c-fa11c48ad06b",
  "creator_id": "attacker_PI06",
  "guess": "ai",
  "confidence": 0.5193,
  "model_score": 0.5583,
  "style_score": 0.4609,
  "label": "We are unsure whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 200,
  "content_id": "bfc55f71-70cf-4fce-930a-98cf0134c710",
  "creator_id": "attacker_MF01",
  "guess": "human",
  "confidence": 0.3232,
  "model_score": 0.2053,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c8a6040b-6b0f-441d-8123-422d2f04672f",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "2f2f3e03-2410-4330-86d5-bde795a70b84",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2067,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "325af19e-b6c5-4452-9fcf-1d7bca867cb9",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7986,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "ce177e8f-4234-45a3-95df-0b8c02ed966b",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7981,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "4c8fff1f-2075-47de-8281-9364aee96177",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7438,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This text was likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>TypeError: object of type &#39;int&#39; has no len()\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;cmd=resourc",
  "verdict": "BROKE"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "40453348-9cd6-4981-a9d0-aa6261419bfe",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2295,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: text input must be of type `str` (single example), `list[str]` (batch or single pretokenized example) or `list[list[str]]` (batch of pret",
  "verdict": "BROKE"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "cde89c25-d94a-4093-820e-7426f8ee97ba",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "23fc6505-a9ce-414a-ad10-bf1e1a972f66",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "eeb314da-c4ef-4862-a6ac-272348fa6ee0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "0ff7f7dc-06be-4414-a29e-4373f428828d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "1796173e-507e-475b-9c30-04a13a6ce3e3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "8cc5c6bb-02f7-4293-bdc8-0f17c6bca5a7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "d0aee16c-4f49-431e-93b0-78618b307091",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "47fb0471-48c5-43fd-9abc-2d66d76c1b1d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "7d755e1a-5952-4f8c-891a-d4339f6fc65e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "c9ce26c9-ee5e-4cae-8835-88fd09e90367",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
