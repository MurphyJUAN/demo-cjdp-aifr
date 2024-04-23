# %%
import pickle
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from aiohttp import ClientSession
import asyncio
import os
import random
import requests
import pandas as pd
import tempfile
import shutil
import uvicorn

# %%
# For CORS Protocal
app = FastAPI()

# 设置静态文件夹和模板文件夹
app.mount("/static", StaticFiles(directory="dist/static"), name="static")
templates = Jinja2Templates(directory="dist")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名跨域，生产环境中应更严格
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法（如 POST, GET, DELETE 等）
    allow_headers=["*"],  # 允许所有头信息
)
count = 0
# %%
df = pd.read_csv('./selected_samples.csv').fillna("")
# %%
'''
Interface...
'''
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # 使用模板
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/random")
async def random_number():
    print('>>>Hi!')
    response = {
        'randomNumber': random.randint(1, 100)
    }
    return response

@app.api_route('/api/intermediate-vote-monitor', methods=['POST', 'GET'])
async def forward_get_vote(request: Request):
    payload = dict(request.query_params)
    print('>>>payload:', payload)
    external_url = 'http://140.114.80.46:5556/api/vote-monitor'
    
    async with ClientSession() as session:
        async with session.get(external_url, params=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise HTTPException(status_code=response.status, detail="Failed to retrieve data")

@app.api_route('/api/intermediate-vote-download', methods=['POST', 'GET'])
async def forward_download(request: Request):
    payload = dict(request.query_params)
    external_url = 'http://140.114.80.46:5556/api/vote-download'
    
    async with ClientSession() as session:
        async with session.get(external_url, params=payload) as external_response:
            if external_response.status == 200:
                content = await external_response.read()
                headers = {
                    "Content-Disposition": "attachment; filename=downloaded_file.csv",
                    "Content-Type": "text/csv; charset=utf-8"
                }
                print(f"接收到的文件大小为 {len(content)} 字节")
                return Response(content=content, headers=headers, media_type="text/csv")
            else:
                # 如果外部请求失败，返回错误信息
                return Response("Failed to download file from external URL", status_code=external_response.status)



@app.post('/api/intermediate-predict')
@app.get('/api/intermediate-predict')
async def forward_predict(request: Request):
    payload = await request.json()
    external_url = 'http://140.114.80.46:5556/api/predict'
    
    async with ClientSession() as session:
        async with session.post(external_url, json=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise HTTPException(status_code=response.status, detail="Failed to make prediction")

@app.get('/api/get-testcase')
async def get_testcase():
    random_row = df.sample(n=1)
    response = {
        'ID': random_row['ID'].values[0],
        "result": random_row['Result'].values[0],
        "data": {
          "AA": [{ "Sentence": random_row['AA_Rationale'].values[0], "Feature": random_row['AA_Factor'].values[0].split(",") }],
          "AD": [{ "Sentence": random_row['AD_Rationale'].values[0], "Feature": random_row['AD_Factor'].values[0].split(",") }],
          "RA": [{ "Sentence": random_row['RA_Rationale'].values[0], "Feature": random_row['RA_Factor'].values[0].split(",") }],
          "RD": [{ "Sentence": random_row['RD_Rationale'].values[0], "Feature": random_row['RD_Factor'].values[0].split(",") }],
        },
    }
    return response

# %%

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("inter_backend_fastapi:app", host="0.0.0.0", port=port, reload=True)
