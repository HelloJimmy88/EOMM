"""Simple winning probability estimation using an Elo-like model."""
import math
from typing import Tuple


def predict_win_prob(mmr_a: int, mmr_b: int) -> Tuple[float, float, float]:
    """Return win/draw/lose probabilities for player A versus B."""
    # Draw probability fixed for simplicity
    draw = 0.0
    ea = 1 / (1 + math.pow(10, (mmr_b - mmr_a) / 400))
    win = ea
    lose = 1 - win - draw
    return win, draw, lose
