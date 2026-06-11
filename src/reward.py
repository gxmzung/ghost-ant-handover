def calculate_reward(rsrp, los, handover, delay, packet_loss,
                     alpha=1.0, beta=1.0, gamma=1.0, delta=1.0, epsilon=1.0):
    return (
        alpha * rsrp
        + beta * los
        - gamma * handover
        - delta * delay
        - epsilon * packet_loss
    )
