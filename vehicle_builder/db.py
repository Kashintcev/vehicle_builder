import aiopg.sa


async def pg_context(app):
    conf = app['config']['database']

    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )

    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()
