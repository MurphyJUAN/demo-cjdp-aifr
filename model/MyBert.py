import torch
from transformers.models.bert.modeling_bert import BertPreTrainedModel, BertModel
import torch.nn as nn
from torch.nn import CrossEntropyLoss
from transformers import AutoModel, AutoTokenizer

class MyBert(BertPreTrainedModel):
    def __init__(self, config):
        super(MyBert, self).__init__(config)
        self.num_labels = config.num_labels
        # if 'bert' in  config.pretrained_model_name_or_path:
        self.bert = BertModel(config)
        # self.bert = AutoModel.from_pretrained('thunlp/Lawformer')
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, self.num_labels)
        # self.apply(self.init_bert_weights)
        # self.init_weights()
    def forward(self, input_ids, token_type_ids=None, attention_mask=None,labels=None):
        _,  pooled_output = self.bert(input_ids, token_type_ids=token_type_ids, attention_mask=attention_mask, return_dict=False)
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)

        loss = None
        if labels is not None:
            loss_fct = CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
        return  {'logits': logits, 'loss': loss, 'sentence_emb': pooled_output}

# class BertForClassification(BertPreTrainedModel):
#     def __init__(self, config, *model_args, **model_kwargs):
#         super(BertForClassification, self).__init__(config, *model_args, **model_kwargs)
#         self.num_labels = config.num_labels
#         self.MAX_LENGTH = config.max_length
#         self.DEVICE = model_kwargs['device']
#         self.pooling_strategy = model_kwargs['pooling_strategy']
#         self.bert = BertModel(config)
#         self.dropout = nn.Dropout(config.hidden_dropout_prob)
#         self.relu = nn.ReLU()

#         self.output_base = nn.Linear(num_encoder_hidden, self.num_labels)
#         self.init_weights()
#     def forward(self, input_ids, token_type_ids=None, attention_mask=None,labels=None, lengths= None, output_attention=False):
#         outputs = self.bert(input_ids, token_type_ids=token_type_ids,attention_mask=attention_mask)
#         sequence_output = outputs[0]
#         encoder_hidden_states = sequence_output.to(self.DEVICE)
#         ############## Baseline1 #####################
#         if self.pooling_strategy == 'cls':
#             cls_vector = encoder_hidden_states[:, 0, :]
#         elif self.pooling_strategy == 'reduce_mean':
#             cls_vector = encoder_hidden_states.sum(axis=1) / attention_mask.sum(axis=-1).unsqueeze(-1)
#         else:
#             print('>>>>> Wrong pooling strategy! >>>>>')
#             return
#         logits = self.output_base(cls_vector)

#         loss = None
#         if labels is not None:
#             B = logits.view(-1, self.num_labels).size(0)
#             loss_fct = CrossEntropyLoss()
#             loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))

#         output = (logits,) + outputs[2:]
#         if loss is not None:
#             return ((loss,) + cls_vector)
#         else:
#             return ((logits,) + cls_vector)