# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import (HTTPException, status)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def get_value_401(data, error='Unauthorized'):
    return get_value(data, status_code=401, error=error)

def get_value(data, status_code=500, error='Internal Server Error'):
    try:
        return data.__next__()
    except StopIteration as e:
        raise HTTPException(status_code=status_code, detail=error)

def error_message(status, message, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder({'status': status,'message': message})
    )
