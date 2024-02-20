# %%
import pickle
from flask import Flask, request, render_template, jsonify, make_response, send_file
import os
from flask_cors import CORS, cross_origin
import random
from model.MyJointBert import MyJointRoberta
import copy
import pandas as pd
import math
import torch
import torch.nn.functional as F
import numpy as np
from model.MyJointBert import MyJointBert,  MyJointRoberta
from model.MyDNN import SplitedDNN
from transformers import BertTokenizer, AutoTokenizer
import gdown
import xgboost as xgb
from opencc import OpenCC
cc = OpenCC('t2s')
from gensim.models.doc2vec import Doc2Vec
from gensim.test.test_doc2vec import ConcatenatedDoc2Vec
import re
import data_preprocess
from data_preprocess import clean_to_seg
# %%
# For CORS Protocal
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# %%
# Define General Model Parameter
PRETRAINED_MODEL_NAME = "bert-base-chinese" 
NUM_LABELS = 3
EMB_MODEL_NAME = ""
device = "cpu"
batch_size = 4
MAX_LENGTH = 512
tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
confidence_weight = 5
features = ['親子感情', '意願能力', '父母經濟', '支持系統', '父母生活', '主要照顧',\
       '子女年齡', '人格發展', '父母健康', '父母職業', '子女意願', '友善父母', '父母品行']
# %%
# Parameter For Pertubation
copy_ratio = 20
with open('./neu_string.txt', 'r', encoding='utf-8') as file:
    neu_string = file.read()
# %%
'''
Loading Model......
'''
def load_bert_model(model_path, PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME):
    model = MyJointBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS, emb_name=EMB_MODEL_NAME)
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    return model
def load_roberta_model(model_path, PRETRAINED_MODEL_NAME, NUM_LABELS):
    model = MyJointRoberta(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS)
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    return model
def load_dnn_model(model_path, input_size=200, bottleneck_size=100, output_size=3):
    model = SplitedDNN(input_size=input_size, bottleneck_size=bottleneck_size, output_size=output_size)
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    return model
# For Demo Paper
# Our(only switch)
our_switch_model = None
our_switch_5_model_1 = None
our_switch_5_model_2 = None
our_switch_5_model_3 = None
our_switch_10_model = None
our_switch_15_model = None

