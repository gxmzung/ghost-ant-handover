from src.reward import calculate_reward

reward = calculate_reward(
    rsrp=0.8,
    los=0.9,
    handover=0.2,
    delay=0.1,
    packet_loss=0.05,
)

print("Ghost Ant Adaptive Handover Demo")
print(f"Reward: {reward:.3f}")
