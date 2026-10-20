from fastapi import FastAPI
from app.models.user import User
from app.database import Base, engine
from app.api.auth import router as auth_router
from app.api.user import router as user
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.common.exceptions import (
    BusinessException,
    bussiness_excpetion_hadler,
    http_excpetion_hadler,
    validation_excpetion_hadler,
    global_excpetion_hadler,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 注册异常处理器
app.add_exception_handler(BusinessException, bussiness_excpetion_hadler)
app.add_exception_handler(HTTPException, http_excpetion_hadler)
app.add_exception_handler(RequestValidationError, validation_excpetion_hadler)
# 全局的异常兜底，必须放在最后注册！！
app.add_exception_handler(Exception, global_excpetion_hadler)


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


app.include_router(auth_router)
app.include_router(user)