def load_demo_models():
    global our_switch_model 
    global our_switch_5_model_1 
    global our_switch_5_model_2 
    global our_switch_5_model_3 
    global our_switch_10_model 
    global our_switch_15_model 
    our_switch_model_path = './ckpt/new/our_switch_0.pt'
    our_switch_model = load_bert_model(our_switch_model_path, PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
    our_switch_model.to(device)
    # Our(swotch + 5% both augment 1)
    our_switch_5_model_1 = load_bert_model('./ckpt/new/our_switch_5_1.pt', PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
    our_switch_5_model_1.to(device)
    # Our(swotch + 5% both augment 2)
    our_switch_5_model_2 = load_bert_model('./ckpt/new/our_switch_5_2.pt', PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
    our_switch_5_model_2.to(device)
    # Our(swotch + 5% both augment 3)
    our_switch_5_model_3 = load_bert_model('./ckpt/new/our_switch_5_3.pt', PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
    our_switch_5_model_3.to(device)
    # Our(swotch + 10% both augment)
    our_switch_10_model = load_bert_model('./ckpt/new/our_switch_10.pt', PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
    our_switch_10_model.to(device)
    # Our(swotch + 15% both augment)
    our_switch_15_model = load_bert_model('./ckpt/new/our_switch_15.pt', PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
    our_switch_15_model.to(device)


# # Our(swotch + 30% both augment)
# our_switch_30_model = load_bert_model('./ckpt/new_moaug/our_switch_30.pt', PRETRAINED_MODEL_NAME, NUM_LABELS, EMB_MODEL_NAME)
# our_switch_30_model.to(device)

# For AIFR Demo
# For XGBoos
def load_xgboost_models(model_paths):
    model_list = []
    for p in model_paths:
        xgboost_model = xgb.XGBClassifier(objective='multi:softmax', num_class=NUM_LABELS, use_label_encoder=False)
        with open(p, "rb") as f:
            xgboost_model = pickle.load(f)
        model_list.append(
            xgboost_model
        )
    return model_list
xgboost_model_paths = ['./ckpt/xgboost_3class_0.pkl', './ckpt/xgboost_3class_1.pkl', './ckpt/xgboost_3class_2.pkl', './ckpt/xgboost_3class_3.pkl', './ckpt/xgboost_3class_4.pkl', './ckpt/xgboost_3class_5.pkl', './ckpt/xgboost_3class_6.pkl', './ckpt/xgboost_3class_7.pkl', './ckpt/xgboost_3class_8.pkl', './ckpt/xgboost_3class_9.pkl', './ckpt/xgboost_3class_10.pkl']
xgboost_model_list = []

# For DNN
# 讀入中性句的平均向量
# 讀入 DNN 的六個模型
# Switch + 0%
dnn_switch_0_model = None
dnn_switch_5_model = None
dnn_switch_10_model = None
dnn_switch_15_model = None
dnn_switch_20_model = None
dnn_switch_30_model = None

def load_dnn_models():
    global dnn_switch_0_model
    global dnn_switch_5_model
    global dnn_switch_10_model
    global dnn_switch_15_model
    global dnn_switch_20_model
    global dnn_switch_30_model
    dnn_switch_0_path = './ckpt/new_moaug/dnn_switch_0.pt'
    dnn_switch_0_model = load_dnn_model(dnn_switch_0_path)
    dnn_switch_0_model.to(device)
    # Switch + 5%
    dnn_switch_5_path = './ckpt/new_moaug/dnn_switch_5_1.pt'
    dnn_switch_5_model = load_dnn_model(dnn_switch_5_path)
    dnn_switch_5_model.to(device)
    # Switch + 10%
    dnn_switch_10_path = './ckpt/new_moaug/dnn_switch_10.pt'
    dnn_switch_10_model = load_dnn_model(dnn_switch_10_path)
    dnn_switch_10_model.to(device)
    # Switch + 15%
    dnn_switch_15_path = './ckpt/new_moaug/dnn_switch_15.pt'
    dnn_switch_15_model = load_dnn_model(dnn_switch_15_path)
    dnn_switch_15_model.to(device)
    # Switch + 20
    dnn_switch_20_path = './ckpt/new_moaug/dnn_switch_20.pt'
    dnn_switch_20_model = load_dnn_model(dnn_switch_20_path)
    dnn_switch_20_model.to(device)
    # Switch + 30
    dnn_switch_30_path = './ckpt/new_moaug/dnn_switch_30.pt'
    dnn_switch_30_model = load_dnn_model(dnn_switch_30_path)
    dnn_switch_30_model.to(device)
# For Lawformer (switch + 0% both augment)
lawformer_switch_0_model = None
lawformer_switch_5_model = None
lawformer_switch_10_model = None
lawformer_switch_15_model = None

def load_lawformer_models():
    global lawformer_switch_0_model 
    global lawformer_switch_5_model 
    global lawformer_switch_10_model 
    global lawformer_switch_15_model 
    lawformer_switch_0_model = load_roberta_model('./ckpt/new/lawformer_switch_0.pt', "thunlp/Lawformer", NUM_LABELS)
    lawformer_switch_0_model.to(device)
    # For Lawformer (switch + 05% both augment)
    lawformer_switch_5_model = load_roberta_model('./ckpt/new/lawformer_switch_5.pt', "thunlp/Lawformer", NUM_LABELS)
    lawformer_switch_5_model.to(device)
    # For Lawformer (switch + 10% both augment)
    lawformer_switch_10_model = load_roberta_model('./ckpt/new/lawformer_switch_10.pt', "thunlp/Lawformer", NUM_LABELS)
    lawformer_switch_10_model.to(device)
    # For Lawformer (switch + 15% both augment)
    lawformer_switch_15_model = load_roberta_model('./ckpt/new/lawformer_switch_15.pt', "thunlp/Lawformer", NUM_LABELS)
    lawformer_switch_15_model.to(device)
# %%
# For Doc2Vec
model_dbow = None
model_dmm = None
concate_model = None
def load_doc2vec_models():
    global model_dbow
    global model_dmm
    global concate_model
    model_dbow = Doc2Vec.load('./ckpt/dbow_100_ADV_DIS_model.bin')
    model_dmm = Doc2Vec.load('./ckpt/dmm_100_ADV_DIS_model.bin')
    model_dbow.random.seed(3407)
    model_dmm.random.seed(3407)
    concate_model = ConcatenatedDoc2Vec([model_dbow, model_dmm])
# %%
def initialize_model():
    """在处理第一个请求之前加载模型"""
    global xgboost_model_list
    load_demo_models()
    xgboost_model_list = load_xgboost_models(xgboost_model_paths)
    load_dnn_models()
    load_lawformer_models()
    load_doc2vec_models()
# %%
initialize_model()


# %%
def seg_to_DocVec(input_txt, model):
    avgDoc2Vec = []
    for _ in range(1):
        avgDoc2Vec.append(np.array(model.infer_vector(input_txt)))
    avgDoc2Vec = np.mean(avgDoc2Vec, axis=0)
    return avgDoc2Vec
test_neutral_vector_pool = np.load('./ckpt/test_neutral_avg_vector_pool.npy')
# %%
def collect_features(row, sentiment):
    old_list = [0.0] * len(features)
    for idx, feature in enumerate(features):
        if feature in row:
            if sentiment == "有利":
                old_list[idx] = 1.0
            elif sentiment == "不利":
                old_list[idx] = -1.0
            else:
                print("error")
                break
    # ans = f"{target}具有{','.join(txt)}{sentiment}的因素。"
    return old_list
def remove_random_chars(sentence, num_chars_to_remove):
    chars = list(sentence)
    if len(chars) <= num_chars_to_remove:
        return sentence
    # 隨機選擇要刪除的字元的索引
    indices_to_remove = random.sample(range(len(chars)), num_chars_to_remove)
    # 在新的列表上刪除選定的字元
    for index in sorted(indices_to_remove, reverse=True):
        del chars[index]
    # 將剩餘的字元重新組成一個句子
    return ''.join(chars)
def sample_characters(text, num_chars):
    # 檢查字元數是否超過文本長度
    random.seed(None)
    if num_chars > len(text):
        raise ValueError("num_chars is larger than the text length.")
    # 將文本轉換為一個字元列表
    characters = list(text)
    # 從字元列表中隨機選擇 num_chars 個字元
    selected_characters = random.sample(characters, num_chars)
    # 將選擇的字元組合成一個字符串
    return ''.join(selected_characters)
def get_perturbation_data(data, convert=True):
    aa = data['AA']['Sentence']
    ad = data['AD']['Sentence']
    ra = data['RA']['Sentence']
    rd = data['RD']['Sentence']

    s_aa = []
    s_ad = []
    s_ra = []
    s_rd = []

    f_aa = []
    f_ad = []
    f_ra = []
    f_rd = []

    for i in range(copy_ratio):
        if i < copy_ratio / 2:
            new_aa = remove_random_chars(aa, max(5, round(len(aa)*0.05)))
            new_ad = remove_random_chars(ad, max(5, round(len(ad)*0.05)))
            new_ra = remove_random_chars(ra, max(5, round(len(ra)*0.05)))
            new_rd = remove_random_chars(rd, max(5, round(len(rd)*0.05)))
        elif i >= copy_ratio / 2 and i < copy_ratio * 3 / 4:
            new_aa = aa + sample_characters(neu_string, max(5, round(len(aa)*0.05)))
            new_ad = ad + sample_characters(neu_string, max(5, round(len(ad)*0.05)))
            new_ra = ra + sample_characters(neu_string, max(5, round(len(ra)*0.05)))
            new_rd = rd + sample_characters(neu_string, max(5, round(len(rd)*0.05)))
        else:
            new_aa = sample_characters(neu_string, max(5, round(len(aa)*0.05))) + aa
            new_ad = sample_characters(neu_string, max(5, round(len(ad)*0.05))) + ad
            new_ra = sample_characters(neu_string, max(5, round(len(ra)*0.05))) + ra
            new_rd = sample_characters(neu_string, max(5, round(len(rd)*0.05))) + rd
        
        s_aa.append(cc.convert("[AA] " + new_aa) if convert else "[AA] " + new_aa)
        f_aa.append(cc.convert("[AA] " + data['AA']['Feature'])if convert else "[AA] " + data['AA']['Feature'])

        s_ad.append(cc.convert("[AD] " + new_ad) if convert else "[AD] " + new_ad)
        f_ad.append(cc.convert("[AD] " + data['AD']['Feature']) if convert else "[AD] " + data['AD']['Feature'])

        s_ra.append(cc.convert("[RA] " + new_ra) if convert else "[RA] " + new_ra)
        f_ra.append(cc.convert("[RA] " + data['RA']['Feature']) if convert else "[RA] " + data['RA']['Feature'])

        s_rd.append(cc.convert("[RD] " + new_rd) if convert else "[RD] " + new_rd)
        f_rd.append(cc.convert("[RD] " + data['RD']['Feature']) if convert else "[RD] " + data['RD']['Feature'])
    return s_aa, f_aa, s_ad, f_ad, s_ra, f_ra, s_rd, f_rd
def get_perturbation_result(data, model, device):
    model.eval()
    model.to(device)
    s_aa, f_aa, s_ad, f_ad, s_ra, f_ra, s_rd, f_rd = get_perturbation_data(data)
    
    all_probs = []
    for i in range(0, copy_ratio, batch_size):
        AA = tokenizer(f_aa[i:i+batch_size], s_aa[i:i+batch_size], \
            padding=True, max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
        AD = tokenizer(f_ad[i:i+batch_size], s_ad[i:i+batch_size], \
            padding=True, max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
        RA = tokenizer(f_ra[i:i+batch_size], s_ra[i:i+batch_size], \
            padding=True, max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
        RD = tokenizer(f_rd[i:i+batch_size], s_rd[i:i+batch_size], \
            padding=True, max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
        AA = {key: val.to(device) for key, val in AA.items()}
        AD = {key: val.to(device) for key, val in AD.items()}
        RA = {key: val.to(device) for key, val in RA.items()}
        RD = {key: val.to(device) for key, val in RD.items()}

        with torch.no_grad():
            outputs = model(AA, AD, RA, RD)
        logits = outputs['logits']
        prob_ = F.softmax(logits.data, dim = 1).squeeze().cpu().numpy().tolist()
        all_probs += prob_
    return all_probs
def get_demo_predict(data, model_list, device):
    print('>>>>> Start Predict...')
    all_probs = []
    for model in model_list:
        all_probs += get_perturbation_result(data, model, device)

    result = {
        "detail_info": [],
        "avg_prob": {"plaintiff": 0, "both": 0, "defendant": 0},
        "std": {"plaintiff": 0, "both": 0, "defendant": 0},
        "confidence":{"plaintiff": 0, "both": 0, "defendant": 0},
        "granted": "",
    }
    # Extract the first, second, and third elements from each sublist
    for x in all_probs:
        result['detail_info'].append({'label': '聲請方(Plaintiff)', 'probability': round(x[0]*100, 2)})
        result['detail_info'].append({'label': '雙方(Both)', 'probability': round(x[2]*100, 2)})
        result['detail_info'].append({'label': '相對方(Defendant)', 'probability': round(x[1]*100, 2)})
    
    avg_prob = np.mean(np.array(all_probs), axis=0).tolist()
    result["avg_prob"] = {"plaintiff": np.round(avg_prob[0]*100, 2), "both": np.round(avg_prob[2]*100, 2), "defendant": np.round(avg_prob[1]*100, 2)}
    std = np.std(np.array(all_probs), ddof=1, axis=0).tolist()
    result["std"] = {"plaintiff": np.round(std[0]*100, 2), "both": np.round(std[2]*100, 2), "defendant": np.round(std[1]*100, 2)}
    result["confidence"] = {"plaintiff": np.round((np.exp(-confidence_weight * std[0]))*100, 2), "both": np.round((np.exp(-confidence_weight * std[2]))*100, 2), "defendant": np.round((np.exp(-confidence_weight * std[1]))*100, 2)}
    max_idx = np.argmax(avg_prob)
    name = ["plaintiff", "defendant", "both"]
    result['granted'] = name[max_idx]
    print('>>>>> Predict Result:', result['avg_prob'])
    return result

def get_splits_sentences(data):
    data_list = [{
        "AA": [],
        "AD": [],
        "RA": [],
        "RD": []
    }]
    data_list[0]['AA'] = [s.strip() for s in re.split(r'[。！？]', data['AA']['Sentence']) if s.strip()]
    data_list[0]['AD'] = [s.strip() for s in re.split(r'[。！？]', data['AD']['Sentence']) if s.strip()]
    data_list[0]['RA'] = [s.strip() for s in re.split(r'[。！？]', data['RA']['Sentence']) if s.strip()]
    data_list[0]['RD'] = [s.strip() for s in re.split(r'[。！？]', data['RD']['Sentence']) if s.strip()]
    return data_list

def get_doc2vec_augment_vector(data_list):
    new_data_list = []
    for _ in range(copy_ratio):
        for item in data_list:
            new_item = {
                "AA": [],
                "AD": [],
                "RA": [],
                "RD": []
            }
            for key in item:
                if len(item[key]) > 0:
                    new_item[key] = np.mean([seg_to_DocVec(clean_to_seg(s,textmode = True), model=concate_model) for s in item[key]], axis = 0)
                else:
                    neu_index = np.random.choice(len(test_neutral_vector_pool))
                    new_item[key] = test_neutral_vector_pool[neu_index]
            new_data_list.append(new_item)
    return new_data_list

def get_dnn_augment_result(vector_data_list, model, device):
    model.eval()
    model.to(device)
    all_probs = []
    for i in range(0, copy_ratio, batch_size):
        AA = torch.tensor(np.array([i['AA'] for i in vector_data_list[i:i+batch_size]])).to(device)
        AD = torch.tensor(np.array([i['AD'] for i in vector_data_list[i:i+batch_size]])).to(device)
        RA = torch.tensor(np.array([i['RA'] for i in vector_data_list[i:i+batch_size]])).to(device)
        RD = torch.tensor(np.array([i['RD'] for i in vector_data_list[i:i+batch_size]])).to(device)

        with torch.no_grad():
            outputs = model(AA, AD, RA, RD)
        logits = outputs['logits']
        prob_ = F.softmax(logits.data, dim = 1).squeeze().cpu().numpy().tolist()
        all_probs += prob_
    return all_probs

def get_predict(data, model_list, type, device):
    print('>>>>> Start Predict ...')
    if type == "bert-based":
        all_probs = []
        for model in model_list:
            all_probs += get_perturbation_result(data, model, device)
        prob = np.mean(np.array(all_probs), axis=0).tolist()
        std = np.std(np.array(all_probs), ddof=1, axis=0).tolist()
        min_values = np.min(all_probs, axis=0).tolist()
        q1_values = np.percentile(all_probs, 25, axis=0).tolist()
        q2_values = np.percentile(all_probs, 50, axis=0).tolist()  # This is the median
        q3_values = np.percentile(all_probs, 75, axis=0).tolist()
        max_values = np.max(all_probs, axis=0).tolist()
    elif type == "dnn":
        # 斷句 get_split_sentences
        data_list = get_splits_sentences(data)
        # 轉成 doc2vec，並擴增 100 個 sample get_doc2vec_augment_vector()，且補上中向平均向量
        vector_data_list = get_doc2vec_augment_vector(data_list)
        # 輸入模型得到 prob get_dnn_augment_result
        all_probs = []
        for model in model_list:
            all_probs += get_dnn_augment_result(vector_data_list, model, device)
        # 計算 acg_prob, acg_std
        prob = np.mean(np.array(all_probs), axis=0).tolist()
        std = np.std(np.array(all_probs), ddof=1, axis=0).tolist()
        min_values = np.min(all_probs, axis=0).tolist()
        q1_values = np.percentile(all_probs, 25, axis=0).tolist()
        q2_values = np.percentile(all_probs, 50, axis=0).tolist()  # This is the median
        q3_values = np.percentile(all_probs, 75, axis=0).tolist()
        max_values = np.max(all_probs, axis=0).tolist()
    elif type == "xgboost-based":
        AA = collect_features(data['AA']['Feature'], '有利')
        AD = collect_features(data['AD']['Feature'], '不利')
        RA = collect_features(data['RA']['Feature'], '有利')
        RD = collect_features(data['RD']['Feature'], '不利')
        A = [a + b for a, b in zip(AA, AD)]
        R = [a + b for a, b in zip(RA, RD)]
        subtract = [a - b for a, b in zip(A, R)]
        divide = [a / 2 for a in subtract]

        all_probs = []
        for model in model_list:
            probs = model.predict_proba([divide])[0]
            all_probs.append(probs)
        prob = np.mean(np.array(all_probs), axis=0).tolist()
        std = np.std(np.array(all_probs), ddof=1, axis=0).tolist()
        min_values = np.min(all_probs, axis=0).tolist()
        q1_values = np.percentile(all_probs, 25, axis=0).tolist()
        q2_values = np.percentile(all_probs, 50, axis=0).tolist()  # This is the median
        q3_values = np.percentile(all_probs, 75, axis=0).tolist()
        max_values = np.max(all_probs, axis=0).tolist()
    print('>>>>> Predict Result:', prob)
    return prob, [np.round(s*100, decimals=2)  for s in std], ([np.round(v*100, decimals=2) for v in min_values], [np.round(v*100, decimals=2) for v in q1_values], [np.round(v*100, decimals=2) for v in q2_values], [np.round(v*100, decimals=2) for v in q3_values], [np.round(v*100, decimals=2) for v in max_values]), np.array(all_probs)
    
# %%
'''
Interface...
'''
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': random.randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/demo-predict', methods=['POST', 'GET'])
def demo_predict():
    full_data = request.get_json()
    print('>>>>> Input Query Data:', full_data)
    data = full_data
    for key in data:
        if len(data[key]['Feature']) > 0:
            str = "當事人具有"
            for idx, feature in enumerate(data[key]['Feature']):
                if idx < len(data[key]['Feature']) - 1:
                    str += feature['value'] + '，'
                else:
                    str += feature['value']

            if 'AA' in key or 'RA' in key:
                str += "等有利的判決因子"
            else:
                str += "等不利的判決因子"
        else:
            str = ""
        data[key]['Feature'] = str
    print('>>>>> Input Model data:', data)
    if torch.cuda.is_available():
        device = torch.device('cuda')
    demo_model_list = [our_switch_model, our_switch_5_model_1, our_switch_5_model_2, our_switch_5_model_3, our_switch_10_model, our_switch_15_model]
    result = get_demo_predict(data, demo_model_list, device)
    for m in demo_model_list:
        m.cpu()
    del demo_model_list
    torch.cuda.empty_cache()
    return jsonify(result)

@app.route('/api/predict', methods=['POST', 'GET'])
def predict():
    device = "cpu"
    full_data = request.get_json()
    print('>>>>> Input Query Data:', full_data)
    mode = full_data['model']
    data = full_data['data']
    for key in data:
        if len(data[key]['Feature']) > 0:
            str = "當事人具有"
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

    print('>>>>>Iuput model data:', data)
    print('>>>>>Testing mode(模式一/模式二/模式三)', mode)

    if torch.cuda.is_available():
        device = torch.device('cuda')

    our_model_list = [our_switch_model, our_switch_5_model_1, our_switch_5_model_2, our_switch_5_model_3, our_switch_10_model, our_switch_15_model]
    prob_our_bert, std_our_bert, (min_our_bert, q1_our_bert, q2_our_bert, q3_our_bert, max_our_bert), all_our_bert_probs = get_predict(data=data, model_list=our_model_list, type="bert-based", device=device)
    # TODO
    # prob_our_bert = [0, 0, 0]
    # std_our_bert = [0, 0, 0]
    
    if mode == "mode1":
        print('>>>mode1')
        if data['AA'] == data['RA'] and data['AD'] == data['RD']:
            # TODO
            result = {
            'L1': { 'Applicant': {'avg_prob': 0*100, 'std': 0, 'min': 0, "q1": 0, "q2": 0, "q3": 0, "max": 0, "all_probs": [0]*len(xgboost_model_list)}, \
                    'Respondent': {'avg_prob':0*100, 'std': 0, 'min': 0, "q1": 0, "q2": 0, "q3": 0, "max": 0, "all_probs": [0]*len(xgboost_model_list)}, \
                    'Both': {'avg_prob': 1*100, 'std': 0, 'min': 100, "q1": 100, "q2": 100, "q3": 100, "max": 100, "all_probs": [1]*len(xgboost_model_list)}
                    },
            'L2': {
                 'Applicant': {'avg_prob': 0*100, 'std': 0, 'min': 0, "q1": 0, "q2": 0, "q3": 0, "max": 0, "all_probs": [0]*len(all_our_bert_probs)}, \
                'Respondent': {'avg_prob': 0*100, 'std': 0, 'min': 0, "q1": 0, "q2": 0, "q3": 0, "max": 0, "all_probs": [0]*len(all_our_bert_probs)}, \
                'Both': {'avg_prob': 1*100, 'std': 0, 'min': 100, "q1": 100, "q2": 100, "q3": 100, "max": 100, "all_probs": [1]*len(all_our_bert_probs)}
                }
        }
        else:
            prob_xgboost, std_xgboost, (min_xgboost, q1_xgboost, q2_xgboost, q3_xgboost, max_xgboost), all_xgboost_probs = get_predict(data=data, model_list=xgboost_model_list, type='xgboost-based', device=device)
            result = {
                'L1': { 'Applicant': {'avg_prob': prob_xgboost[0]*100, 'std': std_xgboost[0], 'min': min_xgboost[0], "q1": q1_xgboost[0], "q2": q2_xgboost[0], "q3": q3_xgboost[0], "max": max_xgboost[0], "all_probs": all_xgboost_probs[:, 0].tolist()}, \
                        'Respondent': {'avg_prob': prob_xgboost[1]*100, 'std': std_xgboost[1], 'min': min_xgboost[1], "q1": q1_xgboost[1], "q2": q2_xgboost[1], "q3": q3_xgboost[1], "max": max_xgboost[1], "all_probs": all_xgboost_probs[:, 1].tolist()}, \
                        'Both': {'avg_prob': prob_xgboost[2]*100, 'std': std_xgboost[2], 'min': min_xgboost[2], "q1": q1_xgboost[2], "q2": q2_xgboost[2], "q3": q3_xgboost[2], "max": max_xgboost[2], "all_probs": all_xgboost_probs[:, 2].tolist()}
                        },
                'L2': {
                    'Applicant': {'avg_prob': prob_our_bert[0]*100, 'std': std_our_bert[0], 'min': min_our_bert[0], "q1": q1_our_bert[0], "q2": q2_our_bert[0], "q3": q3_our_bert[0], "max": max_our_bert[0], "all_probs": all_our_bert_probs[:, 0].tolist()},  \
                    'Respondent': {'avg_prob': prob_our_bert[1]*100, 'std': std_our_bert[1], 'min': min_our_bert[1], "q1": q1_our_bert[1], "q2": q2_our_bert[1], "q3": q3_our_bert[1], "max": max_our_bert[1], "all_probs": all_our_bert_probs[:, 1].tolist()}, \
                    'Both': {'avg_prob': prob_our_bert[2]*100, 'std': std_our_bert[2], 'min': min_our_bert[2], "q1": q1_our_bert[2], "q2": q2_our_bert[2], "q3": q3_our_bert[2], "max": max_our_bert[2], "all_probs": all_our_bert_probs[:, 2].tolist()}
                    }
            }
    elif mode == "mode2":
        print('>>>data', data)
        dnn_model_list = [dnn_switch_0_model, dnn_switch_5_model, dnn_switch_10_model, dnn_switch_15_model, dnn_switch_20_model, dnn_switch_30_model]
        prob_dnn, std_dnn, (min_dnn, q1_dnn, q2_dnn, q3_dnn, max_dnn), all_dnn_probs = get_predict(data=data, model_list=dnn_model_list, type="dnn", device=device)
        result = {
            'S1': { 'Applicant': {'avg_prob': prob_dnn[0]*100, 'std': std_dnn[0], 'min': min_dnn[0], "q1": q1_dnn[0], "q2": q2_dnn[0], "q3": q3_dnn[0], "max": max_dnn[0], "all_probs": all_dnn_probs[:, 0].tolist()}, \
                    'Respondent': {'avg_prob': prob_dnn[1]*100, 'std': std_dnn[1], 'min': min_dnn[1], "q1": q1_dnn[1], "q2": q2_dnn[1], "q3": q3_dnn[1], "max": max_dnn[1], "all_probs": all_dnn_probs[:, 1].tolist()}, \
                    'Both': {'avg_prob': prob_dnn[2]*100, 'std': std_dnn[2], 'min': min_dnn[2], "q1": q1_dnn[2], "q2": q2_dnn[2], "q3": q3_dnn[2], "max": max_dnn[2], "all_probs": all_dnn_probs[:, 2].tolist()}
                    },
            'S2': {
                    'Applicant': {'avg_prob': prob_our_bert[0]*100, 'std': std_our_bert[0], 'min': min_our_bert[0], "q1": q1_our_bert[0], "q2": q2_our_bert[0], "q3": q3_our_bert[0], "max": max_our_bert[0], "all_probs": all_our_bert_probs[:, 0].tolist()},  \
                    'Respondent': {'avg_prob': prob_our_bert[1]*100, 'std': std_our_bert[1], 'min': min_our_bert[1], "q1": q1_our_bert[1], "q2": q2_our_bert[1], "q3": q3_our_bert[1], "max": max_our_bert[1], "all_probs": all_our_bert_probs[:, 1].tolist()}, \
                    'Both': {'avg_prob': prob_our_bert[2]*100, 'std': std_our_bert[2], 'min': min_our_bert[2], "q1": q1_our_bert[2], "q2": q2_our_bert[2], "q3": q3_our_bert[2], "max": max_our_bert[2], "all_probs": all_our_bert_probs[:, 2].tolist()}
                    }
        }
        # for m in dnn_model_list:
        #     m.cpu()
        # del dnn_model_list
        # torch.cuda.empty_cache()
        
    elif mode == "mode3":
        lawformer_model_list = [lawformer_switch_0_model, lawformer_switch_5_model, lawformer_switch_10_model, lawformer_switch_15_model]
        prob_lawformer, std_lawformer, (min_lawformer, q1_lawformer, q2_lawformer, q3_lawformer, max_lawformer), all_lawformer_probs = get_predict(data=data, model_list=lawformer_model_list, type="bert-based", device=device)

        result = {
        'C1': {
            'Applicant': {'avg_prob': prob_lawformer[0]*100, 'std': std_lawformer[0], 'min': min_lawformer[0], "q1": q1_lawformer[0], "q2": q2_lawformer[0], "q3": q3_lawformer[0], "max": max_lawformer[0], "all_probs": all_lawformer_probs[:, 0].tolist()}, \
            'Respondent': {'avg_prob': prob_lawformer[1]*100, 'std': std_lawformer[1], 'min': min_lawformer[1], "q1": q1_lawformer[1], "q2": q2_lawformer[1], "q3": q3_lawformer[1], "max": max_lawformer[1], "all_probs": all_lawformer_probs[:, 1].tolist()}, \
            'Both': {'avg_prob': prob_lawformer[2]*100, 'std': std_lawformer[2], 'min': min_lawformer[2], "q1": q1_lawformer[2], "q2": q2_lawformer[2], "q3": q3_lawformer[2], "max": max_lawformer[2], "all_probs": all_lawformer_probs[:, 2].tolist()}
        },
        'C2': {
                    'Applicant': {'avg_prob': prob_our_bert[0]*100, 'std': std_our_bert[0], 'min': min_our_bert[0], "q1": q1_our_bert[0], "q2": q2_our_bert[0], "q3": q3_our_bert[0], "max": max_our_bert[0], "all_probs": all_our_bert_probs[:, 0].tolist()},  \
                    'Respondent': {'avg_prob': prob_our_bert[1]*100, 'std': std_our_bert[1], 'min': min_our_bert[1], "q1": q1_our_bert[1], "q2": q2_our_bert[1], "q3": q3_our_bert[1], "max": max_our_bert[1], "all_probs": all_our_bert_probs[:, 1].tolist()}, \
                    'Both': {'avg_prob': prob_our_bert[2]*100, 'std': std_our_bert[2], 'min': min_our_bert[2], "q1": q1_our_bert[2], "q2": q2_our_bert[2], "q3": q3_our_bert[2], "max": max_our_bert[2], "all_probs": all_our_bert_probs[:, 2].tolist()}
                    }
        }
        # for m in lawformer_model_list:
        #     m.cpu()
        # del lawformer_model_list
        # torch.cuda.empty_cache()
    else:
        print(f'>>>>Error: Not exist mode: {mode}')

    # 清除 CUDA 的冗余 MEM
    # for m in our_model_list:
    #     m.cpu()
    # del our_model_list
    # torch.cuda.empty_cache()
        
    return jsonify(result)


# %%

if __name__ == "__main__":
       port = int(os.environ.get("PORT", 8000))
       app.run(host='0.0.0.0', port=port, debug=True)