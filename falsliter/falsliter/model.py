import torch
import torch.nn as nn
import torch.nn.functional as F

class FalsLiterModel(nn.Module):
    def __init__(self, n_size, v_size, e_size=256, h_size=1024, dropout=0.5):
        super().__init__()
        self.emb = nn.Embedding(v_size, e_size)
        self.norm0 = nn.LayerNorm(e_size)
        self.norm1 = nn.LayerNorm(h_size)
        self.norm2 = nn.LayerNorm(h_size)
        self.norm3 = nn.LayerNorm(h_size)
        self.fc1 = nn.Linear(e_size * 2 * n_size, h_size)
        self.fc2 = nn.Linear(h_size, h_size)
        self.fc3 = nn.Linear(h_size, h_size)
        self.cls = nn.Linear(h_size, v_size)
        self.act = nn.GELU()
        self.dropout = nn.Dropout(dropout)

    def __call__(self, batch):
        x = self.emb(batch['src'])
        x = self.norm0(x)
        x = x.flatten(start_dim=-2)
        x = self.dropout(self.act(self.fc1(x)))
        x = self.norm1(x)
        x = self.dropout(self.act(self.fc2(x)))
        x = self.norm2(x)
        x = self.dropout(self.act(self.fc3(x)))
        x = self.norm3(x)
        x = self.cls(x)
        return x

