"""
Scenarios for evaluating acceptance criteria.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "I went to the store yesterday and bought some apples. They were red and green and tasted really good.",
            "The weather today is kind of cloudy, but I think it might clear up later this afternoon.",
            "I am learning how to use Python for my class, and it is a bit tricky but fun.",
            "My favorite movie is probably The Matrix, I love the action scenes.",
            "I need to remember to buy milk and bread on my way home from work today.",
            "I woke up late this morning so I had to skip breakfast and just grab coffee.",
            "The new restaurant downtown has really good pizza, you should try it sometime.",
            "I am planning a trip to the mountains next month with my friends.",
            "I have been reading a lot of mystery novels lately, they are so engaging.",
            "The traffic on the highway was terrible this morning, it took an extra hour."
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        "texts": [
            "In conclusion, it is important to note that artificial intelligence represents a transformative paradigm shift in modern society. Furthermore, the integration of these technologies necessitates a comprehensive framework.",
            "I went to the store yesterday and bought some apples. They were red and green and tasted really good.",
            "The quick brown fox jumps over the lazy dog. This is a test of the system."
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },
]

def validate() -> list[str]:
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems