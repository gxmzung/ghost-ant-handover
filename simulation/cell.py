from dataclasses import dataclass
import math


@dataclass
class BaseStation:
    cell_id: str
    x: int
    y: int
    z: int = 2


def distance_2d(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def estimate_rsrp(uav_position, base_station):
    d = distance_2d(uav_position, (base_station.x, base_station.y))

    # Simple normalized RSRP model
    # closer cell = higher RSRP
    return max(0.1, 1.0 - d / 30.0)


def estimate_los(uav_position, base_station):
    d = distance_2d(uav_position, (base_station.x, base_station.y))

    # Simple LoS probability model
    return max(0.1, 1.0 - d / 40.0)


def estimate_delay(rsrp):
    # weaker signal = higher delay
    return max(0.05, 0.4 - rsrp * 0.3)


def estimate_packet_loss(rsrp, los):
    # weaker signal and worse LoS = higher packet loss
    return max(0.005, 0.1 - (rsrp + los) * 0.04)
