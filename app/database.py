# -*- mode: python -*- -*- coding: utf-8 -*-
import databases
import sqlalchemy

from .config import (DATABASE_URI, ECHO_LOG)

# databases
db = databases.Database(DATABASE_URI, min_size=5, max_size=20)
engine = sqlalchemy.create_engine(DATABASE_URI, echo=ECHO_LOG)
metadata = sqlalchemy.MetaData()
