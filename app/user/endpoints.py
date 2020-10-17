# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def read_user():
    return {'msg': 'hello'}
