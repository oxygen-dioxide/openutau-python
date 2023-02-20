import yaml

from .UProject import UProject

from typing import List, Union

def loads(data:str) -> UProject:
    return UProject.from_dict(yaml.safe_load(data))

def dumps(project:UProject) -> str:
    return yaml.safe_dump(project.to_dict())