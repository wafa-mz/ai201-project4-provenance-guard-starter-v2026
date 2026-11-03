# Acceptance Criteria

1. **False Positives**
   * **Target:** Of 10 pieces of text I know are human-written, at most 1 is labeled as "high-confidence AI".
   * **Why:** Falsely accusing a human writer of cheating is the worst mistake this system can make.

2. **Score Spread**
   * **Target:** On a test of 5 clearly-AI texts and 5 clearly-human texts, the average score of the AI texts should be at least 0.3 higher than the human texts.
   * **Why:** If the scores are too close together, the system can't reliably tell them apart.

3. **Label Coverage**
   * **Target:** There must be at least 1 reachable score for every label (High-confidence AI, High-confidence human, Unsure).
   * **Why:** The "Unsure" label is useless if the math never allows a score to land there.

4. **The Appeal Path**
   * **Target:** When I submit an appeal with a valid content ID, the system must change the status to `under_review` and record it in the log in 1 request.
   * **Why:** The appeal is the only thing protecting humans from a false positive, so it must work immediately.

5. **Bad Input**
   * **Target:** If I submit text that is empty or longer than 10,000 characters, the system returns a 400 error and does not log it.
   * **Why:** The system shouldn't waste compute or crash on invalid data.