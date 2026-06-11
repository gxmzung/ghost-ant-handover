#!/bin/bash

echo "======================================"
echo " Ghost Ant Handover Full Pipeline"
echo "======================================"

echo "[1/5] Running reward demo..."
PYTHONPATH=. python3 scripts/demo.py

echo "[2/5] Running handover demo..."
PYTHONPATH=. python3 scripts/handover_demo.py

echo "[3/5] Running UAM simulation..."
PYTHONPATH=. python3 scripts/uam_simulation.py

echo "[4/5] Generating report..."
PYTHONPATH=. python3 scripts/generate_report.py

echo "[5/5] Generating animation..."
PYTHONPATH=. python3 scripts/animate_uam.py

echo "======================================"
echo " Pipeline completed."
echo " Check results/ directory."
echo "======================================"
