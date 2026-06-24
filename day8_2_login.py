from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

""" userid='user' ->  틀리면 로그인 실패
password='1234' ->  틀리면 비밀번호가 다릅니다
둘 다 맞으면 로그인 성공 """

class login(BaseModel):
    userid: str 
    password: str

USERID = 'user'
PASSWORD = '1234'

@app.post('/login/')
async def login(login:login):
    if login.userid != 'USERID':
        return {'message': '사용자 아이디가 다릅니다'}
    if login.password != 'PASSWORD':
        return {'message': '비밀번호가 다릅니다'}
    return {'message': '로그인 성공'}