import random
import matplotlib.pyplot as plt


def simulate(mode: str, steps: int = 50):
    handovers = []
    delays = []
    packet_losses = []

    ho_count = 0

    for t in range(steps):
        if mode == "baseline":
            ho_prob = 0.35
            delay = random.uniform(60, 95)
            packet_loss = random.uniform(0.02, 0.08)

        elif mode == "aco":
            ho_prob = 0.18
            delay = random.uniform(45, 75)
            packet_loss = random.uniform(0.01, 0.05)

        elif mode == "ghost_ant":
            ho_prob = 0.08
            delay = random.uniform(35, 60)
            packet_loss = random.uniform(0.005, 0.025)

        else:
            raise ValueError("mode must be baseline, aco, or ghost_ant")

        if random.random() < ho_prob:
            ho_count += 1

        handovers.append(ho_count)
        delays.append(delay)
        packet_losses.append(packet_loss)

    return handovers, delays, packet_losses


def plot_metric(metric_name, data_dict, ylabel, filename):
    plt.figure(figsize=(10, 5))

    for mode, values in data_dict.items():
        plt.plot(values, label=mode)

    plt.title(metric_name)
    plt.xlabel("Time step")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"saved: {filename}")


def main():
    modes = ["baseline", "aco", "ghost_ant"]

    results = {
        mode: simulate(mode)
        for mode in modes
    }

    plot_metric(
        "Cumulative Handover Count",
        {mode: results[mode][0] for mode in modes},
        "Handover count",
        "handover_comparison.png",
    )

    plot_metric(
        "Communication Delay",
        {mode: results[mode][1] for mode in modes},
        "Delay (ms)",
        "delay_comparison.png",
    )

    plot_metric(
        "Packet Loss",
        {mode: results[mode][2] for mode in modes},
        "Packet loss ratio",
        "packet_loss_comparison.png",
    )


if __name__ == "__main__":
    main()
