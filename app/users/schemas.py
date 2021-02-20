# -*- mode: python -*- -*- coding: utf-8 -*-
import datetime
from typing import Optional

from pydantic import (BaseModel)


class User(BaseModel):
    """User Model"""
    name: str
    email: str


class UserSelect(User):
    """User Select Model"""


class UserCreate(User):
    """User Create Model"""
    password: Optional[str]
    create_at: Optional[datetime.date]
    update_at: Optional[datetime.date]


class UserUpdate(UserCreate):
    """User Update Model"""
    id: int
