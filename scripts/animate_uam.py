import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from simulation.environment import generate_base_stations


def load_log(path):
    rows = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "time": int(row["time"]),
                "x": float(row["x"]),
                "y": float(row["y"]),
                "cell": row["selected_cell"],
                "reward": float(row["reward"]),
            })

    return rows


def main():
    log_path = Path("results/uam_simulation_log.csv")
    output_path = Path("results/uam_animation.gif")

    if not log_path.exists():
        raise FileNotFoundError("Run scripts/uam_simulation.py first.")

    rows = load_log(log_path)
    stations = generate_base_stations()

    fig, ax = plt.subplots(figsize=(7, 7))

    def update(frame):
        ax.clear()

        current = rows[frame]
        path = rows[: frame + 1]

        xs = [p["x"] for p in path]
        ys = [p["y"] for p in path]

        for station in stations:
            ax.scatter(station.x, station.y, marker="^")
            ax.text(station.x + 0.2, station.y + 0.2, station.cell_id, fontsize=8)

        ax.plot(xs, ys, marker="o", label="UAM path")
        ax.scatter(current["x"], current["y"], s=120, marker="o")

        ax.set_title(
            f"Ghost Ant UAM Simulation | t={current['time']} | "
            f"cell={current['cell']} | reward={current['reward']:.2f}"
        )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_xlim(0, 30)
        ax.set_ylim(0, 30)
        ax.grid(True)
        ax.legend(loc="upper left")

    ani = FuncAnimation(fig, update, frames=len(rows), interval=400)

    ani.save(output_path, writer=PillowWriter(fps=3))

    print(f"saved: {output_path}")


if __name__ == "__main__":
    main()
