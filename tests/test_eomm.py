import unittest

from NewMM.player import Player
from NewMM.eomm import match_players

class TestEOMM(unittest.TestCase):
    def test_match_players_unique_pairs(self):
        players = [
            Player(mmr=100, latest_outcomes=[1, 1], player_id='A'),
            Player(mmr=80, latest_outcomes=[1, -1], player_id='B'),
            Player(mmr=30, latest_outcomes=[-1, -1], player_id='C'),
            Player(mmr=60, latest_outcomes=[-1, 1], player_id='D'),
        ]
        matches = match_players(players)
        self.assertEqual(len(matches), 2)
        used = set()
        for a, b in matches:
            self.assertNotIn(a, used)
            self.assertNotIn(b, used)
            used.add(a)
            used.add(b)
        self.assertEqual(used, {'A', 'B', 'C', 'D'})

if __name__ == '__main__':
    unittest.main()
