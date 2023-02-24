# %%
import torch
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
        # self.bert = BertModel(config)
        # Load embeding model
        PRETRAINED_MODEL_NAME = "bert-base-chinese" 
        model = MyBert.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=3)
        if len(emb_name) > 0:
            model.load_state_dict(torch.load(emb_name))
            print(f'>>>>Finish loadding from {emb_name}')
        self.bert = model.bert
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
        _,  AA_pooled_output = self.bert(AA['input_ids'], token_type_ids=AA['segment'], attention_mask=AA['mask'], return_dict=False)
        AA_pooled_output = self.dropout(self.batchNorm(AA_pooled_output))
        _,  AD_pooled_output = self.bert(AD['input_ids'], token_type_ids=AD['segment'], attention_mask=AD['mask'], return_dict=False)
        AD_pooled_output = self.dropout(self.batchNorm(AD_pooled_output))
        _,  RA_pooled_output = self.bert(RA['input_ids'], token_type_ids=RA['segment'], attention_mask=RA['mask'], return_dict=False)
        RA_pooled_output = self.dropout(self.batchNorm(RA_pooled_output))
        _,  RD_pooled_output = self.bert(RD['input_ids'], token_type_ids=RD['segment'], attention_mask=RD['mask'], return_dict=False)
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
