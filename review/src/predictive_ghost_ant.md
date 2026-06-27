# Code Review: `src/predictive_ghost_ant.py`

## Original Code

```python
from dataclasses import dataclass
from typing import List, Tuple

from src.reward import calculate_reward
from src.pheromone import PheromoneMap


@dataclass
class UAVState:
    position: Tuple[int, int, int]
    velocity: Tuple[int, int, int]


@dataclass
class FutureCandidateCell:
    cell_id: str
    x: int
    y: int
    z: int
    rsrp: float
    los: float
    delay: float
    packet_loss: float
    handover: float


class PredictiveGhostAnt:
    def __init__(self, pheromone_map: PheromoneMap, lookahead_steps: int = 5):
        self.pheromone_map = pheromone_map
        self.lookahead_steps = lookahead_steps

    def predict_future_position(self, state: UAVState) -> Tuple[int, int, int]:
        x, y, z = state.position
        vx, vy, vz = state.velocity

        return (
            x + vx * self.lookahead_steps,
            y + vy * self.lookahead_steps,
            z + vz * self.lookahead_steps,
        )

    def evaluate_candidate(self, candidate: FutureCandidateCell) -> float:
        return calculate_reward(
            rsrp=candidate.rsrp,
            los=candidate.los,
            handover=candidate.handover,
            delay=candidate.delay,
            packet_loss=candidate.packet_loss,
            alpha=1.0,
            beta=1.2,
            gamma=0.8,
            delta=0.7,
            epsilon=1.5,
        )

    def virtual_explore(self, state: UAVState, candidates: List[FutureCandidateCell]):
        if not candidates:
            raise ValueError("candidates must not be empty")

        future_position = self.predict_future_position(state)

        scored_candidates = []

        for candidate in candidates:
            reward = self.evaluate_candidate(candidate)

            self.pheromone_map.deposit(
                candidate.x,
                candidate.y,
                candidate.z,
                reward,
            )

            scored_candidates.append((candidate, reward))

        best_candidate, best_reward = max(scored_candidates, key=lambda item: item[1])

        return {
            "future_position": future_position,
            "best_cell": best_candidate.cell_id,
            "best_reward": best_reward,
        }
```

---

## Purpose

This file contains the main predictive decision logic of the Ghost Ant Handover project.

It predicts the future position of the UAM, evaluates candidate communication cells, updates pheromone values, and selects the best cell based on reward.

---

## Code-by-Code Summary

```text
dataclass
    ↓
Define simple data containers for UAV state and candidate cells.

UAVState
    ↓
Stores current position and velocity.

FutureCandidateCell
    ↓
Stores candidate communication-cell data.

PredictiveGhostAnt
    ↓
Main predictive handover decision class.

predict_future_position()
    ↓
Estimates where the UAM will be after lookahead steps.

evaluate_candidate()
    ↓
Converts candidate-cell quality into a reward score.

virtual_explore()
    ↓
Evaluates all candidates, updates pheromone, and selects the best cell.
```

The most important flow is:

```text
Current UAV State
        ↓
Future Position Prediction
        ↓
Candidate Cell Evaluation
        ↓
Reward Calculation
        ↓
Pheromone Deposit
        ↓
Best Cell Selection
```

---

## Why This File Exists

A normal handover decision can choose a cell based only on the current signal condition.

However, a UAM is moving.

A cell that looks good now may become worse after a few seconds.

This file exists to add a prediction step before making the handover decision.

The key idea is:

```text
Current Position
        ↓
Predict Future Position
        ↓
Evaluate Candidate Cells
        ↓
Select Better Cell
```

---

## Import Section

```python
from dataclasses import dataclass
from typing import List, Tuple
```

### `dataclass`

`dataclass` helps define simple data containers without writing a full constructor manually.

It is useful when a class mainly stores values.

### `List`, `Tuple`

These are type hints.

They make the code easier to understand.

For example:

```python
Tuple[int, int, int]
```

