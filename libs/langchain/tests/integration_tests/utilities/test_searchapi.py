"""Integration tests for SearchApi"""
import pytest

from langchain.utilities.searchapi import SearchApiAPIWrapper


def test_call() -> None:
    """Test that call gives correct answer."""
    search = SearchApiAPIWrapper()
    output = search.run("What is the capital of Lithuania?")
    assert "Vilnius" in output


def test_results() -> None:
    """Test that call gives correct answer."""
    search = SearchApiAPIWrapper()
    output = search.results("What is the capital of Lithuania?")
    assert "Vilnius" in output["knowledge_graph"]["description"]
    assert "Vilnius" in output["organic_results"][0]["snippet"]


def test_scholar_call() -> None:
    """Test that call gives correct answer for scholar search."""
    search = SearchApiAPIWrapper(engine="google_scholar")
    output = search.run("large language models")
    assert "state of large language models and their applications" in output


def test_jobs_call() -> None:
    """Test that call gives correct answer for jobs search."""
    search = SearchApiAPIWrapper(engine="google_jobs")
    output = search.run("AI")
    assert "years of experience" in output


@pytest.mark.asyncio
async def test_async_call() -> None:
    """Test that call gives the correct answer."""
    search = SearchApiAPIWrapper()
    output = await search.arun("What is Obama's full name?")
    assert "Barack Hussein Obama II" in output


@pytest.mark.asyncio
async def test_async_results() -> None:
    """Test that call gives the correct answer."""
    search = SearchApiAPIWrapper(searchapi_api_key="demo")
    output = await search.aresults("What is Obama's full name?")
    assert "Barack Hussein Obama II" in output["knowledge_graph"]["description"]
