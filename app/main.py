from fastapi import FastAPI
from starlette.requests import Request

from app.service.database import database
from app.users.endpoints import router as userrouter

app = FastAPI()

# 起動時にDatabaseに接続する。


@app.on_event("startup")
async def startup():
    await database.connect()

# 終了時にDatabaseを切断する。


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# users routerを登録する。
app.include_router(userrouter)

# middleware state.connectionにdatabaseオブジェクトをセットする。


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response
