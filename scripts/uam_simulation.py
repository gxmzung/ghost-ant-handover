from src.pheromone import PheromoneMap
from src.predictive_ghost_ant import (
    PredictiveGhostAnt,
    UAVState,
    FutureCandidateCell,
)
from simulation.environment import generate_base_stations
from simulation.cell import (
    estimate_rsrp,
    estimate_los,
    estimate_delay,
    estimate_packet_loss,
)
from simulation.uam import UAM


def build_candidates(uam_position, stations, current_cell):
    candidates = []

    for station in stations:
        rsrp = estimate_rsrp(uam_position, station)
        los = estimate_los(uam_position, station)
        delay = estimate_delay(rsrp)
        packet_loss = estimate_packet_loss(rsrp, los)
        handover = 0.0 if station.cell_id == current_cell else 0.1

        candidates.append(
            FutureCandidateCell(
                cell_id=station.cell_id,
                x=min(station.x, 29),
                y=min(station.y, 29),
                z=station.z,
                rsrp=rsrp,
                los=los,
                delay=delay,
                packet_loss=packet_loss,
                handover=handover,
            )
        )

    return candidates


def main():
    stations = generate_base_stations()
    pheromone = PheromoneMap(x=30, y=30, z=5)
    ghost = PredictiveGhostAnt(pheromone_map=pheromone, lookahead_steps=3)

    uam = UAM(
        position=(2, 2, 2),
        velocity=(1, 1, 0),
    )

    current_cell = None
    handover_count = 0

    print("UAM Ghost Ant Simulation")
    print("========================")

    for t in range(20):
        position = uam.move()

        state = UAVState(
            position=position,
            velocity=uam.velocity,
        )

        candidates = build_candidates(position, stations, current_cell)
        result = ghost.virtual_explore(state, candidates)

        selected_cell = result["best_cell"]

        if current_cell is None:
            current_cell = selected_cell

        elif selected_cell != current_cell:
            handover_count += 1
            current_cell = selected_cell

        print(
            f"t={t:02d} | pos={position} | selected={current_cell} | "
            f"future={result['future_position']} | reward={result['best_reward']:.3f}"
        )

    print("========================")
    print(f"Total handovers: {handover_count}")


if __name__ == "__main__":
    main()
