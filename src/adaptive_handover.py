from dataclasses import dataclass
from typing import List, Optional

from src.reward import calculate_reward


@dataclass
class CandidateCell:
    cell_id: str
    rsrp: float
    los: float
    delay: float
    packet_loss: float
    handover_required: bool


class AdaptiveHandover:
    def __init__(self, min_reward_gap: float = 0.1):
        self.current_cell: Optional[str] = None
        self.min_reward_gap = min_reward_gap

    def score_cell(self, cell: CandidateCell) -> float:
        handover_penalty = 1.0 if cell.handover_required else 0.0

        return calculate_reward(
            rsrp=cell.rsrp,
            los=cell.los,
            handover=handover_penalty,
            delay=cell.delay,
            packet_loss=cell.packet_loss,
            alpha=1.0,
            beta=1.2,
            gamma=0.8,
            delta=0.7,
            epsilon=1.5,
        )

    def select_best_cell(self, candidates: List[CandidateCell]) -> Optional[CandidateCell]:
        if not candidates:
            return None

        return max(candidates, key=self.score_cell)

    def should_handover(self, candidates: List[CandidateCell]) -> bool:
        best_cell = self.select_best_cell(candidates)

        if best_cell is None:
            return False

        if self.current_cell is None:
            self.current_cell = best_cell.cell_id
            return False

        current_candidates = [
            cell for cell in candidates
            if cell.cell_id == self.current_cell
        ]

        if not current_candidates:
            return True

        current_score = self.score_cell(current_candidates[0])
        best_score = self.score_cell(best_cell)

        return (
            best_cell.cell_id != self.current_cell
            and best_score - current_score > self.min_reward_gap
        )

    def update_current_cell(self, candidates: List[CandidateCell]) -> Optional[str]:
        if self.should_handover(candidates):
            best_cell = self.select_best_cell(candidates)
            self.current_cell = best_cell.cell_id
            return self.current_cell

        return self.current_cell
