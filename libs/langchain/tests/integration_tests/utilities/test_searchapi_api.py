"""Integration tests for SearchApi"""
from langchain.utilities.searchapi_search import SearchAPIWrapper


def test_call() -> None:
    """Test that call gives the correct answer."""
    search = SearchAPIWrapper()
    output = search.run("What is the capital of Lithuania?")
    assert "Vilnius" in output
