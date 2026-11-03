# Milestone 1: Design Notes

## 1. The Path of a Submission
1. A POST request to /submit sends JSON containing the text and creator_id.
2. The system checks if the text is empty or too long.
3. Signal 1 (detector.py) reads the text and adds a score from 0 to 1 showing how likely it is to be AI.
4. Signal 2 (stylometry.py) reads the text and adds a score based on things like sentence length and word variety.
5. We combine the two scores into one final confidence number.
6. We turn that number into a plain-English label (like "Likely AI").
7. We save the whole record to the audit log.

## 2. The Two Signals and Their Blind Spots
**Signal 1 (detector.py):**
What it measures: It measures the probability that a machine wrote the text.
Why it differs: AI often uses very common words and predictable sentence structures.
Blind spot: It might accidentally flag a human who writes very formally (like a lawyer or a non-native English speaker).

**Signal 2 (stylometry.py):**
* What it measures: It measures things like sentence length, word variety, and punctuation
* Why it differs: AI tends to be very consistent, while humans are messy and vary their sentence lengths.
* Blind spot: Poetry or short sentences might look like AI because they have a consistent rhythm.

## 3. The False Positive Trace
*Imagine a real human submits a poem and our system says it's AI.*
* What score did they get? 0.85
* What label did they see? "This was likely written by an AI."
* What can they do about it? Click an "Appeal" button to explain they wrote it.

## 4. Endpoint Contracts

**POST /submit**
* **Input:** `{"text": "string", "creator_id": "string"}`
* **Output:** `{"content_id": "string", "guess": "string", "confidence": float, "label": "string"}`
* **Errors:** Return a 400 error if the text is missing or empty.

**POST /appeal**
* **Input:** `{"content_id": "string", "reasoning": "string"}`
* **Output:** `{"status": "under_review", "message": "string"}`
* **Errors:** Return a 404 error if the content_id doesn't exist in our database.