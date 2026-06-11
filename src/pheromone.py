import numpy as np


class PheromoneMap:
    def __init__(self, x=20, y=20, z=5, evaporation=0.95):
        self.map = np.ones((x, y, z))
        self.evaporation = evaporation

    def evaporate(self):
        self.map *= self.evaporation

    def deposit(self, x, y, z, amount):
        self.map[x, y, z] += amount

    def get(self, x, y, z):
        return self.map[x, y, z]
