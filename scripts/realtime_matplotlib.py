import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from simulation.environment import generate_base_stations
from simulation.uam import UAM

stations = generate_base_stations()
uam = UAM(position=(2, 2, 2), velocity=(1, 1, 0))
path = []

fig, ax = plt.subplots(figsize=(7, 7))

def update(frame):
    ax.clear()
    pos = uam.move()
    path.append(pos)

    xs = [p[0] for p in path]
    ys = [p[1] for p in path]

    for bs in stations:
        ax.scatter(bs.x, bs.y, marker="^", s=100)
        ax.text(bs.x + 0.3, bs.y + 0.3, bs.cell_id)

    ax.plot(xs, ys, marker="o", label="UAM Path")
    ax.scatter(pos[0], pos[1], s=200, marker="o", label="Current UAM")

    ax.set_xlim(0, 30)
    ax.set_ylim(0, 30)
    ax.grid(True)
    ax.legend()
    ax.set_title(f"Realtime UAM Simulation | t={frame}")

ani = FuncAnimation(fig, update, frames=30, interval=500)
plt.show()
