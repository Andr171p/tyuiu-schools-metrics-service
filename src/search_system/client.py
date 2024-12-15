from accessify import protected
from typing import Dict, Any, List

from elasticsearch import AsyncElasticsearch

from src.search_system.options import url


class ESClient:
    def __init__(self) -> None:
        self._es_client = AsyncElasticsearch(url)

    @protected
    async def create_index(
            self,
            index: str,
            mappings: Dict[str, Any]
    ) -> bool | None:
        try:
            response = await self._es_client.indices.create(
                index=index,
                body={
                    "mappings": mappings
                }
            )
            return True if response is not None else False
        except Exception as _ex:
            raise _ex

    @protected
    async def add_documents(
            self,
            index: str,
            document: Dict[str, Any]
    ) -> None:
        await self._es_client.index(
            index=index,
            document=document
        )

    @protected
    async def search_documents(
            self,
            index: str,
            query: str
    ) -> List[Dict[str, Any]]:
        response = await self._es_client.search(index=index, body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["name^2", "city"]
                }
            },
            "_source": ["id", "name", "city"],
            "size": 10
        })
        return [hit["_source"] for hit in response["hits"]["hits"]]


