from typing import Any, Coroutine
from langchain.tools.base import BaseTool


class SearchAPIRun(BaseTool):

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        return super()._run(*args, **kwargs)

    def _arun(self, *args: Any, **kwargs: Any) -> Coroutine[Any, Any, Any]:
        return super()._arun(*args, **kwargs)


class SearchAPIResults(BaseTool):

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        return super()._run(*args, **kwargs)

    def _arun(self, *args: Any, **kwargs: Any) -> Coroutine[Any, Any, Any]:
        return super()._arun(*args, **kwargs)
