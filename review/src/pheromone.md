# Code Review: `src/pheromone.py`

## Original Code

```python
import numpy as np


class PheromoneMap:
    def __init__(self, x=20, y=20, z=5, evaporation=0.95):
        self.map = np.ones((x, y, z))
        self.evaporation = evaporation

    def evaporate(self):
        self.map *= self.evaporation

    def deposit(self, x, y, z, amount):
        self.map[x, y, z] += amount

    def get(self, x, y, z):
        return self.map[x, y, z]
```

---

## Purpose

This file defines the pheromone map used in the Ghost Ant handover model.

The pheromone map stores preference values for positions in a 3D space.

In this project, pheromone means:

> A stored preference score that can influence future cell-selection decisions.

---

## Why This File Exists

Ghost Ant Handover borrows the concept of Ant Colony Optimization.

In ant behavior, pheromone trails help future ants prefer paths that worked well before.

In this project, the pheromone map helps the algorithm remember which regions or paths were previously useful.

---

## Import

```python
import numpy as np
```

This imports NumPy.

NumPy is used because the pheromone map is stored as a 3D array.

A normal Python list could work, but NumPy is faster and easier for numerical operations.

---

## Class: `PheromoneMap`

```python
class PheromoneMap:
```

This class manages the pheromone values.

It does not directly decide handovers.

It only stores, updates, and returns pheromone scores.

---

## Constructor

```python
def __init__(self, x=20, y=20, z=5, evaporation=0.95):
```

This function runs when a new `PheromoneMap` object is created.

### Parameters

- `x`: size of the map on the x-axis
- `y`: size of the map on the y-axis
- `z`: size of the map on the z-axis
- `evaporation`: rate used to reduce pheromone values over time

---

## Map Initialization

```python
self.map = np.ones((x, y, z))
```

This creates a 3D NumPy array filled with `1`.

Example:

```text
x = 20
y = 20
z = 5
```

means the pheromone map has:

```text
20 × 20 × 5 = 2000 cells
```

Each cell starts with a pheromone value of `1`.

This means every position starts with the same neutral preference.

---

## Evaporation Rate

```python
self.evaporation = evaporation
```

This stores the evaporation rate.

The default value is:

```text
0.95
```

This means the pheromone value keeps 95% of its previous value after evaporation.

Example:

```text
1.00 → 0.95 → 0.9025 → 0.8573
```

The value slowly decreases over time.

---

## Method: `evaporate`

```python
def evaporate(self):
    self.map *= self.evaporation
```

This reduces all pheromone values.

It simulates pheromone evaporation.

In Ant Colony Optimization, old paths should gradually lose influence.

If this did not exist, old decisions could dominate forever.

---

## Method: `deposit`

```python
def deposit(self, x, y, z, amount):
    self.map[x, y, z] += amount
```

This adds pheromone to a specific location.

### Meaning

If a position or path is considered useful, the algorithm can increase its pheromone value.

That location becomes more preferred in future decisions.

---

## Method: `get`

```python
def get(self, x, y, z):
    return self.map[x, y, z]
```

This returns the pheromone value at a specific position.

The handover algorithm can use this value as part of the candidate-cell score.

---

## Explanation in My Words

`PheromoneMap` is the memory layer of the Ghost Ant model.

Reward tells the system:

> Which cell looks good now?

Pheromone tells the system:

> Which region or path has been useful before?

Together, reward and pheromone help the algorithm avoid making every decision from scratch.

---

## Design Advantages

- Simple structure
- Easy to visualize
- Easy to update
- Works naturally with simulation grids
- Makes the ant-colony concept explainable

---

## Current Limitations

This implementation is simplified.

Current limitations:

- no boundary check for `x`, `y`, `z`
- no maximum pheromone limit
- no minimum pheromone limit
- evaporation rate is fixed
- deposit amount is manually controlled
- not a complete ACO implementation

---

## Future Improvements

Possible improvements:

- add boundary checking
- add minimum and maximum pheromone values
- make evaporation dynamic
- connect deposit amount to reward score
- compare with standard ACO pheromone equations
- visualize pheromone changes over time

---

## Interview Lesson

This file showed me that even simple code needs explanation.

The important question is not only:

> What does this code do?

but also:

> Why does this structure exist in the system?