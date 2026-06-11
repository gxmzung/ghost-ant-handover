from src.pheromone import PheromoneMap
from src.ghost_ant import GhostAnt


def main():
    pheromone = PheromoneMap()
    ghost = GhostAnt(pheromone)

    candidate = {
        "x": 10,
        "y": 8,
        "z": 2,
        "rsrp": 0.92,
        "los": 0.95,
        "handover": 0.2,
        "delay": 0.1,
        "packet_loss": 0.03,
    }

    score = ghost.explore(candidate)

    print("Ghost Ant Exploration Demo")
    print(f"Reward score: {score:.3f}")
    print(f"Pheromone τ(10,8,2): {pheromone.get(10, 8, 2):.3f}")


if __name__ == "__main__":
    main()
