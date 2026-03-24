---
description: "Run the test suite, report pass/fail and coverage details, and suggest next actions."
name: "report-coverage"
argument-hint: "Path to tests or command to execute"
agent: "agent"
---
Run tests for the current workspace and produce a short status report:
- Run `python -m unittest` and capture output
- If available, run a coverage command (e.g., `coverage run -m pytest && coverage report`)
- Report number of tests run, passed, failures, errors, and total coverage %
- Highlight any failing tests and suggest one next step (e.g. add test, fix assertion, refactor)
- If the test command is missing or fails, explain how to fix it

Example invocation:
- `/report-coverage` (no args) for default suite
- `/report-coverage tests/test_gilded_rose.py` to run a targeted test file
