from typing import Iterable, Tuple, Dict, List

from .player import Player
from .skill_model import predict_win_prob
from .churn_model import predict_individual_churn


def _edge_weight(pa: Player, pb: Player) -> float:
    """Calculate retention weight for a pair of players."""
    win, draw, lose = predict_win_prob(pa.mmr, pb.mmr)
    churn_a = (
        win * predict_individual_churn(pa.latest_outcomes[-2:] + [1])
        + lose * predict_individual_churn(pa.latest_outcomes[-2:] + [-1])
    )
    churn_b = (
        win * predict_individual_churn(pb.latest_outcomes[-2:] + [-1])
        + lose * predict_individual_churn(pb.latest_outcomes[-2:] + [1])
    )
    churn = churn_a + churn_b
    return 200 - churn


def build_edges(players: Iterable[Player]) -> Dict[Tuple[str, str], float]:
    """Compute retention weights for all possible pairs."""
    players = list(players)
    edges: Dict[Tuple[str, str], float] = {}
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            pa, pb = players[i], players[j]
            key = tuple(sorted((pa.player_id, pb.player_id)))
            edges[key] = _edge_weight(pa, pb)
    return edges


def _best_matching(players: List[Player], edges: Dict[Tuple[str, str], float]):
    """Brute-force search for the best matching (small pools only)."""
    if not players:
        return [], 0.0
    first = players[0]
    best_pairs = []
    best_score = -1.0
    for i in range(1, len(players)):
        second = players[i]
        pair_key = tuple(sorted((first.player_id, second.player_id)))
        weight = edges[pair_key]
        rest_players = players[1:i] + players[i + 1 :]
        pairs, score = _best_matching(rest_players, edges)
        score += weight
        if score > best_score:
            best_score = score
            best_pairs = [(first.player_id, second.player_id)] + pairs
    return best_pairs, best_score


def match_players(players: Iterable[Player]) -> Dict[Tuple[str, str], float]:
    """Return optimal pairs with expected retention. Works for small pools."""
    players = list(players)
    edges = build_edges(players)
    pairs, _ = _best_matching(players, edges)
    return {tuple(pair): edges[tuple(sorted(pair))] for pair in pairs}
