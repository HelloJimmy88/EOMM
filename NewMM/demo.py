"""Demonstration of the simplified EOMM implementation."""
from .player import Player
from .eomm import match_players


def main():
    players = [Player.random() for _ in range(10)]
    pairs = match_players(players)
    for (a, b), retain in pairs.items():
        print(f"{a} vs {b} -> expected retain {retain:.2f}")


if __name__ == "__main__":
    main()
