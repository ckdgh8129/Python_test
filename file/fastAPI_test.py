#pip install fastapi uvicorn

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
                    CORSMiddleware,
                    allow_origins=["*"],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
)
@app.get("/data")
def home():
    return {
        "name" : "김유신","age" : 34
    }
#python -m uvicorn fastAPI_test:app(파일명) --reload
