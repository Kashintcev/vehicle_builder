from typing import List
from vehicle_builder.repositories import GroupsRepository
from vehicle_builder.schemas import Group


class GroupsService:
    async def get_groups(self, connection, include: List[str] = None) -> List[Group]:
        groups_repository = GroupsRepository(connection)
        groups = await groups_repository.get_groups(include)
        return groups
