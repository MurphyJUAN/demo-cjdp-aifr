# %%
import torch
from transformers.models.bert.modeling_bert import BertPreTrainedModel, BertModel
from transformers import AutoModel, AutoTokenizer
from transformers.models.bert.modeling_bert import BertPreTrainedModel, BertModel
import torch.nn as nn
from torch.nn import CrossEntropyLoss

from model.MyBert import MyBert

# PRETRAINED_MODEL_NAME = "bert-base-chinese"  
# MODEL_NAME = './ckpt/sentiment_analysis_DAN_textNfeature.pt'
# model = MyBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=3)
# model.load_state_dict(torch.load(MODEL_NAME))


class MyJointBert(BertPreTrainedModel):
    def __init__(self, config, emb_name):
        super(MyJointBert, self).__init__(config)
        self.num_labels = config.num_labels
        self.bert = BertModel.from_pretrained("bert-base-chinese")
        # Load embeding model
        # PRETRAINED_MODEL_NAME = "bert-base-chinese" 
        # myBert = MyBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=3)
        # self.bert = myBert.bert  # first assign the bert model
        # if len(emb_name) > 0:
        #     self.bert.load_state_dict(torch.load(emb_name))  # load weights after assignment
        #     print(f'>>>>Finish loading from {emb_name}')
        # Load embeding model
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.batchNorm = nn.BatchNorm1d(768)
        self.classifier = nn.Sequential(
            # nn.Linear(config.hidden_size * 4, config.hidden_size * 2),
            # nn.LeakyReLU(),
            # nn.Linear(config.hidden_size * 2, config.hidden_size * 1),
            # nn.LeakyReLU(),
            # nn.Linear(config.hidden_size * 1, self.num_labels)
            nn.Linear(config.hidden_size * 4, self.num_labels)
        )
        # self.apply(self.init_bert_weights)
        # self.init_weights()
    def avarage_embedding(self, hidden_states, attention_mask):
        # hidden_states 的 shape 為 (batch_size, sequence_length, hidden_size)
        # attention_mask 的 shape 為 (batch_size, sequence_length)
        mask = attention_mask.unsqueeze(-1).expand(hidden_states.size()).float()
        # 將 PAD tokens 的 mask 設為 0，其他 tokens 的 mask 設為 1
        masked_hidden_states = hidden_states * mask
        # 計算 token embeddings 的平均值
        sum_embeddings = torch.sum(masked_hidden_states, 1)
        sum_mask = torch.clamp(mask.sum(1), min=1e-9)
        avg_embeddings = sum_embeddings / sum_mask
        return avg_embeddings
    
    def forward(self, AA, AD, RA, RD, labels=None):
        AA_hidden_state, AA_pooled_output = self.bert(AA['input_ids'], token_type_ids=AA['token_type_ids'], attention_mask=AA['attention_mask'], return_dict=False)
        AD_hidden_state, AD_pooled_output = self.bert(AD['input_ids'], token_type_ids=AD['token_type_ids'], attention_mask=AD['attention_mask'], return_dict=False)
        RA_hidden_state, RA_pooled_output = self.bert(RA['input_ids'], token_type_ids=RA['token_type_ids'], attention_mask=RA['attention_mask'], return_dict=False)
        RD_hidden_state, RD_pooled_output = self.bert(RD['input_ids'], token_type_ids=RD['token_type_ids'], attention_mask=RD['attention_mask'], return_dict=False)
        
        # AA_pooled_output = self.dropout(self.batchNorm(AA_pooled_output))
        # AD_pooled_output = self.dropout(self.batchNorm(AD_pooled_output))
        # RA_pooled_output = self.dropout(self.batchNorm(RA_pooled_output))
        # RD_pooled_output = self.dropout(self.batchNorm(RD_pooled_output))
        
        AA_pooled_output = self.dropout(self.batchNorm(\
          self.avarage_embedding(AA_hidden_state, AA['attention_mask'])))
        AD_pooled_output = self.dropout(self.batchNorm( \
          self.avarage_embedding(AD_hidden_state,AD['attention_mask'])))
        RA_pooled_output = self.dropout(self.batchNorm( \
          self.avarage_embedding(RA_hidden_state, RA['attention_mask'])))
        RD_pooled_output = self.dropout(self.batchNorm( \
          self.avarage_embedding(RD_hidden_state, RD['attention_mask'])))

        pooled_output = torch.cat((AA_pooled_output, AD_pooled_output, RA_pooled_output, RD_pooled_output), 1)
        # pooled_output = (AA_pooled_output + AD_pooled_output + RA_pooled_output + RD_pooled_output) / 4
        logits = self.classifier(pooled_output)

        loss = None
        if labels is not None:
            loss_fct = CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
        return  {'logits': logits, 'loss': loss, 'sentence_emb': pooled_output}

