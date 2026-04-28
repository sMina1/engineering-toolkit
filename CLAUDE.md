# Engineering Toolkit

## Learning Context

This is a structured Python + Git training project for Mina (GitHub: sMina1). The goal is to learn Python, Git, and software engineering practices through building a real engineering toolkit. Tasks are guided by Claude Chat (concepts/planning) and Claude Code (hands-on coding).

When helping with this project: explain what functions and arguments do, teach rather than just implement, and tailor explanations to someone learning these tools for the first time.

## 6-Phase Training Plan

| Phase | Topic | Status |
|-------|-------|--------|
| 1 | Foundations — Unit Converter CLI (Python basics, first git repo) | Complete |
| 2 | Structure — Modules and Testing (packages, pytest, branching, PRs) | Complete |
| 3 | Data Handling — File I/O and Pandas (CSV, argparse, git stash) | Complete |
| 4 | Visualisation and Analysis (matplotlib, moving average, regression, git tags) | **In progress** — tasks 4.1–4.2 done, 4.3–4.5 remaining |
| 5 | OOP and Simulation (classes, inheritance, merge conflicts) | Not started |
| 6 | Integration — Engineering Dashboard (Streamlit/Flask web app) | Not started |

Current task: **4.3** — Linear regression with `numpy.polyfit`, display equation on plot.

## Project — A Python CLI for unit conversions (length, temperature, pressure, force/torque) and sensor data analysis.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
python main.py          # interactive unit converter CLI
python process.py       # CSV data processing
python analysis/plot_sensor.py  # sensor data visualisation
```

## Tests

```bash
pytest tests/ -v
```

## Project Structure

- `converters/` — unit conversion modules (length, temperature, pressure, force_torque)
- `utils/` — shared helper functions
- `analysis/` — data analysis and plotting scripts
- `tests/` — pytest test suite
- `process.py` — CSV processing pipeline
- `data/` — data files (gitignored, not committed)
