import requests

requests.post('http://localhost:3000/send_private_msg', json={
    'user_id': 123456,
    'message': [{
        'type': 'text',
        'data': {
            'text': 'Hello, World!'
        }
    }]
})

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/")
async def root(request: Request):
    data = await request.json()  # 获取事件数据
    print(data)
    return {}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)