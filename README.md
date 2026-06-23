# Ghost Ant Handover

**UAM Communication Handover Optimization Research**  
Reward Function · Ant Colony Concept · Predictive Handover · Simulation Dashboard

![Status](https://img.shields.io/badge/status-Research%20Prototype-blue)
![Focus](https://img.shields.io/badge/focus-UAM%20Handover-22314E)
![Method](https://img.shields.io/badge/method-Reward%20Function%20%2B%20ACO-orange)
![Language](https://img.shields.io/badge/language-Python-3776AB)

---

## Overview

**Ghost Ant Handover** is a research-oriented simulation project for UAM communication handover optimization.

The core idea is simple:

> When a flying vehicle moves through multiple communication zones, it should choose the most stable network based on signal quality, delay, packet loss, movement, and handover cost.

This repository explores reward-based network selection and ant-colony-inspired decision logic through simulation, visualization, comparison metrics, and dashboard prototypes.

---

## Problem

UAM vehicles may pass through multiple wireless network zones during flight.

Frequent or poorly timed handovers can cause:

- unstable connection
- increased latency
- packet loss
- unnecessary switching
- mission risk

The key questions are:

- When should the system switch networks?
- Which network should it choose?
- How can unnecessary handovers be reduced?
- How can network quality be evaluated over time?

---

## Core Concept

Ghost Ant Handover combines:

```text
UAM Movement
        ↓
Network Quality Observation
        ↓
Reward Function
        ↓
Ant-Colony-Inspired Score Update
        ↓
Predictive Handover Decision
        ↓
Comparison Metrics
Reward Function

The handover decision is based on multiple factors.

Possible reward factors:

Signal strength
Latency
Packet loss
Vehicle speed
Movement direction
Handover cost
Connection stability
Predicted future network quality

The reward function is designed to reduce unstable or unnecessary handovers while keeping the UAM connected to a reliable network.

More details:

Reward Function
Mathematical Model
Why Ant Colony?

Ant Colony Optimization is useful as a conceptual model because it explains how distributed agents can find efficient paths through repeated feedback.

In this project, the concept is adapted to network selection:

Better network paths receive higher scores
Unstable paths lose priority
Past decisions influence future selection
Repeated simulation improves route-quality understanding

This is not a full production-grade ACO network controller.
It is a research prototype for handover decision modeling.

Simulation Results

The repository includes simulation outputs and comparison visualizations.

UAM Trajectory

Handover Comparison

Delay Comparison

Packet Loss Comparison

Pheromone Map

Run Demo
Run all simulations
./run_all.sh
Run main simulation
python3 scripts/uam_simulation.py
Run dashboard
streamlit run dashboard.py
Project Structure
ghost-ant-handover/
├── docs/             # Mathematical model, reward function, system design
├── research/         # Ghost Ant and predictive handover notes
├── results/          # Simulation outputs and figures
├── scripts/          # Demo, visualization, and simulation scripts
├── simulation/       # Environment and UAM simulation modules
├── src/              # Reward, pheromone, handover, and prediction logic
├── dashboard.py      # Streamlit dashboard prototype
└── run_all.sh        # Full simulation runner
Tech Stack
Python
Streamlit
Matplotlib
Simulation logic
Reward modeling
Ant-colony-inspired scoring
Predictive handover concept
Current Status

Ghost Ant Handover is currently a research prototype.

Implemented or partially implemented:

UAM trajectory simulation
Reward-based handover logic
Predictive Ghost Ant logic
Pheromone map visualization
Comparison result generation
Streamlit dashboard prototype
Research documentation
Roadmap
v0.1 — Problem Definition
Define UAM handover problem
Draft reward function
Build basic simulation environment
v0.5 — Simulation and Metrics
Add UAM movement simulation
Compare handover strategies
Generate delay / packet loss / handover count metrics
v1.0 — Predictive Ghost Ant
Add predictive handover logic
Improve pheromone scoring
Add dashboard visualization
Document mathematical model
v2.0 — Research Paper Direction
Formalize model assumptions
Compare with baseline methods
Improve scenario generation
Prepare paper-style report
Limitations

Current limitations:

Simulation assumptions are simplified
Real UAM communication data is not used
Wireless channel model is not production-grade
Handover model is research-oriented
Not validated for real flight communication systems
Author

Lee Youngjun
Department of Computer Science, Paejae University
GitHub: @gxmzung

Disclaimer

This repository is a research and simulation prototype.

It is not a certified UAM communication controller or production-grade handover system.
