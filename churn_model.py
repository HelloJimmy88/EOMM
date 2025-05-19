import math

FEATURE_WEIGHTS = [-1.0, 0.003, -0.5, -0.3, -0.2]  # bias, mu_diff, outcome, win_prob, recent_wins


def _sigmoid(x: float) -> float:
    """Standard logistic function."""
    return 1.0 / (1.0 + math.exp(-x))


class ChurnModel:
    """Logistic churn model inspired by the EOMM paper.

    Parameters are placeholders since the paper does not release the actual
    coefficients.
    """

    def __init__(self, feature_weights=None):
        self.feature_weights = feature_weights or FEATURE_WEIGHTS

    def predict(self, mu_diff: float, outcome: int, win_prob: float, recent_wins: int) -> float:
        """Return churn probability in percentage (0-100)."""
        features = [1.0, mu_diff, outcome, win_prob, recent_wins]
        score = sum(w * f for w, f in zip(self.feature_weights, features))
        return _sigmoid(score) * 100
