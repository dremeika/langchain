"""Integration tests for SearchApi"""
from langchain.utilities.searchapi import SearchApiAPIWrapper


def test_call() -> None:
    """Test that call gives the correct answer."""
    search = SearchApiAPIWrapper()
    output = search.run("What is the capital of Lithuania?")
    assert "Vilnius" in output
