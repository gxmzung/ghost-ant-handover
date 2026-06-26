# Code Review: `src/reward.py`

## Original Code

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

# Purpose

This function calculates a reward score for each candidate communication cell.

The reward is later used to compare multiple candidate cells and select the most suitable one.

---

# Function Name

```python
calculate_reward(...)
```

The name clearly explains its responsibility.

It does not perform handover directly.

It only calculates the reward value.

---

# Input Parameters

## rsrp

Reference Signal Received Power

Represents received signal strength.

Higher is generally better.

---

## los

Line Of Sight score.

Represents visibility between the UAM and the communication node.

Better visibility increases communication quality.

---

## handover

Represents switching cost.

Frequent handovers should be discouraged.

Therefore this value becomes a penalty.

---

## delay

Communication latency.

Higher delay decreases communication quality.

---

## packet_loss

Percentage of lost packets.

Lower packet loss means better communication reliability.

---

## alpha ~ epsilon

These are weighting coefficients.

They determine how important each factor is.

Example:

```text
alpha = Signal importance

beta = LOS importance

gamma = Handover penalty

delta = Delay penalty

epsilon = Packet-loss penalty
```

Changing these values changes the decision strategy.

---

# Reward Equation

The reward score is

Reward

=

Signal

+

LOS

−

Handover Cost

−

Delay

−

Packet Loss

---

# Why "+" and "-" ?

Positive factors

```
Signal
LOS
```

increase reward.

Negative factors

```
Delay
Packet Loss
Handover
```

decrease reward.

---

# Example

Suppose

```text
RSRP = 10

LOS = 8

Handover = 2

Delay = 3

Packet Loss = 1
```

Then

```text
Reward

=

10

+

8

-

2

-

3

-

1

=

12
```

Higher reward

↓

Better candidate cell.

---

# Design Advantages

Simple

Easy to understand

Easy to tune

Easy to compare with other methods

Suitable for simulation

---

# Current Limitation

Currently every coefficient is

```text
1.0
```

In practice

the importance of

Delay

Packet Loss

Signal

may be different.

Future work could optimize these weights.

---

# What I Learned

This function is not making the handover decision.

It is only calculating one score.

The handover algorithm will compare multiple reward values before selecting the best communication cell.

Understanding this separation makes the overall architecture easier to explain.