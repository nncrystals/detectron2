from typing import List, Union

from rx import subject
import logging

from ui.models.metadata import MetaDataCollection
from ui.models.project import Project


class RuntimeStates:
    project: Union[Project, None]

    def __init__(self):
        self.metadata = MetaDataCollection()
        self.project = None

    def get_state_dict(self):
        def recursive_to_dict(d: dict):
            d = d.copy()

            for k, v in d.items():
                if hasattr(v, "__dict__"):
                    d[k] = recursive_to_dict(v.__dict__)
                    d[k]["#class"] = v.__class__.__name__
                if isinstance(v, dict):
                    d[k] = recursive_to_dict(v)
                if isinstance(v, list):
                    d[k] = [recursive_to_dict(x) for x in v]

            return d

        return recursive_to_dict(self.__dict__)




