from typing import Any
from datetime import datetime
from json import JSONEncoder


class DatetimeJsonEncoder(JSONEncoder):
    def default(self, obj: object) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
