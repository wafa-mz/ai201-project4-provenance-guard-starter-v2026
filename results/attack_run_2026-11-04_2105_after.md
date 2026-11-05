# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 21:05
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `98332020-81b0-44b9-8612-06cb8e790968` | human | 0.338 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `acee39ae-0df7-48fe-a96c-e2caddc87457` | human | 0.511 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `6ef28592-8fd5-43d3-a7d2-5274c0ee3a7a` | human | 0.600 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `3b7544da-c77c-429a-9759-11799363e3ce` | human | 0.606 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `45c6a370-704f-41df-8e28-5af6638be0cc` | human | 0.371 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `09a659df-c29d-40ff-a6b8-52525f2516f3` | human | 0.452 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b196f4e9-cc14-4e33-92f6-f042bfde9271` | human | 0.552 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `f94788dc-66b4-41cf-88c8-79e8db0a02a9` | human | 0.347 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `85158b3f-93f0-433a-88eb-f7f180bac1e0` | human | 0.627 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `1199021e-abff-45a7-b702-ab97ed39e98b` | ai | 0.814 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `abfe925a-781e-4bfa-9584-d8f039423f46` | human | 0.553 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `dc75ada8-3601-45ef-a18d-fe8e122b9c87` | human | 0.669 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `7f5ea658-2390-4f85-9799-0ad9227f6c2c` | human | 0.677 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `a6748950-e5e5-47ae-b44e-bda57e84ff51` | human | 0.727 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `287ea448-fdd4-4c64-b0f0-a6071c9fc666` | human | 0.744 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `d7bdd47f-c2c5-457c-a200-c90f73a9d6b2` | human | 0.714 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d1ebf201-0961-4982-a9d3-e1419ec608f5` | ai | 0.759 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `2c34a7d7-2b7a-437b-b7a8-f8d7e6a1801f` | human | 0.393 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ed78fb65-3eff-48c2-b77f-db401599a31d` | human | 0.440 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `1b32424f-aa9c-4e19-adbb-774b99c47e64` | human | 0.283 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `929c1f7c-8fc3-4a7e-987e-2eafc4e72ddc` | human | 0.528 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `7cc1aa30-74b2-4e86-a35f-35ddf2e7ba47` | human | 0.498 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `b37d14f3-e7fd-4618-8661-eda7cf1e83a6` | human | 0.582 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d1f8fb65-b8fc-401e-90bb-f4b390035fbc` | human | 0.519 |  |
| MF01 | malformed | text is only whitespace | 200 | `41c7e0db-ffde-4a43-9647-49f880f68155` | human | 0.323 |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `05f160e9-5590-41e5-a3bf-10fd0120370d` | human | 0.200 |  |
| MF04 | malformed | text is only punctuation | 200 | `06d25999-05bd-4d8f-abc5-c3794c349500` | human | 0.207 |  |
| MF05 | malformed | text is a very long single word | 200 | `0223e765-abe3-41e4-946d-f0ea47fa8346` | ai | 0.799 |  |
| MF06 | malformed | text is emoji only | 200 | `cee00e60-d89c-4251-8939-dbbdd140f398` | ai | 0.798 |  |
| MF07 | malformed | text is right-to-left script | 200 | `d9157560-ae1d-4062-aa63-ea85f23a2509` | human | 0.744 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `2a178a64-d1ff-4677-9f38-76805e9f189c` | human | 0.230 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `67abf296-c8fb-4750-b56f-b751897e2481` | human | 0.217 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6bdd9b14-be98-40cf-94a4-71aef9b8768d` | human | 0.217 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e261d76b-f92d-4d3a-bc6f-d9c4e73959d1` | human | 0.217 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7adbdc98-aa32-4150-9464-d0e4dba90590` | human | 0.217 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a5d2362c-8cd9-4aa4-b690-d0d83c46d978` | human | 0.217 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2e099f58-7c8e-4c86-909d-99684f3e4bfc` | human | 0.217 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b6d9efda-d4b9-44d9-8737-673c33a9be11` | human | 0.217 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b36f6df0-aff0-4dd4-ae4d-46cab65a4fbd` | human | 0.217 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8ce7bfda-2cad-471c-80fa-23e781400ef0` | human | 0.217 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9e7851dd-f29f-4725-84d2-a69d99f17bf4` | human | 0.217 |  |
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
  "content_id": "98332020-81b0-44b9-8612-06cb8e790968",
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
  "content_id": "acee39ae-0df7-48fe-a96c-e2caddc87457",
  "creator_id": "attacker_EV02",
  "guess": "human",
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
  "content_id": "6ef28592-8fd5-43d3-a7d2-5274c0ee3a7a",
  "creator_id": "attacker_EV03",
  "guess": "human",
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
  "content_id": "3b7544da-c77c-429a-9759-11799363e3ce",
  "creator_id": "attacker_EV04",
  "guess": "human",
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
  "content_id": "45c6a370-704f-41df-8e28-5af6638be0cc",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3708,
  "model_score": 0.3212,
  "style_score": 0.4452,
  "label": "This text was likely written by a human.",
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
  "content_id": "09a659df-c29d-40ff-a6b8-52525f2516f3",
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
  "content_id": "b196f4e9-cc14-4e33-92f6-f042bfde9271",
  "creator_id": "attacker_EV07",
  "guess": "human",
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
  "content_id": "f94788dc-66b4-41cf-88c8-79e8db0a02a9",
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
  "content_id": "85158b3f-93f0-433a-88eb-f7f180bac1e0",
  "creator_id": "attacker_EV09",
  "guess": "human",
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
  "content_id": "1199021e-abff-45a7-b702-ab97ed39e98b",
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
  "content_id": "abfe925a-781e-4bfa-9584-d8f039423f46",
  "creator_id": "attacker_FP01",
  "guess": "human",
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
  "content_id": "dc75ada8-3601-45ef-a18d-fe8e122b9c87",
  "creator_id": "attacker_FP02",
  "guess": "human",
  "confidence": 0.6692,
  "model_score": 0.7387,
  "style_score": 0.5649,
  "label": "We are unsure whether this text was written by a human or AI.",
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
  "content_id": "7f5ea658-2390-4f85-9799-0ad9227f6c2c",
  "creator_id": "attacker_FP03",
  "guess": "human",
  "confidence": 0.6774,
  "model_score": 0.8051,
  "style_score": 0.4858,
  "label": "We are unsure whether this text was written by a human or AI.",
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
  "content_id": "a6748950-e5e5-47ae-b44e-bda57e84ff51",
  "creator_id": "attacker_FP04",
  "guess": "human",
  "confidence": 0.7265,
  "model_score": 0.8329,
  "style_score": 0.5669,
  "label": "We are unsure whether this text was written by a human or AI.",
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
  "content_id": "287ea448-fdd4-4c64-b0f0-a6071c9fc666",
  "creator_id": "attacker_FP05",
  "guess": "human",
  "confidence": 0.7439,
  "model_score": 0.8005,
  "style_score": 0.6589,
  "label": "We are unsure whether this text was written by a human or AI.",
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
  "content_id": "d7bdd47f-c2c5-457c-a200-c90f73a9d6b2",
  "creator_id": "attacker_FP06",
  "guess": "human",
  "confidence": 0.7135,
  "model_score": 0.8814,
  "style_score": 0.4616,
  "label": "We are unsure whether this text was written by a human or AI.",
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
  "content_id": "d1ebf201-0961-4982-a9d3-e1419ec608f5",
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
  "content_id": "2c34a7d7-2b7a-437b-b7a8-f8d7e6a1801f",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3934,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "This text was likely written by a human.",
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
  "content_id": "ed78fb65-3eff-48c2-b77f-db401599a31d",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.4403,
  "model_score": 0.4625,
  "style_score": 0.4069,
  "label": "This text was likely written by a human.",
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
  "content_id": "1b32424f-aa9c-4e19-adbb-774b99c47e64",
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
  "content_id": "929c1f7c-8fc3-4a7e-987e-2eafc4e72ddc",
  "creator_id": "attacker_PI03",
  "guess": "human",
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
  "content_id": "7cc1aa30-74b2-4e86-a35f-35ddf2e7ba47",
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
  "content_id": "b37d14f3-e7fd-4618-8661-eda7cf1e83a6",
  "creator_id": "attacker_PI05",
  "guess": "human",
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
  "content_id": "d1f8fb65-b8fc-401e-90bb-f4b390035fbc",
  "creator_id": "attacker_PI06",
  "guess": "human",
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
  "content_id": "41c7e0db-ffde-4a43-9647-49f880f68155",
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
  "content_id": "05f160e9-5590-41e5-a3bf-10fd0120370d",
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
  "content_id": "06d25999-05bd-4d8f-abc5-c3794c349500",
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
  "content_id": "0223e765-abe3-41e4-946d-f0ea47fa8346",
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
  "content_id": "cee00e60-d89c-4251-8939-dbbdd140f398",
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
  "content_id": "d9157560-ae1d-4062-aa63-ea85f23a2509",
  "creator_id": "attacker_MF07",
  "guess": "human",
  "confidence": 0.7438,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We are unsure whether this text was written by a human or AI.",
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
  "content_id": "2a178a64-d1ff-4677-9f38-76805e9f189c",
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
  "content_id": "67abf296-c8fb-4750-b56f-b751897e2481",
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
  "content_id": "6bdd9b14-be98-40cf-94a4-71aef9b8768d",
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
  "content_id": "e261d76b-f92d-4d3a-bc6f-d9c4e73959d1",
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
  "content_id": "7adbdc98-aa32-4150-9464-d0e4dba90590",
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
  "content_id": "a5d2362c-8cd9-4aa4-b690-d0d83c46d978",
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
  "content_id": "2e099f58-7c8e-4c86-909d-99684f3e4bfc",
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
  "content_id": "b6d9efda-d4b9-44d9-8737-673c33a9be11",
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
  "content_id": "b36f6df0-aff0-4dd4-ae4d-46cab65a4fbd",
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
  "content_id": "8ce7bfda-2cad-471c-80fa-23e781400ef0",
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
  "content_id": "9e7851dd-f29f-4725-84d2-a69d99f17bf4",
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
