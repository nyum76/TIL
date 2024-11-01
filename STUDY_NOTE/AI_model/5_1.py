from fastapi import FastAPI

# app : 간단하게 FastAPI의 인스턴스 생성 가능. FastAPI 핵심요소로 웹어플리케이션 정리와 실행 담당 (예 : 엔드포인트 정리 등)
app = FastAPI()

@app.get("/hi") # FastAPI 인스턴스를 통해 get 메서드 정리 ( url로 메서드 호출 시 read_root 실행되어 함수가 반환하는게 결과값이 됨 )
def read_root(): 
    return {"message":"minmin<3"} 

@app.get("/hi2") # FastAPI 인스턴스를 통해 get 메서드 정리 ( url로 메서드 호출 시 read_root 실행되어 함수가 반환하는게 결과값이 됨 )
def read_root(): 
    return {"message":"hihihi"} 
# 이후에 명령어 uvicorn 5_1:app --reload 를 터미널에 입력하기