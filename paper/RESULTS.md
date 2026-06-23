# Results

## Overview

The proposed Ghost Ant and Predictive Ghost Ant methods were evaluated against a traditional threshold-based handover strategy.

The comparison focused on:

* communication delay
* packet loss
* handover frequency
* communication stability

Experimental results were generated using the UAM communication simulator.

---

## Delay Analysis

The delay comparison results are summarized in:

* results/delay_comparison.png

### Observation

The Ghost Ant approach reduced average communication delay compared to the baseline method.

The Predictive Ghost Ant extension achieved the lowest delay among all evaluated approaches.

### Interpretation

The pheromone-based decision process reduces unnecessary network switching and allows the system to remain connected to more stable communication links.

---

## Packet Loss Analysis

The packet-loss comparison results are summarized in:

* results/packet_loss_comparison.png

### Observation

Both Ghost Ant methods produced lower packet-loss rates than the conventional threshold-based handover method.

The Predictive Ghost Ant method achieved the best overall performance.

### Interpretation

By considering historical communication quality, the proposed approach avoids unstable communication cells that would otherwise increase packet loss.

---

## Handover Frequency Analysis

The handover comparison results are summarized in:

* results/handover_comparison.png

### Observation

The baseline method performed frequent network switching.

Ghost Ant reduced unnecessary handovers.

Predictive Ghost Ant further reduced handover frequency while maintaining communication quality.

### Interpretation

Reducing excessive handovers improves communication continuity and decreases the risk of service interruption.

---

## Pheromone Distribution

The pheromone distribution is visualized in:

* results/pheromone_map.png

### Observation

High-quality communication cells accumulated larger pheromone values.

Low-quality communication cells gradually lost pheromone influence through evaporation.

### Interpretation

The pheromone mechanism enables the system to retain historical communication experience and improve future decisions.

---

## UAM Trajectory Evaluation

Trajectory visualization is available in:

* results/uam_trajectory.png
* results/uam_animation.gif

### Observation

The UAM successfully traversed multiple communication regions while continuously evaluating network quality.

The proposed approach maintained stable communication behavior throughout the simulated mission.

---

## Comparative Summary

| Metric         | Baseline | Ghost Ant | Predictive Ghost Ant |
| -------------- | -------- | --------- | -------------------- |
| Delay          | Higher   | Lower     | Lowest               |
| Packet Loss    | Higher   | Lower     | Lowest               |
| Handover Count | Higher   | Lower     | Lowest               |
| Stability      | Lower    | Higher    | Highest              |

---

## Key Findings

The experimental results indicate that:

1. Historical communication quality can improve handover decisions.
2. Pheromone-based scoring reduces unnecessary network switching.
3. Predictive evaluation further improves communication stability.
4. The proposed method demonstrates potential for future UAM communication systems.

---

## Discussion

The results suggest that communication-aware handover strategies may outperform simple threshold-based methods in highly dynamic UAM environments.

Although the current implementation is simulation-based, the observed trends support further investigation using more realistic wireless-network models and flight-test environments.
