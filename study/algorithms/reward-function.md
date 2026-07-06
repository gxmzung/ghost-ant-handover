# Reward Function

## Why I Studied This

The reward function is the core decision mechanism of Ghost Ant Handover.

The purpose of this study note is to understand why a candidate cell receives a high or low score during handover selection.

---

## What is Reward?

Reward represents communication quality.

A higher reward means:

- better communication quality
- lower risk of packet loss
- lower delay
- fewer unnecessary handovers

A lower reward means:

- unstable communication
- high delay
- high packet loss
- frequent switching risk

---

## Current Implementation

```python
def calculate_reward(
    rsrp,
    los,
    handover,
    delay,
    packet_loss,
    alpha=1.0,
    beta=1.0,
    gamma=1.0,
    delta=1.0,
    epsilon=1.0,
):
    return (
        alpha * rsrp
        + beta * los
        - gamma * handover
        - delta * delay
        - epsilon * packet_loss
    )
```

---

## Meaning of Each Term

### Positive Factors

#### RSRP

Signal strength.

Higher signal strength usually means a more reliable connection.

#### LOS

Line-of-sight condition.

A better line of sight can improve communication quality.

---

### Negative Factors

#### Handover

Frequent switching should be avoided.

#### Delay

High latency reduces communication stability.

#### Packet Loss

Packet loss can seriously affect communication reliability.

---

## Weight Parameters

The coefficients:

- alpha
- beta
- gamma
- delta
- epsilon

control how important each factor is.

For example:

- increasing epsilon makes packet loss more important
- increasing gamma makes unnecessary handovers more expensive

---

## Simple Interpretation

The reward function tries to answer:

> Which candidate cell looks best right now?

The pheromone model then answers:

> Which candidate path has been useful over time?

Ghost Ant combines these two ideas.

---

## Future Work

Possible improvements:

- dynamic weight adjustment
- environment-aware reward tuning
- future network quality prediction
- comparison with baseline handover methods

---

## My Understanding

Reward is similar to a score card.

Good communication conditions add points.

Poor communication conditions subtract points.

The cell with the highest score becomes the preferred handover candidate.