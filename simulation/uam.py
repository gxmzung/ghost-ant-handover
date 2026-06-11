from dataclasses import dataclass
from typing import Tuple


@dataclass
class UAM:
    position: Tuple[int, int, int]
    velocity: Tuple[int, int, int]

    def move(self):
        x, y, z = self.position
        vx, vy, vz = self.velocity

        self.position = (
            x + vx,
            y + vy,
            z + vz,
        )

        return self.position
