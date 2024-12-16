from typing import AsyncIterator, Dict, Any
from elasticsearch.helpers import async_bulk

from src.database.services.school import school_service
from src.search.client import ESClient


class ESLoader(ESClient):
    @staticmethod
    async def generate_documents() -> AsyncIterator[Dict[str, Any]]:
        schools = await school_service.get_schools()
        for school in schools:
            document: Dict[str, Any] = {
                "_index": "schools",
                "doc": {
                    "id": school.id,
                    "name": school.name,
                    "city": school.city
                }
            }
            yield document

    async def load_documents(self) -> None:
        await async_bulk(self._es_client, self.generate_documents())
