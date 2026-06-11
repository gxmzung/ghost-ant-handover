# System Design

## Ghost Ant Based Adaptive Handover Framework

This project explores predictive handover optimization for VTOL/UAM communication.

## Problem

UAM and VTOL missions require stable communication links.
However, low-altitude urban flight can suffer from:

- RSRP fluctuation
- LoS blockage
- Frequent handover
- Communication delay
- Packet loss

In mission-critical flight, communication failure is directly related to mission failure.

## Core Idea

The proposed method uses a Ghost Ant lookahead mechanism to evaluate future candidate cells before the current link quality degrades.

## Architecture

1. UAM position update
2. Future position prediction
3. Candidate cell evaluation
4. Reward calculation
5. Pheromone map update
6. Adaptive handover decision

## Reward Function

Q = α·RSRP + β·LoS − γ·Handover − δ·Delay − ε·PacketLoss

## Expected Effect

- Reduced unnecessary handover
- Lower delay
- Lower packet loss
- More stable mission communication

## Future Integration

- ROS2
- PX4
- Gazebo simulation
- QGroundControl telemetry
