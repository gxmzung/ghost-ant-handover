# Method

## Problem Definition

Urban Air Mobility (UAM) systems frequently move across multiple communication cells.

Traditional handover approaches often rely on fixed thresholds such as signal strength, which may cause:

* unnecessary handovers
* increased packet loss
* communication instability
* higher latency

The objective of this research is to design a predictive handover strategy that improves communication continuity.

---

## Ghost Ant Concept

The proposed Ghost Ant algorithm is inspired by ant-colony optimization.

Instead of selecting the next communication cell using only instantaneous signal strength, the algorithm maintains a virtual pheromone score that reflects historical network quality.

Each candidate network accumulates a pheromone value based on:

* signal quality
* packet loss
* latency
* handover stability
* historical reward

The network with the highest combined score becomes the preferred handover target.

---

## Reward Function

The reward function evaluates communication quality.

Reward is calculated using:

Reward = w1 × SignalQuality
- w2 × PacketLoss
- w3 × Delay
- w4 × HandoverCost

Where:

* SignalQuality represents link quality
* PacketLoss represents communication reliability degradation
* Delay represents network latency
* HandoverCost penalizes excessive switching

The weighting factors can be adjusted depending on mission requirements.

---

## Pheromone Update

After each communication interval, the pheromone value is updated.

Positive communication outcomes increase pheromone values.

Negative communication outcomes reduce pheromone values.

Pheromone Update:

τ(t+1) = (1 - ρ)τ(t) + Δτ

Where:

* τ = pheromone value
* ρ = evaporation factor
* Δτ = reward contribution

This mechanism enables long-term learning behavior.

---

## Predictive Ghost Ant Extension

The Predictive Ghost Ant model extends the original algorithm.

Future network quality is estimated before a handover occurs.

Predicted values include:

* future signal quality
* future latency
* future packet loss

The handover decision uses both:

* current network quality
* predicted network quality

This reduces unnecessary handovers and improves stability.

---

## Decision Flow

Network Observation
→ Reward Evaluation
→ Pheromone Update
→ Future Quality Prediction
→ Candidate Ranking
→ Handover Decision
→ Performance Logging

---

## Evaluation Metrics

The proposed method is evaluated using:

* Average Delay
* Packet Loss Rate
* Handover Count
* Communication Stability Score

These metrics are compared against baseline handover methods.
