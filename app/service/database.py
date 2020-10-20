# -*- mode: python -*- -*- coding: utf-8 -*-
import databases
import sqlalchemy

from app.config import (DATABASE_URI, ECHO_LOG)

# databases
db = databases.Database(DATABASE_URI)
engine = sqlalchemy.create_engine(DATABASE_URI, echo=ECHO_LOG)
metadata = sqlalchemy.MetaData()
