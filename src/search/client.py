from accessify import protected
from typing import AsyncIterator, Dict, Any, List

from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk

from src.config import settings


class ESClient:
    def __init__(self) -> None:
        self._es_client: AsyncElasticsearch = AsyncElasticsearch(
            hosts=settings.es.url,
            basic_auth=(settings.es.user, settings.es.password)
        )

    @protected
    async def create_index(
            self,
            index: str,
            mappings: Dict[str, Any]
    ) -> bool | None:
        try:
            if not await self._es_client.indices.exists(index):
                response = await self._es_client.indices.create(
                    index=index,
                    body=mappings,
                )
                return True if response is not None else False
        except Exception as _ex:
            raise _ex

    @protected
    async def add_documents(
            self,
            documents: AsyncIterator[Dict[str, Any]]
    ) -> None:
        await async_bulk(self._es_client, documents)

    @protected
    async def search_documents(
            self,
            index: str,
            body: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        response = await self._es_client.search(
            index=index,
            body=body
        )
        return [
            item['_source']
            for item in response['hits']['hits']
        ]
