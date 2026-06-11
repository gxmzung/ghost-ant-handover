from src.pheromone import PheromoneMap
from src.predictive_ghost_ant import (
    PredictiveGhostAnt,
    UAVState,
    FutureCandidateCell,
)


def main():
    pheromone = PheromoneMap(x=30, y=30, z=5)

    ghost = PredictiveGhostAnt(
        pheromone_map=pheromone,
        lookahead_steps=5,
    )

    state = UAVState(
        position=(5, 5, 2),
        velocity=(1, 1, 0),
    )

    candidates = [
        FutureCandidateCell(
            cell_id="BS-1",
            x=8,
            y=8,
            z=2,
            rsrp=0.70,
            los=0.60,
            delay=0.25,
            packet_loss=0.05,
            handover=0.3,
        ),
        FutureCandidateCell(
            cell_id="BS-2",
            x=10,
            y=10,
            z=2,
            rsrp=0.92,
            los=0.95,
            delay=0.08,
            packet_loss=0.01,
            handover=0.1,
        ),
        FutureCandidateCell(
            cell_id="BS-3",
            x=12,
            y=9,
            z=2,
            rsrp=0.85,
            los=0.75,
            delay=0.12,
            packet_loss=0.02,
            handover=0.2,
        ),
    ]

    result = ghost.virtual_explore(state, candidates)

    print("Predictive Ghost Ant Demo")
    print(f"Future position: {result['future_position']}")
    print(f"Best future cell: {result['best_cell']}")
    print(f"Best reward: {result['best_reward']:.3f}")


if __name__ == "__main__":
    main()
