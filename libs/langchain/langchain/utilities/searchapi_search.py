from langchain.pydantic_v1 import BaseModel


class SearchAPIWrapper(BaseModel):

    def run(self, *args, **kwargs):
        raise NotImplementedError

    def arun(self, *args, **kwargs):
        raise NotImplementedError

    def results(self, *args, **kwargs):
        raise NotImplementedError

    def aresults(self, *args, **kwargs):
        raise NotImplementedError
