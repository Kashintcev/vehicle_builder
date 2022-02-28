import abc
from typing import List

import databases
import sqlalchemy

from models.database import database


class BaseRepository(abc.ABC):
    def __init__(self, db: databases.Database = database, *args, **kwargs) -> None:
        self._db = db
        super()

    @property
    @abc.abstractmethod
    def _table(self) -> sqlalchemy.Table:
        pass

    @property
    @abc.abstractmethod
    def _schema(self):
        pass

    async def find_all(self) -> List:
        query = self._table.select()
        rows = await self._db.fetch_all(query=query)
        return [self._schema(**dict(row.items())) for row in rows]

    async def find_by_id(self, el_id: int) -> _schema:
        query = self._table.select().where(self._table.c.id == el_id)
        row = await self._db.fetch_one(query)
        if row:
            return self._schema(**dict(row.items()))
        return None
