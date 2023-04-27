# %%
from flask import Flask, request, render_template, jsonify, make_response, send_file
import os
from flask_cors import CORS
from random import *
# %%
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# %%
import math
import torch
import torch.nn.functional as F
import numpy as np
from model.MyJointBert import MyJointBert
from transformers import BertTokenizer
import gdown

os.makedirs('./ckpt', exist_ok=True)
best_model_path = './ckpt/best.pt'
deploy_model_path = './ckpt/aug.pt'
model_path = './ckpt/aug_last.pt'
# if os.path.isfile(best_model_path):
#   print(">>>>>檔案存在。")
# else:
#     url = 'https://drive.google.com/uc?export=download&id=1wk_Fvcky0M4pQOs7RiEwei_dIZCHjXxh'
#     gdown.download(url, best_model_path, quiet=False)

PRETRAINED_MODEL_NAME = "bert-base-chinese" 
NUM_LABELS = 3
MAX_LENGTH = 512
EMB_MODEL_NAME = ""
tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
# Ensemble
best_model = MyJointBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS, emb_name=EMB_MODEL_NAME)
best_model.load_state_dict(torch.load(best_model_path, map_location='cpu'))
deploy_model = MyJointBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS, emb_name=EMB_MODEL_NAME)
deploy_model.load_state_dict(torch.load(deploy_model_path, map_location='cpu'))
# Choose one
# model = MyJointBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS, emb_name=EMB_MODEL_NAME)
# model.load_state_dict(torch.load(model_path, map_location='cpu'))


def get_predict(data, model):
    AA = tokenizer(data['AA']['Feature'], data['AA']['Sentence'], \
        padding="max_length", max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
    AD = tokenizer(data['AD']['Feature'], data['AD']['Sentence'], \
        padding="max_length", max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
    RA = tokenizer(data['RA']['Feature'], data['RA']['Sentence'], \
        padding="max_length", max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
    RD = tokenizer(data['RD']['Feature'], data['RD']['Sentence'], \
        padding="max_length", max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')

    # Ensemble
    # best_outputs = best_model(AA, AD, RA, RD)
    # best_logits = best_outputs['logits']
    # best_prob = F.softmax(best_logits.data, dim = 1).squeeze().numpy()

    # deploy_outputs = deploy_model(AA, AD, RA, RD)
    # deploy_logits = deploy_outputs['logits']
    # deploy_prob = F.softmax(deploy_logits.data, dim = 1).squeeze().numpy()
    # prob = (best_prob + deploy_prob) / 2

    # Choose one
    outputs = model(AA, AD, RA, RD)
    logits = outputs['logits']
    prob = F.softmax(logits.data, dim = 1).squeeze().numpy().tolist()

    return prob

    
    
    
# %%
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/test')
def test():
    test_data = {
        'AA': { 'Sentence': '測試', 'Feature': ['測試'] },
        'AD': { 'Sentence': '測試', 'Feature': ['測試'] },
        'RA': { 'Sentence': '測試', 'Feature': ['測試'] },
        'RD': { 'Sentence': '測試', 'Feature': ['測試'] },
    }

    data = test_data
    for key in data:
        data[key]['Feature'] = f'該方具有{" ".join(test_data[key]["Feature"])}'
    prob = get_predict((data))


    return prob

@app.route('/api/predict', methods=['POST', 'GET'])
def predict():
    full_data = request.get_json()
    print('>>>>>data:', full_data)
    mode = full_data['model']
    data = full_data['data']
    test_data = data
    for key in data:
        if len(data[key]['Feature']) > 0:
            str = "該方具有"
            for idx, feature in enumerate(data[key]['Feature']):
                if idx < len(data[key]['Feature']) - 1:
                    str += feature + '，'
                else:
                    str += feature

            if 'AA' in key or 'RA' in key:
                str += "等有利的判決因子"
            else:
                str += "等不利的判決因子"
        else:
            str = ""
        data[key]['Feature'] = str
    print('>>>>>data:', data)
    print('>>>>>mode', mode)

    prob_deploy = get_predict(data, deploy_model)
    prob_best = get_predict(data, best_model)
    if mode == "mode1":
        result = {
            'L1': { 'Applicant': prob_best[0]*100, \
                    'Respondent': prob_best[1]*100, \
                    'Both': prob_best[2]*100 
                    },
            'L2': {
                 'Applicant': prob_deploy[0]*100, \
                'Respondent': prob_deploy[1]*100, \
                'Both': prob_deploy[2]*100 
                }
        }
    elif mode == "mode2":
        result = {
            'S1': { 'Applicant': prob_best[0]*100, \
                    'Respondent': prob_best[1]*100, \
                    'Both': prob_best[2]*100 
                    },
            'S2': {
                'Applicant': prob_deploy[0]*100, \
                'Respondent': prob_deploy[1]*100, \
                'Both': prob_deploy[2]*100 
                }
        }
        
    elif mode == "mode3":
        result = {
        'C1': { 'Applicant': prob_deploy[0]*100, \
                    'Respondent': prob_deploy[1]*100, \
                    'Both': prob_deploy[2]*100 
                },
        'C2': {
            'Applicant': prob_deploy[0]*100, \
            'Respondent': prob_deploy[1]*100, \
            'Both': prob_deploy[2]*100 
            }
        }
    else:
        print(f'>>>>Error: Not exist mode: {mode}')
        
    return jsonify(result)


# %%

if __name__ == "__main__":
       port = int(os.environ.get("PORT", 8000))
       app.run(host='0.0.0.0', port=port, debug=True)