# Wireless Metric: RSRP

## Why I Studied This

Ghost Ant Handover uses wireless communication quality as part of the handover decision.

During the review, I realized that I need to understand the meaning of wireless metrics instead of using them as abstract numbers.

One important metric is **RSRP**.

---

## What is RSRP?

RSRP means:

```text
Reference Signal Received Power
```

It represents the received power of a reference signal from a base station.

In simple words:

```text
RSRP = how strong the base-station signal is
```

---

## Typical RSRP Interpretation

RSRP is usually measured in dBm.

Typical values:

```text
-70 dBm   very strong
-85 dBm   good
-95 dBm   normal
-105 dBm  weak
-115 dBm  very weak
```

A value closer to 0 is stronger.

For example:

```text
-70 dBm is stronger than -100 dBm
```

---

## Why RSRP Matters for Handover

If a UAM moves away from one base station, the RSRP from that station may decrease.

If another base station has stronger RSRP, the system may consider switching to that station.

However, RSRP alone is not enough.

A cell with strong signal can still have:

- high delay
- packet loss
- unstable connection
- bad future position quality

---

## RSRP in Ghost Ant Handover

In this project, RSRP is one part of the reward function.

```python
alpha * rsrp
```

Higher RSRP increases reward.

But the final score also considers:

- LOS
- handover cost
- delay
- packet loss

This is important because the algorithm should not choose a cell only because its current signal is strong.

---

## Related Metrics

## RSRQ

Reference Signal Received Quality.

It represents signal quality, not just signal strength.

---

## SINR

Signal to Interference plus Noise Ratio.

It represents how clean the signal is compared to interference and noise.

---

## LOS

Line Of Sight.

It means whether there is a clear path between the transmitter and receiver.

In this project, LOS is simplified as a score.

---

## My Explanation

RSRP is like checking how loud a speaker sounds from far away.

But loudness alone is not enough.

If there is too much noise, delay, or interruption, communication may still be bad.

That is why Ghost Ant uses RSRP together with delay, packet loss, LOS, and handover cost.

---

## Interview Lesson

When I use a metric in code, I should understand what it means in the real system.

A variable name is not enough.

I need to explain the engineering meaning behind it.