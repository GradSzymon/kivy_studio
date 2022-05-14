from abc import ABCMeta

class BasePipeline(meta=ABCMeta):

    def add(self, element) -> None:
        raise NotImplementedError
