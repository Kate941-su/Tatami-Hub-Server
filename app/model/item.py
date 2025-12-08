import dataclasses
import json
from typing import Optional, Union
from datetime import datetime

@dataclasses.dataclass
class ItemModel:
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
    
    @staticmethod
    def fromJson(json_data: dict[str, any]) -> Optional['ItemModel']:
        return ItemModel(
            # Required fields are passed directly
            id=json_data['id'],
            datetime_string=json_data['datetime_string'],
            user_id=json_data['user_id'],
            n_good=json_data['n_good'],
            n_bad=json_data['n_bad'],
            title=json_data['title'],
            tags=json_data['tags'],
            link_url=json_data['link_url'],
            thumbnail_url=json_data['thumbnail_url'],
            
            # Optional fields need a .get() check with a default of None
            description=json_data.get('description'), 
            embedded_url=json_data.get('embedded_url')
        )
            