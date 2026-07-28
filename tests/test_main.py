"""Tests for the main module."""

from src.main import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from test05\n"
