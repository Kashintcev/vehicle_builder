import aiopg.sa

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from vehicle_builder.settings import get_config
from vehicle_builder.db import pg_context
from vehicle_builder.models import function_table
#
#
# def setup_db(db_url: str) -> None:
#     print("Creating database")
#     if not database_exists(db_url):
#         create_database(db_url)
#     else:
#         print("Database already exists")
#
#
# def teardown_db(db_url: str) -> None:
#     drop_database(db_url)
#
#
# def sample_data(conn) -> None:
#     query = function_table.insert().values(
#         name="test function",
#     )
#     await conn.execute(query)


if __name__ == '__main__':
    config = get_config()["database"]
    db_url = f"postgresql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
    create_engine(db_url)
    # setup_db(db_url)
    #
    # engine = await aiopg.sa.create_engine(
    #     database=config['database'],
    #     user=config['user'],
    #     password=config['password'],
    #     host=config['host'],
    #     port=config['port'],
    # )
    # sample_data(engine)
