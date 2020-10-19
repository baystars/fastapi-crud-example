# -*- mode: python -*- -*- coding: utf-8 -*-
import sqlalchemy
from app.database import (metadata, engine)

User = sqlalchemy.Table(
    'user',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("username", sqlalchemy.String, index=True),
    sqlalchemy.Column("email", sqlalchemy.String, index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean(), default=True),
    sqlalchemy.Column("is_superuser", sqlalchemy.Boolean(), default=False)
)

metadata.create_all(bind=engine)
