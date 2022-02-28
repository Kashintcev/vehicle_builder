from typing import List
from vehicle_builder.models import group_table
from vehicle_builder.schemas import Group


class GroupsRepository:
    def __init__(self, connection):
        self.connection = connection

    async def get_groups(self, include: List[str] = None) -> List[Group]:
        query = group_table.select()

        result = await self.connection.execute(query)
        rows = await result.fetchall()
        return [
            Group(**dict(row))
            for row in rows
        ]

    async def get_groups_with_features(self):
        query = group_table.select().join(C, C.id == D.c_id)


        result = await self.connection.execute(query)
        rows = await result.fetchall()
