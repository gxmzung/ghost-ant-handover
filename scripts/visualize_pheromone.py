import matplotlib.pyplot as plt
import numpy as np


def main():
    grid = np.random.rand(20, 20)

    plt.figure(figsize=(7, 6))
    plt.imshow(grid)
    plt.colorbar(label="Pheromone intensity")
    plt.title("3D Pheromone Map Projection")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()
    plt.savefig("results/pheromone_map.png")
    print("saved: results/pheromone_map.png")


if __name__ == "__main__":
    main()
