# -*- mode: python -*- -*- coding: utf-8 -*-
import datetime
from typing import Optional

from pydantic import (BaseModel)


class UserBase(BaseModel):
    """User Model"""
    name: str
    email: str
    password: Optional[str]


class UserSelect(UserBase):
    """User Select Model"""
    id: int


class UserCreate(UserBase):
    """User Create Model"""
    password: Optional[str]
    create_at: Optional[datetime.date]
    update_at: Optional[datetime.date]


class UserUpdate(UserCreate):
    """User Update Model"""
    id: int
