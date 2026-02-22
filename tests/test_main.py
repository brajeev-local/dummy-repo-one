"""Sample tests."""

import pytest

from src.my_python_app.main import main


def test_main_runs_without_error() -> None:
    """main() runs without raising."""
    main()
