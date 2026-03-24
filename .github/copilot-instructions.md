---
description: "GitHub Copilot workspace instructions for Python Gilded Rose Refactoring Kata (testing, style, and common tasks)"
---

# Gilded Rose Python workspace instructions

## Project summary

- Repository: `GildedRose-Refactoring-Kata`
- Focus: Python reference implementation of the Gilded Rose Kata with unit tests and approval tests.
- Main files:
  - `gilded_rose.py` + `texttest_fixture.py`
  - `tests/test_gilded_rose.py`
  - `tests/test_gilded_rose_approvals.py`
  - `README.md` (Python folder) and top-level `README.md`

## Getting started

- Activate Python virtual environment (already configured in workspace):
  - `source .venv/bin/activate`
- Install dependencies:
  - `pip install -r requirements.txt`

## Run tests

- All unit tests:
  - `python -m unittest`
- Approval test script:
  - `python tests/test_gilded_rose_approvals.py`
- TextTest fixture (legacy kata approval style):
  - `python texttest_fixture.py 10`

## Code style and conventions

- Python 3.11+ compatible (use the virtualenv interpreter in `.venv`).
- Keep code minimal and behavior-preserving: kata is about safe refactoring.
- Maintain existing public behavior in `update_quality()` semantics according to `GildedRoseRequirements.md`.
- Architecture uses the **Strategy Pattern**: each item type has a dedicated strategy class extending `UpdateStrategy`. New item types should follow this pattern by adding a class and registering it in `StrategyFactory._strategies`.

## Typical tasks for this workspace

- Add descriptive unit tests for edge cases (sell-in boundaries, quality caps, special item types).
- Refactor `gilded_rose.py` into smaller classes/functions without changing test outcomes.
- Keep approval tests passing when behavior effects are intentional and explicit.

## Agent instructions

- Prefer non-invasive refactoring suggestions (small steps with tests first).
- When a behavior request refers to special item names (`Aged Brie`, `Sulfuras, Hand of Ragnaros`, `Backstage passes`), use the kata requirements to validate.
- Confirm each code change by running `python -m unittest`.
- When tests are missing for requested behavior, add focused tests first.

## Notes for custom helpers

- This workspace has no `.github/AGENTS.md` currently; use this file as the canonical workspace-level instruction.
- If you need per-file semantics, create `.github/instructions/*.instructions.md` with `applyTo:` globs.
