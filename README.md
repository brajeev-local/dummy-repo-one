# Python project template

Starter template for a Python project with `src` layout, pytest, and GitHub Actions CI. Use **Use this template** on GitHub to create a new repo from this template, then rename the package and start coding.

## Requirements

- Python 3.9 or newer
- pip (upgrade with `python -m pip install --upgrade pip` if `pip install -e .` fails)

## Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies and this package in editable mode
pip install -r requirements.txt
pip install -e .
```

If editable install fails on an older pip, run `python -m pip install --upgrade pip` and try again, or run tests with:

```bash
pip install -r requirements.txt
PYTHONPATH=src pytest -v
```

## Run

```bash
python -m src.my_python_app.main
```

## Test

```bash
pytest
# Or with verbose output:
pytest -v
```

## Project layout

| Path | Purpose |
|------|---------|
| `src/my_python_app/` | Main package (rename to your project name) |
| `src/my_python_app/__init__.py` | Package version and exports |
| `src/my_python_app/main.py` | Entry point |
| `tests/` | Pytest tests (mirror package structure if you like) |
| `pyproject.toml` | Project metadata, build, and pytest config |
| `requirements.txt` | Runtime and dev dependencies |
| `.github/workflows/test.yml` | CI: runs tests on push/PR |

## After creating a repo from this template

1. Rename `src/my_python_app` to your package name and update imports in `tests/` and any scripts.
2. Update `pyproject.toml`: `name`, `description`, `authors`.
3. Add your dependencies to `requirements.txt` (and optionally to `[project.optional-dependencies]` in `pyproject.toml`).
4. Replace this README content with your project’s docs.

## License

See [LICENSE](LICENSE).
