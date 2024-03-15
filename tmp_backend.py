# %%
import pickle
from flask import Flask, request, render_template, jsonify, make_response, send_file
import os
from flask_cors import CORS, cross_origin
import random
import requests
import pandas as pd

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
        app.run(host='0.0.0.0', port=port, debug=True)
