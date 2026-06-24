from fastapi import FastAPI
import random
import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "키움 디지털 아카데미 4기에 오신 것을 환영합니다!",
        "학습_단계": [
            "1단계: 기본 GET 요청",
            "2단계: 경로 매개변수",
            "3단계: 쿼리 매개변수",
            "4단계: POST 요청과 모델",
            "5단계: 실전 프로젝트",
        ],
        "tip": "/docs 에서 API 문서를 확인해보세요!",
    }



@app.get("/hello/{name}")
def read_hello(name: str):
    greetings = ["안녕하세요", "반갑습니다", "환영합니다", "좋은 하루예요"]

    return {
        "message": f"{random.choice(greetings)}, {name}님!",
        "today": datetime.date.today().strftime("%Y-%m-%d"),
        "lucky_number": random.randint(1, 100),
    }

from pydantic import BaseModel

class Item(BaseModel):
    subject : str
    score : int

@app.post('/score/')
def read_score(item:list[Item]):
    return item