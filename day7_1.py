from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message':'집가고싶다'}

@app.get('/hello/')
def read_hello():
    return {'id':'hello world!'}

@app.get('/hello1/')
def read_hello1():
    return {'result':'5+3=8'}

@app.get('/item/{item_id}')
def read_item(item_id: int) -> dict:
    return {'item_id': f'{item_id}번 입력되었습니다'}

@app.get('/userid/{user_id}/password/{password}/')
def read_login(user_id: int, password :int) -> dict:
    return {'userid': user_id, 'password': password}

@app.get('/userid/{user_id}/password/{pwd}/name{name}') 
def read_userid(user_id:str, pwd:str, name:str) -> dict:
    a = f'{user_id}, {pwd}, {name}이 입력되었습니다'
    return{'사용자ID': a}

@app.get('/login/{user}')
def read_login(user:str) -> dict:
    if user =='사용자':
        return {'로그인':'로그인 성공'}
    else: 
        return{'로그인':'로그인 실패'}

#query 매개변수 

@app.get('/query/')
def read_query(item:str, item2:str) -> dict:
    ret = f'{item}과 {item2}을(를) 찾고 있습니다'
    return {'query': ret}

from fastapi import Query
# list
@app.get('/items/')
def read_items(q: list[str] = Query([])): 
    return {'q':q}


# pydantic 모델 
from pydantic import BaseModel 


