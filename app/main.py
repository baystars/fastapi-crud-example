# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import FastAPI
from starlette.requests import Request

from app.service.database import db
from app.user.endpoints import router as user_router

app = FastAPI()

# 起動時にDatabaseに接続する。
@app.on_event("startup")
async def startup():
    await db.connect()

# 終了時にDatabaseを切断する。
@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

# users routerを登録する。
app.include_router(user_router, prefix='/user')

# middleware state.connectionにdatabaseオブジェクトをセットする。
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = db
    response = await call_next(request)
    return response

if __name__ == "__main__":
    main()