class MyJointRoberta(torch.nn.Module):
    def __init__(self, pretrained_model_name, num_labels):
        super(MyJointRoberta, self).__init__()
        self.hidden_size = 768
        self.num_labels = num_labels
        # self.bert = BertModel(config)
        self.bert = AutoModel.from_pretrained(pretrained_model_name)
        # self.bert = model.bert
        self.dropout = nn.Dropout(0.1)
        self.batchNorm = nn.BatchNorm1d(768)
        self.classifier = nn.Sequential(
            # nn.Linear(config.hidden_size * 4, config.hidden_size * 2),
            # nn.LeakyReLU(),
            # nn.Linear(config.hidden_size * 2, config.hidden_size * 1),
            # nn.LeakyReLU(),
            # nn.Linear(config.hidden_size * 1, self.num_labels)
            nn.Linear(self.hidden_size * 4, self.num_labels)
        )
        # self.apply(self.init_bert_weights)
        # self.init_weights()
    def forward(self, AA, AD, RA, RD, labels=None):
        _,  AA_pooled_output = self.bert(AA['input_ids'], token_type_ids=AA['token_type_ids'], attention_mask=AA['attention_mask'], return_dict=False)
        AA_pooled_output = self.dropout(self.batchNorm(AA_pooled_output))
        _,  AD_pooled_output = self.bert(AD['input_ids'], token_type_ids=AD['token_type_ids'], attention_mask=AD['attention_mask'], return_dict=False)
        AD_pooled_output = self.dropout(self.batchNorm(AD_pooled_output))
        _,  RA_pooled_output = self.bert(RA['input_ids'], token_type_ids=RA['token_type_ids'], attention_mask=RA['attention_mask'], return_dict=False)
        RA_pooled_output = self.dropout(self.batchNorm(RA_pooled_output))
        _,  RD_pooled_output = self.bert(RD['input_ids'], token_type_ids=RD['token_type_ids'], attention_mask=RD['attention_mask'], return_dict=False)
        RD_pooled_output = self.dropout(self.batchNorm(RD_pooled_output))
        pooled_output = torch.cat((AA_pooled_output, AD_pooled_output, RA_pooled_output, RD_pooled_output), 1)
        # pooled_output = (AA_pooled_output + AD_pooled_output + RA_pooled_output + RD_pooled_output) / 4
        logits = self.classifier(pooled_output)

        loss = None
        if labels is not None:
            loss_fct = CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
        return  {'logits': logits, 'loss': loss, 'sentence_emb': pooled_output}


# class MyJointBert(BertPreTrainedModel):
#     def __init__(self, config):
#         super(MyJointBert, self).__init__(config)
#         self.num_labels = config.num_labels
#         # self.bert = BertModel(config)
#         self.bert_AA = model_AA.bert
#         self.bert_AD = model_AD.bert
#         self.bert_RA = model_RA.bert
#         self.bert_RD = model_RD.bert
#         self.dropout = nn.Dropout(config.hidden_dropout_prob)
#         self.classifier = nn.Sequential(
#             # nn.Linear(config.hidden_size * 4, config.hidden_size * 2),
#             # nn.LeakyReLU(),
#             # nn.Linear(config.hidden_size * 2, config.hidden_size * 1),
#             # nn.LeakyReLU(),
#             # nn.Linear(config.hidden_size * 1, self.num_labels)
#             nn.Linear(config.hidden_size * 4, self.num_labels)
#         )
#         # self.apply(self.init_bert_weights)
#         self.init_weights()
#     def forward(self, AA, AD, RA, RD, labels=None):
#         _,  AA_pooled_output = self.bert_AA(AA['input_ids'], token_type_ids=AA['segment'], attention_mask=AA['mask'], return_dict=False)
#         AA_pooled_output = self.dropout(AA_pooled_output)
#         _,  AD_pooled_output = self.bert_AD(AD['input_ids'], token_type_ids=AD['segment'], attention_mask=AD['mask'], return_dict=False)
#         AD_pooled_output = self.dropout(AD_pooled_output)
#         _,  RA_pooled_output = self.bert_RA(RA['input_ids'], token_type_ids=RA['segment'], attention_mask=RA['mask'], return_dict=False)
#         RA_pooled_output = self.dropout(RA_pooled_output)
#         _,  RD_pooled_output = self.bert_RD(RD['input_ids'], token_type_ids=RD['segment'], attention_mask=RD['mask'], return_dict=False)
#         RD_pooled_output = self.dropout(RD_pooled_output)
#         pooled_output = torch.cat((AA_pooled_output, AD_pooled_output, RA_pooled_output, RD_pooled_output), 1)
#         # pooled_output = (AA_pooled_output + AD_pooled_output + RA_pooled_output + RD_pooled_output) / 4
#         logits = self.classifier(pooled_output)

#         loss = None
#         if labels is not None:
#             loss_fct = CrossEntropyLoss()
#             loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
#         return  {'logits': logits, 'loss': loss, 'sentence_emb': pooled_output}

# %%