means a tuple with three integer values, such as:

```python
(2, 3, 1)
```

---

## Project Imports

```python
from src.reward import calculate_reward
from src.pheromone import PheromoneMap
```

This file uses two project modules:

- `calculate_reward`: calculates the score of a candidate cell
- `PheromoneMap`: stores accumulated preference values

This shows that `predictive_ghost_ant.py` is not isolated.

It connects reward logic and pheromone memory.

---

## Data Class: `UAVState`

```python
@dataclass
class UAVState:
    position: Tuple[int, int, int]
    velocity: Tuple[int, int, int]
```

`UAVState` stores the current state of the UAM.

It has two values:

- `position`: current 3D position
- `velocity`: movement direction and speed

Example:

```python
UAVState(
    position=(2, 2, 2),
    velocity=(1, 1, 0),
)
```

This means the UAM is currently at `(2, 2, 2)` and moves by `(1, 1, 0)` per step.

---

## Data Class: `FutureCandidateCell`

```python
@dataclass
class FutureCandidateCell:
    cell_id: str
    x: int
    y: int
    z: int
    rsrp: float
    los: float
    delay: float
    packet_loss: float
    handover: float
```

This class stores information about a candidate communication cell.

Each candidate has:

- ID
- position
- signal quality
- LOS score
- delay
- packet loss
- handover cost

This allows each candidate cell to be evaluated using the same reward function.

---

## Class: `PredictiveGhostAnt`

```python
class PredictiveGhostAnt:
```

This class controls the predictive exploration process.

It is called "Ghost Ant" because it virtually explores a future position before the real UAM reaches it.

---

## Constructor

```python
def __init__(self, pheromone_map: PheromoneMap, lookahead_steps: int = 5):
    self.pheromone_map = pheromone_map
    self.lookahead_steps = lookahead_steps
```

### `pheromone_map`

The pheromone map stores previous preference information.

It acts like memory.

### `lookahead_steps`

This controls how far into the future the algorithm predicts.

If `lookahead_steps = 5`, the algorithm predicts the UAM position after 5 movement steps.

---

## Method: `predict_future_position`

```python
def predict_future_position(self, state: UAVState) -> Tuple[int, int, int]:
    x, y, z = state.position
    vx, vy, vz = state.velocity

    return (
        x + vx * self.lookahead_steps,
        y + vy * self.lookahead_steps,
        z + vz * self.lookahead_steps,
    )
```

This method predicts where the UAM will be in the future.

Formula:

```text
future_position = current_position + velocity × lookahead_steps
```

Example:

```text
current_position = (2, 2, 2)
velocity = (1, 1, 0)
lookahead_steps = 5
```

Then:

```text
future_position = (7, 7, 2)
```

This is the predictive part of the project.

---

## Method: `evaluate_candidate`

```python
def evaluate_candidate(self, candidate: FutureCandidateCell) -> float:
    return calculate_reward(
        rsrp=candidate.rsrp,
        los=candidate.los,
        handover=candidate.handover,
        delay=candidate.delay,
        packet_loss=candidate.packet_loss,
        alpha=1.0,
        beta=1.2,
        gamma=0.8,
        delta=0.7,
        epsilon=1.5,
    )
```

This method converts candidate-cell information into one reward score.

It uses:

- RSRP
- LOS
- handover cost
- delay
- packet loss

The weights are not all equal.

```text
alpha = 1.0
beta = 1.2
gamma = 0.8
delta = 0.7
epsilon = 1.5
```

This means packet loss is penalized more strongly than delay or handover cost.

---

## Why Packet Loss Has a High Weight

```python
epsilon=1.5
```

Packet loss directly affects communication reliability.

For UAM communication, losing packets may be more dangerous than having a small delay.

That is why packet loss is given a stronger penalty in this simplified model.

---

## Method: `virtual_explore`

```python
def virtual_explore(self, state: UAVState, candidates: List[FutureCandidateCell]):
```

