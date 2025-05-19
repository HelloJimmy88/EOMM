from dataclasses import dataclass, field
from typing import List
import uuid
import random

@dataclass
class Player:
    """A simple player model used for matchmaking."""
    mmr: int
    latest_outcomes: List[int]
    player_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    @staticmethod
    def random(mmr_range=(1, 100)):
        """Create a random player for demonstration."""
        mmr = random.randint(*mmr_range)
        outcomes = [random.choice([1, -1]) for _ in range(2)]
        return Player(mmr=mmr, latest_outcomes=outcomes)
