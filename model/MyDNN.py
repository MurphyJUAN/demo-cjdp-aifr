import torch
import torch.nn as nn
import torch.nn.functional as F
num_or_size_splits = 4
class SplitedDNN(nn.Module):
    def __init__(self, input_size, bottleneck_size=100, output_size=3):
        super(SplitedDNN, self).__init__()

        self.bottleneck_size = bottleneck_size
        self.num_labels = 3

        self.split_layer_AA = nn.Linear(in_features=input_size, out_features=bottleneck_size) 
        self.split_layer_AD = nn.Linear(in_features=input_size, out_features=bottleneck_size) 
        self.split_layer_RA = nn.Linear(in_features=input_size, out_features=bottleneck_size) 
        self.split_layer_RD = nn.Linear(in_features=input_size, out_features=bottleneck_size) 


        self.hidden_layers = nn.ModuleList([
            nn.Linear(in_features=bottleneck_size * num_or_size_splits, out_features=bottleneck_size * num_or_size_splits // 2),
            nn.Linear(in_features=bottleneck_size * num_or_size_splits // 2, out_features=bottleneck_size * num_or_size_splits // 4),
            nn.Linear(in_features=bottleneck_size * num_or_size_splits // 4, out_features=bottleneck_size * num_or_size_splits // 8),
            nn.Linear(in_features=bottleneck_size * num_or_size_splits // 8, out_features=bottleneck_size * num_or_size_splits // 16),
            nn.Linear(in_features=bottleneck_size * num_or_size_splits // 16, out_features=output_size)
        ])

    def forward(self, AA, AD, RA, RD, labels=None):
        # 分割輸入先分別通過 nn 再 concatenate 起來
        AA_hidden = F.gelu(self.split_layer_AA(AA))
        AD_hidden = F.gelu(self.split_layer_AD(AD))
        RA_hidden = F.gelu(self.split_layer_RA(RA))
        RD_hidden = F.gelu(self.split_layer_RD(RD))
        x = torch.cat([AA_hidden, AD_hidden, RA_hidden, RD_hidden], dim = 1)

        # 逐層處理
        for layer in self.hidden_layers:
            x = F.gelu(layer(x))

        loss = None
        if labels is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = loss_fct(x.view(-1, self.num_labels), labels.view(-1))

        return {'logits': x, 'loss': loss}