from vehicle_builder.repositories import GroupsRepository


class LibraryService:
    async def get_library(self, conn):
        groups_repository = GroupsRepository(conn)
        groups_with_features = await groups_repository.get_groups_with_features()
