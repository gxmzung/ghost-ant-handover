# Ghost Ant Handover

UAM communication handover optimization research using reward-based network selection and ant-colony-inspired decision logic.

## Overview

Ghost Ant Handover is a research-oriented project about UAM communication handover.

The core idea is simple:

> When a flying vehicle moves through different network zones, it should choose the most stable and efficient connection based on signal quality, movement, delay, and switching cost.

## Problem

UAM vehicles may move across multiple communication zones.  
Frequent handovers can cause instability, delay, or connection loss.

The challenge is to decide:

- When should the system switch networks?
- Which network should it choose?
- How can unnecessary handovers be reduced?

## Core Concept

The handover decision is based on a reward function.

Possible factors:

- Signal strength
- Latency
- Packet loss
- Vehicle speed
- Direction
- Handover cost
- Connection stability

## Why Ant Colony?

Ant Colony Optimization is useful as a conceptual model because it explains how distributed agents can find efficient paths through repeated feedback.

In this project, the idea is applied to network selection:

- Better network paths receive higher scores
- Unstable paths lose priority
- The system gradually improves handover decisions

## Current Status

- Research concept
- Reward function design
- Simulation planning
- UAM communication scenario definition

## Roadmap

### v0.1
- Problem definition
- Reward function draft

### v0.5
- Simulation model
- Network switching scenario

### v1.0
- Handover decision dashboard
- Comparative analysis

---

## Research Motivation

Communication failure is not just a network problem.

It becomes a mission failure.

---

## Reward Function

Q = α·RSRP + β·LoS − γ·Handover − δ·Delay − ε·PacketLoss

---

## Core Components

- Ghost Ant Lookahead
- 3D Pheromone Map
- Adaptive Handover
- Dynamic Weight
- VTOL/UAM Connectivity
- Packet Loss Optimization

---

## Future Work

- [x] Reward Function
- [x] Initial Prototype
- [ ] Dynamic Weight
- [ ] Ghost Ant Prediction
- [ ] 3D Pheromone Map
- [ ] ROS2 Simulation
- [ ] PX4 Integration
- [ ] Gazebo Evaluation

---

## Repository Structure

```
docs/
research/
simulation/
scripts/
src/
tests/
```

---

## Status

Research Prototype (v0.1)
---

## Simulation Results

### Handover Comparison

![Handover Comparison](results/handover_comparison.png)

### Delay Comparison

![Delay Comparison](results/delay_comparison.png)

### Packet Loss Comparison

![Packet Loss Comparison](results/packet_loss_comparison.png)

---

## Modes

### Baseline
Conventional reactive handover strategy.

### ACO
Ant Colony Optimization based handover decision.

### Ghost Ant
Lookahead-based predictive handover with reduced unnecessary switching.


---

## UAM Trajectory Simulation

### UAM Path and Base Stations

![UAM Trajectory](results/uam_trajectory.png)

### Simulation Log

The UAM simulation exports step-by-step selected cells, future predicted positions, and reward values.

```text
results/uam_simulation_log.csv

---

## Comparison Summary

The framework compares three strategies:

- Baseline
- ACO
- Ghost Ant

See:

```text
results/comparison_summary.md

---

## UAM Simulation Animation

![UAM Animation](results/uam_animation.gif)

