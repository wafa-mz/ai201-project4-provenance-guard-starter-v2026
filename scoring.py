import config

def combine_signals(detector_score, stylometry_score):
    # Weighted average: 60% detector, 40% stylometry
    combined = (detector_score * 0.6) + (stylometry_score * 0.4)
    return round(combined, 4)

def score_to_label(score):
    # High confidence AI
    if score >= 0.65:
        return "This text was likely written by an AI."
    # Unsure
    elif score >= 0.35:
        return "We are unsure whether this text was written by a human or AI."
    # High confidence Human
    else:
        return "This text was likely written by a human."