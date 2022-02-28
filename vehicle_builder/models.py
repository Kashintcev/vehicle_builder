from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, DateTime, Boolean, func
)

metadata = MetaData()

function_table = Table(
    "function",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String(255), nullable=False, unique=True, index=True),
    Column("created_at", DateTime, server_default=func.now()),
    Column(
        "updated_at", DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    ),
)

feature_table = Table(
    "feature",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String(255), nullable=False, unique=True, index=True),
    Column("created_at", DateTime, server_default=func.now()),
    Column(
        "updated_at", DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    ),
)

group_table = Table(
    "group",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String(255), nullable=False, unique=False, index=True),
    Column("is_set", Boolean, default=False),
    Column("parent_id", Integer, ForeignKey("group.id"), nullable=True),
)

vehicle_table = Table(
    "vehicle",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String(255), nullable=False, unique=False, index=True),
    Column("range", Integer, nullable=True, unique=False),
)

component_table = Table(
    "component",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String(255), nullable=False, unique=False, index=True),
    Column("link", String(255), nullable=True, unique=False),
    Column("article_number", Integer, nullable=True, unique=False),
    Column("weight", Integer, nullable=True, unique=False),
    Column("supplier", Integer, nullable=True, unique=False),
)

group_feature_table = Table(
    "group_feature",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("group_id", Integer, ForeignKey("group.id")),
    Column("feature_id", Integer, ForeignKey("feature.id"))
)

vehicle_feature_table = Table(
    "vehicle_feature",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("vehicle_id", Integer, ForeignKey("vehicle.id")),
    Column("feature_id", Integer, ForeignKey("feature.id"))
)

function_component_table = Table(
    "function_component",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("function_id", Integer, ForeignKey("function.id")),
    Column("component_id", Integer, ForeignKey("component.id"))
)

function_feature_table = Table(
    "function_feature",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("function_id", Integer, ForeignKey("function.id")),
    Column("feature_id", Integer, ForeignKey("feature.id"))
)
