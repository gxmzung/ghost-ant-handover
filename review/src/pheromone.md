# Code Review: `src/pheromone.py`

## Purpose

This module manages the pheromone values used in the Ghost Ant handover model.

Instead of making decisions from only the current network quality, the algorithm also remembers previous successful communication paths.

---

## Why This File Exists

One of the main ideas of Ghost Ant is inspired by Ant Colony Optimization (ACO).

Rather than treating every decision independently, previous successful paths influence future decisions.

This file is responsible for storing and updating that preference.

---

## Core Concept

```text
Candidate Cell
        │
        ▼
Reward Evaluation
        │
        ▼
Pheromone Update
        │
        ▼
Higher Preference
        │
        ▼
Future Candidate Selection
```

---

## Main Responsibilities

- Store pheromone values
- Increase pheromone for successful paths
- Reduce pheromone over time (evaporation)
- Provide pheromone score to the handover algorithm

---

## Why Pheromone?

Real ants gradually discover efficient paths through repeated exploration.

This project borrows that idea.

Good communication paths become more preferred, while unstable paths gradually lose importance.

---

## My Understanding

The pheromone value is **not** the final decision.

It is only one component of the decision score.

The final handover decision also considers:

- reward
- delay
- packet loss
- handover cost
- predicted future quality

---

## Current Limitation

This implementation uses a simplified pheromone model.

It is intended for simulation and learning rather than reproducing the complete Ant Colony Optimization algorithm.

---

## Future Improvement

- Dynamic evaporation rate
- Adaptive pheromone update
- Multi-agent simulation
- Comparison with standard ACO equations