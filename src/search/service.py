from typing import Dict, Any, List

from src.search.client import ESClient


class ESService(ESClient):
    def __init__(self, index: str) -> None:
        super().__init__()
        self.index = index

    async def create(self) -> None:
        mappings: Dict[str, Any] = {
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "city": {"type": "keyword"}
                }
            }
        }
        await self.create_index(
            index=self.index,
            mappings=mappings
        )

    async def search(self, query: str) -> List[Dict[str, Any]]:
        body: Dict[str, Any] = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "name": {
                                    "query": query,
                                    "fuzziness": "AUTO",
                                    "prefix_length": 1
                                }
                            }
                        },
                        {
                            "match": {
                                "city": {
                                    "query": query,
                                    "fuzziness": "AUTO",
                                    "prefix_length": 1
                                }
                            }
                        }
                    ]
                }
            }
        }
        return await self.search_documents(
            index=self.index,
            body=body
        )
