import csv
import matplotlib.pyplot as plt

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


def save_csv(rows):
    with open("results/uam_simulation_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "x", "y", "z", "selected_cell", "future_x", "future_y", "future_z", "reward"])
        writer.writerows(rows)


def plot_path(path, stations):
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]

    plt.figure(figsize=(7, 7))
    plt.plot(xs, ys, marker="o", label="UAM path")

    for station in stations:
        plt.scatter(station.x, station.y, marker="^")
        plt.text(station.x + 0.2, station.y + 0.2, station.cell_id, fontsize=8)

    plt.title("UAM Trajectory and Base Stations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/uam_trajectory.png")
    print("saved: results/uam_trajectory.png")


def main():
    stations = generate_base_stations()
    pheromone = PheromoneMap(x=30, y=30, z=5)
    ghost = PredictiveGhostAnt(pheromone_map=pheromone, lookahead_steps=3)

    uam = UAM(position=(2, 2, 2), velocity=(1, 1, 0))

    current_cell = None
    handover_count = 0
    rows = []
    path = []

    print("UAM Ghost Ant Simulation")
    print("========================")

    for t in range(20):
        position = uam.move()
        path.append(position)

        state = UAVState(position=position, velocity=uam.velocity)
        candidates = build_candidates(position, stations, current_cell)
        result = ghost.virtual_explore(state, candidates)

        selected_cell = result["best_cell"]

        if current_cell is None:
            current_cell = selected_cell
        elif selected_cell != current_cell:
            handover_count += 1
            current_cell = selected_cell

        future = result["future_position"]
        reward = result["best_reward"]

        rows.append([
            t,
            position[0],
            position[1],
            position[2],
            current_cell,
            future[0],
            future[1],
            future[2],
            reward,
        ])

        print(
            f"t={t:02d} | pos={position} | selected={current_cell} | "
            f"future={future} | reward={reward:.3f}"
        )

    print("========================")
    print(f"Total handovers: {handover_count}")

    save_csv(rows)
    plot_path(path, stations)

    print("saved: results/uam_simulation_log.csv")


if __name__ == "__main__":
    main()
