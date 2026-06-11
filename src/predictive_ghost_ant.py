from dataclasses import dataclass
from typing import List, Tuple

from src.reward import calculate_reward
from src.pheromone import PheromoneMap


@dataclass
class UAVState:
    position: Tuple[int, int, int]
    velocity: Tuple[int, int, int]


@dataclass
class FutureCandidateCell:
    cell_id: str
    x: int
    y: int
    z: int
    rsrp: float
    los: float
    delay: float
    packet_loss: float
    handover: float


class PredictiveGhostAnt:
    def __init__(self, pheromone_map: PheromoneMap, lookahead_steps: int = 5):
        self.pheromone_map = pheromone_map
        self.lookahead_steps = lookahead_steps

    def predict_future_position(self, state: UAVState) -> Tuple[int, int, int]:
        x, y, z = state.position
        vx, vy, vz = state.velocity

        return (
            x + vx * self.lookahead_steps,
            y + vy * self.lookahead_steps,
            z + vz * self.lookahead_steps,
        )

    def evaluate_candidate(self, candidate: FutureCandidateCell) -> float:
        return calculate_reward(
            rsrp=candidate.rsrp,
            los=candidate.los,
            handover=candidate.handover,
            delay=candidate.delay,
            packet_loss=candidate.packet_loss,
            alpha=1.0,
            beta=1.2,
            gamma=0.8,
            delta=0.7,
            epsilon=1.5,
        )

    def virtual_explore(self, state: UAVState, candidates: List[FutureCandidateCell]):
        if not candidates:
            raise ValueError("candidates must not be empty")

        future_position = self.predict_future_position(state)

        scored_candidates = []

        for candidate in candidates:
            reward = self.evaluate_candidate(candidate)

            self.pheromone_map.deposit(
                candidate.x,
                candidate.y,
                candidate.z,
                reward,
            )

            scored_candidates.append((candidate, reward))

        best_candidate, best_reward = max(scored_candidates, key=lambda item: item[1])

        return {
            "future_position": future_position,
            "best_cell": best_candidate.cell_id,
            "best_reward": best_reward,
        }