This is the main method of this file.

It performs the virtual exploration process.

---

## Empty Candidate Check

```python
if not candidates:
    raise ValueError("candidates must not be empty")
```

If there are no candidate cells, the algorithm cannot make a decision.

So the function stops early with an error.

This is a simple defensive programming pattern.

---

## Predict Future Position

```python
future_position = self.predict_future_position(state)
```

Before evaluating candidates, the algorithm predicts the future UAM position.

This is what makes the algorithm different from a purely current-state-based handover method.

---

## Candidate Evaluation Loop

```python
scored_candidates = []

for candidate in candidates:
    reward = self.evaluate_candidate(candidate)

    self.pheromone_map.deposit(
        candidate.x,
        candidate.y,
        candidate.z,
        reward,
    )

    scored_candidates.append((candidate, reward))
```

For each candidate cell:

1. Calculate reward
2. Deposit pheromone at the candidate position
3. Store the candidate and reward together

The structure is:

```text
Candidate Cell
        ↓
Reward Calculation
        ↓
Pheromone Update
        ↓
Candidate Score List
```

---

## Pheromone Deposit

```python
self.pheromone_map.deposit(
    candidate.x,
    candidate.y,
    candidate.z,
    reward,
)
```

This line connects reward and pheromone.

If the candidate gets a higher reward, more pheromone is deposited.

This means better candidate cells can influence future decisions more strongly.

---

## Selecting the Best Candidate

```python
best_candidate, best_reward = max(scored_candidates, key=lambda item: item[1])
```

This selects the candidate with the highest reward.

### What `key=lambda item: item[1]` means

Each item is:

```python
(candidate, reward)
```

`item[1]` means the reward value.

So this line means:

> Select the tuple with the highest reward.

Example:

```python
[
    ("BS-1", 1.2),
    ("BS-2", 2.1),
    ("BS-3", 0.8),
]
```

The best candidate is:

```python
("BS-2", 2.1)
```

---

## Return Value

```python
return {
    "future_position": future_position,
    "best_cell": best_candidate.cell_id,
    "best_reward": best_reward,
}
```

The function returns a dictionary with:

- predicted future position
- selected cell ID
- best reward value

This makes the result easy to log, print, or save into CSV.

---

## Explanation in My Words

`PredictiveGhostAnt` is the main decision unit of this project.

It does not only ask:

> Which cell is good now?

It asks:

> Which cell is likely to remain useful after the UAM moves?

That is why it predicts a future position and evaluates candidate cells before selecting the best one.

---

## Current Limitations

Current limitations:

- future position is predicted using a simple linear model
- pheromone is deposited but not used directly in final selection in this function
- candidate position is used for pheromone deposit, but future position is not directly used for candidate recalculation here
- weights are manually chosen
- no real wireless data is used
- no comparison with standard ACO equations yet

---

## Important Issue I Need to Improve

Currently, the function deposits pheromone based on reward:

```python
self.pheromone_map.deposit(candidate.x, candidate.y, candidate.z, reward)
```

However, the final selection uses only reward:

```python
max(scored_candidates, key=lambda item: item[1])
```

This means pheromone is being updated, but it is not yet fully used in the selection score inside this method.

A future improvement could combine reward and pheromone:

```text
final_score = reward + pheromone_score - handover_cost
```

This would make the ant-colony-inspired concept stronger.

---

## Future Improvements

- Use pheromone score directly in candidate selection
- Add boundary checks for candidate coordinates
- Use future position more directly when generating candidates
- Add dynamic reward weights
- Add baseline comparison
- Add unit tests
- Add real or semi-realistic wireless channel data

---

## Interview Lesson

This file taught me that the project idea alone is not enough.

I must be able to explain:

- what each class stores
- why prediction is needed
- how reward is calculated
- how pheromone is updated
- what is still incomplete

The goal is not only to build a prototype.

The goal is to understand and explain the system.