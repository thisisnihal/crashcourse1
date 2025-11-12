# Python Assignments

This folder contains a set of small Python example projects and utilities used for learning and quick experiments. Each subfolder is a self-contained example with a short description and a simple way to run it.

Quick start
 - Recommended: create and activate a virtual environment, then install dependencies from `requirements.txt` (if needed).

PowerShell (Windows)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Projects

- `1.logreport/`
  - Description: Log-reporting example that includes a small runner (`main.py`) and utilities for generating or profiling log data.
  - Key files: `main.py`, `json_logreport_mem_profiler.py`, `memory_profiler_report.txt`, `data/` (sample log files).
  - Run: `python .\1.logreport\main.py` (reads data from the `data/` subfolder).

- `2.api_design/`
  - Description: API design examples and small snippets demonstrating request/response handling and design decisions.
  - Key files: `main1.py`, `main2.py`, `tmp.py`.
  - Run: `python .\2.api_design\main1.py` or `python .\2.api_design\main2.py`.

- `3.remove_duplicate_emails/`
  - Description: Small utility to remove duplicate emails from a CSV file.
  - Key files: `main.py`, `input.csv` (example input).
  - Run: `python .\3.remove_duplicate_emails\main.py` (reads `input.csv` in the same folder and prints or writes cleaned output depending on the script behaviour).

- `4.redact_users_info/`
  - Description: Script to redact or anonymize user information in a CSV file.
  - Key files: `main.py`, `input.csv` (example input).
  - Run: `python .\4.redact_users_info\main.py` (reads `input.csv` and outputs redacted data per the script logic).

- `5.social_network/`
  - Description: Small social-network example that reads JSON input and produces JSON output.
  - Key files: `main.py`, `input.json`, `output.json` (sample output file included).
  - Run: `python .\5.social_network\main.py` (reads `input.json` and writes `output.json`).

Utilities

- `.logreportenv/` - a local virtual environment included in the folder (if present). Prefer creating your own `.venv` instead of using this directory.
- `utils/json_generator.py` - helper used to generate JSON/log samples.

Notes
- The projects are small learning examples and may print results to stdout or write to files in their respective folders. Check the top of each `main.py` for specific behaviour and any CLI options.
- If a script requires additional packages, install them from the top-level `requirements.txt` inside this folder.
- No formal test suite is included. If you'd like, I can add minimal unit tests or example inputs/outputs for any project.

