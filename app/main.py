from fastapi import FastAPI
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

from app.service.database import database
from app.users.endpoints import router as userrouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)


@app.on_event("startup")
async def startup():
    """# 起動時にDatabaseに接続する。"""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """# 終了時にDatabaseを切断する。"""
    await database.disconnect()

# users routerを登録する。
app.include_router(userrouter)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    """# middleware state.connectionにdatabaseオブジェクトをセットする。"""
    request.state.connection = database
    response = await call_next(request)
    return response
