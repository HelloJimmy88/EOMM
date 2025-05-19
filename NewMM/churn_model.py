"""Simple churn prediction helpers based on recent outcomes."""
from typing import Sequence

# Basic mapping of last three outcomes to churn risk (percentage)
_CHURN_TABLE = {
    (1, 1, 1): 37,
    (1, 1, -1): 49,
    (1, -1, 1): 46,
    (-1, 1, 1): 43,
    (-1, 1, -1): 37,
    (-1, -1, 1): 27,
    (1, -1, -1): 56,
    (-1, -1, -1): 61,
}

def predict_individual_churn(history: Sequence[int]) -> float:
    """Return churn probability given the upcoming outcome appended to history."""
    key = tuple(history)
    return _CHURN_TABLE.get(key, 50)
