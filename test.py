# %%
import torch
import torch.nn.functional as F
import numpy as np
from model.MyJointBert import MyJointBert
from transformers import BertTokenizer
# %%
PRETRAINED_MODEL_NAME = "bert-base-chinese" 
NUM_LABELS = 3
MAX_LENGTH = 512
EMB_MODEL_NAME = ""
device = "cuda"
tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
bert_best_model_path = './ckpt/bert_balance.pt'
bert_best_model = MyJointBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS, emb_name=EMB_MODEL_NAME)
bert_best_model.load_state_dict(torch.load(bert_best_model_path, map_location='cpu'))
bert_best_model.to(device)
# %%
AA = {'Sentence': '', 'Feature': '該方具有親子感情等有利的判決因子'}
AD = {'Sentence': '', 'Feature': '該方具有意願能力等不利的判決因子'}
RA = {'Sentence': '', 'Feature': '該方具有親子感情等有利的判決因子'}
RD = {'Sentence': '', 'Feature': '該方具有意願能力等不利的判決因子'}
# %%
AA['Feature'] = ""
AD['Feature'] = ""
RA['Feature'] = ""
RD['Feature'] = ""
# %%
AA_tok = tokenizer(AA['Feature'], AA['Sentence'],  max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
AD_tok = tokenizer(AD['Feature'], AD['Sentence'],  max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
RA_tok = tokenizer(RA['Feature'], RA['Sentence'],  max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
RD_tok = tokenizer(RD['Feature'], RD['Sentence'],  max_length=MAX_LENGTH, truncation="longest_first", return_tensors='pt')
# %%
AA = {key: val.to(device) for key, val in AA_tok.items()}
AD = {key: val.to(device) for key, val in AD_tok.items()}
RA = {key: val.to(device) for key, val in RA_tok.items()}
RD = {key: val.to(device) for key, val in RD_tok.items()}

outputs = bert_best_model(AA, AD, RA, RD)
logits = outputs['logits']
prob = F.softmax(logits.data, dim = 1).squeeze().cpu().numpy().tolist()
print(prob)
# %%
