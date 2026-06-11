from simulation.cell import BaseStation


def generate_base_stations():
    stations = []

    index = 1
    for x in range(5, 30, 8):
        for y in range(5, 30, 8):
            stations.append(
                BaseStation(
                    cell_id=f"BS-{index}",
                    x=x,
                    y=y,
                    z=2,
                )
            )
            index += 1

    return stations
