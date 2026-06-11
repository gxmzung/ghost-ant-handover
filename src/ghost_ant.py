from src.reward import calculate_reward


class GhostAnt:
    def __init__(self, pheromone_map):
        self.pheromone_map = pheromone_map

    def explore(self, candidate):
        reward = calculate_reward(
            rsrp=candidate["rsrp"],
            los=candidate["los"],
            handover=candidate["handover"],
            delay=candidate["delay"],
            packet_loss=candidate["packet_loss"],
        )

        self.pheromone_map.deposit(
            candidate["x"],
            candidate["y"],
            candidate["z"],
            reward,
        )

        return reward
