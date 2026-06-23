# Experiment

## Experimental Objective

The objective of this experiment is to evaluate whether the proposed Ghost Ant handover strategy can improve communication quality compared to conventional handover approaches.

The evaluation focuses on:

* communication latency
* packet loss
* handover frequency
* communication stability

---

## Simulation Environment

The simulation environment represents a UAM vehicle moving through multiple communication cells.

The environment includes:

* multiple network cells
* dynamic signal quality
* communication delay variation
* packet-loss events
* UAM trajectory movement

The simulator continuously evaluates network conditions while the UAM travels through the mission area.

---

## Compared Methods

### Baseline Method

A traditional threshold-based handover approach.

Decision rule:

* choose the network with the strongest signal
* trigger handover when signal strength falls below a threshold

### Ghost Ant Method

The proposed pheromone-based decision model.

Decision factors:

* signal quality
* packet loss
* latency
* historical communication performance

### Predictive Ghost Ant Method

Extended version of Ghost Ant.

Additional factors:

* predicted future signal quality
* predicted future packet loss
* predicted future latency

---

## Evaluation Metrics

### Average Delay

Measures the average communication latency during the mission.

Lower values are better.

---

### Packet Loss Rate

Measures the percentage of lost packets.

Lower values are better.

---

### Handover Count

Measures the total number of handovers.

Excessive handovers indicate instability.

Lower values are preferred.

---

### Stability Score

A combined metric representing overall communication quality.

Higher values indicate better communication performance.

---

## Test Scenario

The UAM follows a predefined flight path.

During the mission:

* signal quality changes continuously
* network congestion occurs randomly
* packet loss events are introduced
* communication cells overlap

The handover algorithm must continuously determine the best network.

---

## Data Collection

The simulator records:

* timestamp
* selected network
* signal quality
* delay
* packet loss
* reward value
* pheromone value
* handover event

The collected logs are stored in CSV format for analysis.

---

## Visualization

The experiment generates the following outputs:

* delay comparison graph
* packet loss comparison graph
* handover comparison graph
* pheromone map visualization
* UAM trajectory visualization

These visualizations are used to compare baseline and proposed methods.

---

## Reproducibility

All experiments can be reproduced using the provided simulation scripts.

Main scripts:

* simulation/compare_modes.py
* scripts/uam_simulation.py
* scripts/generate_comparison_table.py

The same simulation environment is used for all evaluated methods.
