# Ghost Ant Handover

**UAM Communication Handover Optimization Research**  
Reward Function · Ant-Colony-Inspired Scoring · Predictive Handover · Simulation Dashboard

![Status](https://img.shields.io/badge/status-Research%20Prototype-blue)
![Focus](https://img.shields.io/badge/focus-UAM%20Handover-22314E)
![Method](https://img.shields.io/badge/method-Reward%20Function%20%2B%20ACO%20Inspired-orange)
![Language](https://img.shields.io/badge/language-Python-3776AB)

---

## Overview

**Ghost Ant Handover** is a research-oriented simulation project for UAM communication handover optimization.

The project explores how a flying vehicle can choose a more stable communication cell while moving through multiple network zones.

The core idea is:

> Do not choose a network only by the current signal.  
> Predict the future position, evaluate candidate cells, and select a more stable connection.

This repository focuses on:

- UAM movement simulation
- candidate base-station evaluation
- reward-based handover decision
- ant-colony-inspired score update
- predictive future-position evaluation
- quantitative evaluation
- dashboard visualization

---

## Problem

UAM vehicles may pass through multiple wireless network zones during flight.

Poorly timed handovers can cause:

- unstable connection
- increased latency
- packet loss
- unnecessary switching
- mission risk

The key questions are:

- When should the system switch networks?
- Which network should it choose?
- How can unnecessary handovers be reduced?
- How can future network quality be considered?

---

## System Architecture

```text
UAM Movement
        ↓
Current Position / Velocity
        ↓
Future Position Prediction
        ↓
Candidate Base Station Generation
        ↓
Signal / Delay / Packet Loss Estimation
        ↓
Reward Calculation
        ↓
Pheromone Preference Update
        ↓
Candidate Ranking
        ↓
Selected Cell
        ↓
Simulation Log
        ↓
Evaluation Report / Dashboard
```

---

## Why Ant Colony?

Ant Colony Optimization, or ACO, is inspired by how ants find efficient paths using pheromone trails.

In real ant behavior:

- ants explore multiple paths
- better paths receive stronger pheromone feedback
- weak paths gradually lose influence
- future ants are more likely to follow stronger paths

This project does **not** implement a full production-grade ACO algorithm.

Instead, it borrows the core idea of **feedback-based path preference** and applies it to UAM network handover.

In this project:

- each candidate base station is treated like a possible communication path
- better communication conditions increase the score
- unstable communication conditions reduce the score
- previous decisions can influence future selection
- the system tries to avoid unnecessary switching

The goal is not to perfectly reproduce biological ant behavior.

The goal is to use the ant-colony concept as a simple decision model for repeated network selection.

---

## What "Ghost Ant" Means

The word **Ghost Ant** means a virtual exploration process.

Before the real UAM reaches the next position, the algorithm predicts a future position and evaluates candidate cells in advance.

```text
Current UAM Position
        ↓
Predict Future Position
        ↓
Evaluate Candidate Cells
        ↓
Choose Better Cell Before Quality Drops
```

This is why the project is called **Ghost Ant**.

It is like sending a virtual ant ahead of the UAM path to check which communication cell may become more stable.

---

## Decision Flow

```text
1. Move UAM
2. Read current position and velocity
3. Predict future position
4. Build candidate base stations
5. Estimate signal quality
6. Estimate delay and packet loss
7. Calculate reward
8. Add pheromone preference
9. Apply handover cost
10. Select best cell
11. Save simulation log
12. Generate evaluation summary
```

---

## Reward and Pheromone Concept

The decision score is based on two ideas.

### 1. Reward

Reward represents communication quality.

Possible reward factors:

- signal strength
- delay
- packet loss
- vehicle speed
- movement direction
- handover cost
- connection stability
- predicted future network quality

### 2. Pheromone

Pheromone represents accumulated preference from previous decisions.

It is used to make the system remember which paths or cells were repeatedly useful.

A simplified decision idea is:

```text
Decision Score = Reward + Pheromone Score - Handover Cost
```

This makes the algorithm prefer cells that are not only good at the current moment, but also stable across repeated simulation steps.

---

## Main Modules

```text
src/
├── ghost_ant.py              # Basic handover decision logic
├── predictive_ghost_ant.py   # Future-position-based Ghost Ant logic
├── pheromone.py              # Simplified pheromone preference map
├── reward.py                 # Reward calculation logic
├── adaptive_handover.py      # Adaptive handover concept
└── dynamic_weight.py         # Dynamic weighting concept
```

---

## Simulation Modules

```text
simulation/
├── uam.py                    # UAM position and movement model
├── environment.py            # Base-station environment generation
├── cell.py                   # Signal, delay, packet-loss estimation
├── metrics.py                # Metric calculation support
└── compare_modes.py          # Comparison between handover strategies
```

---

## Scripts

```text
scripts/
├── uam_simulation.py         # Main UAM simulation runner
├── evaluate_results.py       # Quantitative evaluation summary
├── visualize_pheromone.py    # Pheromone map visualization
├── generate_comparison_table.py
├── demo.py
├── ghost_demo.py
├── handover_demo.py
└── predictive_demo.py
```

---

## Results

The repository includes simulation outputs and comparison visualizations.

```text
results/
├── uam_simulation_log.csv
├── evaluation_summary.md
├── uam_trajectory.png
├── handover_comparison.png
├── delay_comparison.png
├── packet_loss_comparison.png
├── pheromone_map.png
└── comparison_summary.md
```

Current evaluation metrics include:

- average reward
- average delay
- average packet loss
- handover count
- stability score
- selected cell usage

---

## Study Notes

This repository also includes study notes written while reviewing and understanding the implementation.

The purpose is to document the concepts behind the code, not just the final result.

```text
study/
├── python/          # Python language concepts used in this project
├── wireless/        # Communication and handover-related concepts
└── algorithms/      # Reward, prediction, and ant-colony-inspired logic
```

Current study topics:

* `__init__.py` and Python package structure
* `@dataclass` and Python decorators
* `return max(...)` and minimum safety values
* RSRP and wireless signal quality
* reward function design
* ant-colony-inspired feedback logic
* predictive handover decision flow

These notes are part of the process of moving from "building a project" to "understanding and explaining the system."


---
## Run Demo

Run all simulations:

```bash
./run_all.sh
```

Run main simulation:

```bash
python3 scripts/uam_simulation.py
```

Run evaluation:

```bash
python3 scripts/evaluate_results.py
```

Run dashboard:

```bash
streamlit run dashboard.py
```

---

## Project Structure

```text
ghost-ant-handover/
├── docs/             # Mathematical model, reward function, system design
├── paper/            # Paper-style draft sections
├── research/         # Ghost Ant and predictive handover notes
├── results/          # Simulation outputs and figures
├── scripts/          # Demo, visualization, and simulation scripts
├── simulation/       # Environment and UAM simulation modules
├── src/              # Reward, pheromone, handover, and prediction logic
├── dashboard.py      # Streamlit dashboard prototype
└── run_all.sh        # Full simulation runner
```

---

## Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit
- Simulation logic
- Reward modeling
- Ant-colony-inspired scoring
- Predictive handover concept

---

## Current Status

Ghost Ant Handover is currently a research prototype.

Implemented or partially implemented:

- UAM trajectory simulation
- reward-based handover logic
- predictive Ghost Ant logic
- pheromone map visualization
- comparison result generation
- quantitative evaluation summary
- Streamlit dashboard prototype
- paper-style documentation

---

## Research Direction

Next research steps:

- formalize the pheromone update equation
- compare with baseline handover methods
- improve wireless channel assumptions
- add more realistic UAM movement scenarios
- evaluate handover stability over longer simulations
- prepare a paper-style technical report

---

## Limitations

Current limitations:

- simulation assumptions are simplified
- real UAM communication data is not used
- wireless channel model is not production-grade
- pheromone update rule is simplified
- handover model is research-oriented
- not validated for real flight communication systems

This project is not a certified UAM communication controller or production-grade handover system.

---

## Author

Lee Youngjun  
Department of Computer Science, Paejae University  
GitHub: [@gxmzung](https://github.com/gxmzung)

---

## Disclaimer

This repository is a research and simulation prototype.

It is not a certified UAM communication controller, telecom product, or production-grade network handover system.
