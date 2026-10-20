from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.common.response import Response


class BusinessException(Exception):
    """自定义的业务异常"""

    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code
        super().__init__(message)


async def bussiness_excpetion_hadler(request: Request, exc: Exception):
    """自定义业务异常处理器"""
    if not isinstance(exc, BusinessException):
        raise TypeError("Expected BusinessException")
    return JSONResponse(
        status_code=200,
        content=Response.error(code=exc.code, message=exc.message).model_dump(),
    )


async def http_excpetion_hadler(request: Request, exc: Exception):
    """Http异常处理器"""
    if not isinstance(exc, HTTPException):
        raise TypeError("Expected HTTPException")
    return JSONResponse(
        status_code=exc.status_code,
        content=Response.error(code=exc.status_code, message=exc.detail).model_dump(),
    )


async def validation_excpetion_hadler(request: Request, exc: Exception):
    """参数异常处理器"""
    if not isinstance(exc, RequestValidationError):
        raise TypeError("Expected RequestValidationError")
    return JSONResponse(
        status_code=422,
        content=Response.error(code=422, message="请求参数校验错误").model_dump(),
    )


async def global_excpetion_hadler(request: Request, exc: Exception):
    """全局异常处理器"""
    return JSONResponse(
        status_code=500,
        content=Response.error(code=500, message="服务器内部错误").model_dump(),
    )
