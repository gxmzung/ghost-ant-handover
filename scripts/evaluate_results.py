import pandas as pd
from pathlib import Path

LOG_PATH = Path("results/uam_simulation_log.csv")
OUT_PATH = Path("results/evaluation_summary.md")

def main():
    df = pd.read_csv(LOG_PATH)

    avg_reward = df["reward"].mean()
    avg_delay = df["delay_ms"].mean()
    avg_packet_loss = df["packet_loss"].mean()
    handover_count = int(df["handover"].sum())
    stability_score = avg_reward - avg_packet_loss - (avg_delay / 100)

    cell_usage = df["selected_cell"].value_counts()

    md = f"""# Evaluation Summary

## Overview

This document summarizes the current Ghost Ant UAM handover simulation results.

## Metrics

| Metric | Value |
|---|---:|
| Samples | {len(df)} |
| Average Reward | {avg_reward:.4f} |
| Average Delay ms | {avg_delay:.4f} |
| Average Packet Loss | {avg_packet_loss:.4f} |
| Handover Count | {handover_count} |
| Stability Score | {stability_score:.4f} |

## Selected Cell Usage

{cell_usage.to_markdown()}

## Interpretation

The current simulation log includes reward, delay, packet loss, and handover event information.

This allows the project to move from qualitative explanation to quantitative evaluation.

## Current Boundary

The current evaluation is based on a simplified simulation environment.

It is not validated with real UAM communication data.
"""

    OUT_PATH.write_text(md)
    print(f"saved: {OUT_PATH}")

if __name__ == "__main__":
    main()
