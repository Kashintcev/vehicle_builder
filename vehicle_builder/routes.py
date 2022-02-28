from vehicle_builder.views import index, groups, library


def setup_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/groups", groups, name="groups")
    app.router.add_get("/library", library, name="library")
