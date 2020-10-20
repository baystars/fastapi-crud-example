# -*- mode: python -*- -*- coding: utf-8 -*-
import hashlib

from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request

from .models import User
from .schemas import (UserCreate, UserUpdate, UserSelect)

from databases import Database

from app.utils.dbutils import get_connection

router = APIRouter()

# 入力したパスワード（平文）をハッシュ化して返します。
def get_user_insert_dict(user):
    pwhash = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
    values = user.dict()
    values.pop('password')
    values['hashed_password'] = pwhash
    return values

# userを全件検索して「UserSelect」のリストをjsonにして返します。
@router.get('/', response_model=List[UserSelect])
async def user_findall(request: Request, database: Database = Depends(get_connection)):
    query = User.select()
    return await database.fetch_all(query)

# userをidで検索して「UserSelect」をjsonにして返します。
@router.get('/find', response_model=UserSelect)
async def user_findone(id: int, database: Database = Depends(get_connection)):
    query = User.select().where(User.columns.id==id)
    return await database.fetch_one(query)

# userを新規登録します。
@router.post('/create', response_model=UserSelect)
async def user_create(user: UserCreate, database: Database = Depends(get_connection)):
    # validatorは省略
    query = User.insert()
    values = get_user_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}

# userを更新します。
@router.patch('/update', response_model=UserSelect)
async def user_update(user: UserUpdate, database: Database = Depends(get_connection)):
    # validatorは省略
    query = User.update().where(User.columns.id==user.id)
    values=get_user_insert_dict(user)
    ret = await database.execute(query, values)
    return {**user.dict()}

# userを削除します。
@router.delete('/delete')
async def user_delete(user: UserUpdate, database: Database = Depends(get_connection)):
    query = User.delete().where(User.columns.id==user.id)
    ret = await database.execute(query)
    return {'result': 'delete success'}
