# Python Decorators: `@`

## Why I Studied This

During the technical review, I realized that I need to understand Python syntax that appears in my own project.

One important example is the `@` symbol.

In this project, `@dataclass` is used in `predictive_ghost_ant.py`.

---

## What is `@` in Python?

In Python, `@` is used for a **decorator**.

A decorator is a way to add behavior to a function or class without rewriting the whole function or class.

In simple words:

```text
Decorator = a wrapper that adds extra behavior
```

---

## Example

```python
@dataclass
class UAVState:
    position: tuple
    velocity: tuple
```

This means:

```text
Apply dataclass behavior to UAVState.
```

`@dataclass` automatically creates useful methods such as:

- `__init__`
- `__repr__`
- `__eq__`

---

## Why `@dataclass` is Useful

Without `@dataclass`, I would need to write:

```python
class UAVState:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
```

With `@dataclass`, I can write:

```python
@dataclass
class UAVState:
    position: tuple
    velocity: tuple
```

This makes the code shorter and easier to read.

---

## Connection to Ghost Ant Handover

In this project, `@dataclass` is used for:

- `UAVState`
- `FutureCandidateCell`

These classes mainly store data.

They do not need complex behavior.

That is why `@dataclass` is suitable.

---

## My Explanation

`@dataclass` is like saying:

> "This class is mostly used to store data. Please generate the basic constructor automatically."

---

## Interview Lesson

If I use syntax like `@dataclass`, I must be able to explain why it is used.

Using convenient syntax without understanding it makes the code look artificial.