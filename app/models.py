# -*- mode: python -*- -*- coding: utf-8 -*-

import sqlalchemy
from app.service.database import (metadata, engine)

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String, index=True),
    sqlalchemy.Column("email", sqlalchemy.String, index=True),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("create_at", sqlalchemy.DateTime),
    sqlalchemy.Column("update_at", sqlalchemy.DateTime),
    #sqlalchemy.Column("is_active", sqlalchemy.Boolean(), default=True),
    #sqlalchemy.Column("is_superuser", sqlalchemy.Boolean(), default=False)
)

metadata.create_all(bind=engine)
