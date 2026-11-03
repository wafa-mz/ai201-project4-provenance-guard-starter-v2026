import re
import statistics

def _words(text):
    return re.findall(r"[A-Za-z']+", text)

def _sentences(text):
    return [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]

def _map(x, x0, x1, y0, y1):
    """Map x from range [x0, x1] to [y0, y1], clamped."""
    if x1 == x0: return (y0 + y1) / 2
    t = max(0.0, min(1.0, (x - x0) / (x1 - x0)))
    return y0 + t * (y1 - y0)

def score_text(text):
    words = _words(text)
    sents = _sentences(text)

    if len(words) < 20 or len(sents) < 2:
        return 0.5  # Not enough text to judge

    # 1. Sentence-length spread (AI is smoother → lower variance)
    lens = [len(_words(s)) for s in sents]
    mean_len = statistics.mean(lens)
    std_len = statistics.pstdev(lens) if len(lens) > 1 else 0
    cv = std_len / mean_len if mean_len else 0
    s_spread = _map(cv, 0.2, 0.8, 0.9, 0.1)

    # 2. Type-token ratio (word variety)
    ttr = len(set(w.lower() for w in words)) / len(words)
    s_ttr = _map(ttr, 0.3, 0.7, 0.8, 0.2)

    # 3. Punctuation density
    punct = len(re.findall(r"[.,;:!?]", text))
    dens = punct / len(words)
    s_punct = _map(dens, 0.02, 0.15, 0.1, 0.9)

    # Average the three sub-scores
    return round((s_spread + s_ttr + s_punct) / 3.0, 4)