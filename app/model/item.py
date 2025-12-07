import dataclasses
import json
from typing import Optional, Union

@dataclasses.dataclass
class Item:
    id: int
    datetime_string: str # yyyymmddhhmmss
    user_id: int
    n_good: int 
    n_bad: int
    title: str
    tags: list[str] 
    link_url: str 
    thumbnail_url: str 
    description: Optional[str]
    embedded_url : Optional[str]

    def toDict(self) -> str:
        return dataclasses.asdict(self)