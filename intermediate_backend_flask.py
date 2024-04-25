# %%
import pickle
from flask import Flask, request, render_template, jsonify, make_response, send_file, Response
import os
from flask_cors import CORS, cross_origin
import random
import requests
import pandas as pd
import tempfile
import shutil

# %%
# For CORS Protocal
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
CORS(app)
count = 0
# %%
df = pd.read_csv('./selected_samples.csv').fillna("")
# %%
'''
Interface...
'''
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/api/random')
def random_number():
    print('>>>Hi!')
    response = {
        'randomNumber': random.randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/intermediate-vote-monitor', methods=['POST', 'GET'])
def forward_get_bote():
    payload = request.args.to_dict()
    print('>>>payload:', payload)
    external_url = 'http://140.114.80.46:5556/api/vote-monitor'
    response = requests.get(external_url, params=payload)
    return jsonify(response.json())

@app.route('/api/intermediate-vote-download', methods=['POST', 'GET'])
def forward_download():
    payload = request.args.to_dict()
    external_url = 'http://140.114.80.46:5556/api/vote-download'
    external_response = requests.get(external_url, params=payload, stream=True)
    # 确保请求成功
    if external_response.status_code == 200:
        file_size_bytes = len(external_response.content)
        print(f"接收到的文件大小为 {file_size_bytes} 字节", external_response.status_code, external_response.headers)

        return Response(external_response.content, headers={
            "Content-Disposition": "attachment; filename=downloaded_file.csv",
            "Content-Type": "text/csv; charset=utf-8"
        })

        # # 创建临时文件以保存下载的CSV文件
        # with tempfile.NamedTemporaryFile(mode='w+b', delete=False, dir='./') as temp_file:
        #     # 将外部响应的内容写入临时文件
        #     shutil.copyfileobj(external_response.raw, temp_file)
        #     temp_file.flush()  # 确保数据写入磁盘
        #     os.fsync(temp_file.fileno())  # 确保数据从操作系统缓冲区写入
        #     # 注意保留文件名，以便后续使用
        #     temp_file_name = temp_file.name
        #     print("临时文件已创建，路径和文件名为:", temp_file_name)
        
        # # 使用Flask的send_file发送文件
        # # 注意：需要设置as_attachment=True以便于触发浏览器的下载行为
        # return send_file(temp_file_name, as_attachment=True, download_name="downloaded_file.csv", mimetype='text/csv')
    else:
        # 如果外部请求失败，返回错误信息
        return Response("Failed to download file from external URL", status=external_response.status_code)

    return response

@app.route('/api/intermediate-predict', methods=['POST', 'GET'])
def forward_predict():
    payload = request.get_json()
    external_url = 'http://140.114.80.46:5556/api/predict'
    response = requests.post(external_url, json=payload)
    return jsonify(response.json())

@app.route('/api/get-testcase', methods=['GET'])
def get_testcase():
    global count
    # selected_ids = ['08_28_637000',
    #     '16_05_1b4347',
    #     '15_11_bffc8d',
    #     '05_22_12ed20',
    #     '11_14_eeea6c',
    #     '26_20_a96471',
    #     '16_03_63d925',
    #     '13_42_8a77cf',
    #     '47_28_1e5167',
    #     '24_18_6003f3',
    #     '18_43_b4f74b',
    #     '28_30_ec0cce',
    #     '31_02_054e98',
    #     '29_28_11be7b',
    #     '06_06_c8e0f8',
    #     '31_24_7d9349']
    # selected_id = selected_ids[count]
    # selected_id = "10_31_885202"
    # count += 1
    random_row = df.sample(n=1)
    # random_row = df[df['ID']==selected_id]
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
    return jsonify(response)

# %%

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 8080))
    #    app.run(host='0.0.0.0', port=port, debug=True, ssl_context=('cert.pem', 'key.pem'))
        app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
