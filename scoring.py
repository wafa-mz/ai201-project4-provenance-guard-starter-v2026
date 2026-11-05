import config

def combine_signals(detector_score, stylometry_score):
    # Weighted average: 60% detector, 40% stylometry
    combined = (detector_score * 0.6) + (stylometry_score * 0.4)
    return round(combined, 4)

def score_to_label(score):
    if score >= config.AI_THRESHOLD:
        return "This text was likely written by an AI."
    if score >= config.HUMAN_THRESHOLD:
        return "We are unsure whether this text was written by a human or AI."
    else:
        return "This text was likely written by a human."