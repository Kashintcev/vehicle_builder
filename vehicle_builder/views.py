from aiohttp import web
from vehicle_builder.services import GroupsService, LibraryService

groups_service = GroupsService()
library_service = LibraryService()


async def index(request):
    return web.json_response({
        "status": "success",
    })


async def groups(request):
    """
    Returns list of groups
    :param request:
    :return:
    """
    async with request.app['db'].acquire() as conn:
        groups = await groups_service.get_groups(conn)
        return web.json_response(
            [group.dict() for group in groups]
        )


async def library(request):
    """
    Returns features library
    :param request:
    :return:
    """
    async with request.app['db'].acquire() as conn:
        library = await library_service.get_library(conn)
        return web.json_response(
            [group.dict() for group in library]
        )
