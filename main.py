import logging

from aiohttp.web import Application, run_app

from vehicle_builder.routes import setup_routes
from vehicle_builder.settings import get_config
from vehicle_builder.db import pg_context


def get_app() -> Application:
    app = Application()
    app.cleanup_ctx.append(pg_context)
    app['config'] = get_config()
    setup_routes(app)
    return app


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    app = get_app()

    run_app(
        app,
        host=app["config"]["HOST"],
        port=app["config"]["PORT"],
    )


if __name__ == '__main__':
    main()
