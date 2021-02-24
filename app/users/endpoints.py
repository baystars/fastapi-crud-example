# -*- mode: python -*- -*- coding: utf-8 -*-
import hashlib
from typing import List

from databases import Database
from fastapi import (APIRouter, Depends)
from starlette.requests import Request

from .models import users
from .schemas import (UserSelect, UserCreate, UserUpdate)

from app.utils.dbutils import get_connection

router = APIRouter()


def get_users_insert_dict(user):
    """入力したパスワード（平文）をハッシュ化して返します。"""
    pwhash = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
    values = user.dict()
    # values.pop("password")
    #values["hashed_password"] = pwhash
    values["password"] = pwhash
    return values


@router.get("/users/", response_model=List[UserSelect])
async def users_findall(request: Request, database: Database = Depends(get_connection)):
    """usersを全件検索して「UserSelect」のリストをjsonにして返します。"""
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=UserSelect)
async def users_findone(user_id: int, database: Database = Depends(get_connection)):
    """usersをidで検索して「UserSelect」をjsonにして返します。"""
    query = users.select().where(users.columns.id == user_id)
    return await database.fetch_one(query)


@router.post("/users/add", response_model=UserCreate)
async def users_create(user: UserCreate, database: Database = Depends(get_connection)):
    """usersを新規登録します。"""
    # validatorは省略
    query = users.insert()
    values = get_users_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}


@router.post("/users/update", response_model=UserSelect)
async def users_update(user: UserUpdate, database: Database = Depends(get_connection)):
    """usersを更新します。"""
    # validatorは省略
    query = users.update().where(users.columns.id == user.id)
    values = get_users_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}


@router.delete("/users/{user_id}")
async def users_delete(user_id: int, database: Database = Depends(get_connection)):
    """usersを削除します。"""
    query = users.delete().where(users.columns.id == user_id)
    ret = await database.execute(query)
    return {"result": "delete success"}
