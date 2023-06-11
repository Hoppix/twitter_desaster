import torch.nn as nn
import pandas as pd
import numpy as np


class TweetDisasterClassifier(nn.Module):
    def __init__(self, input_size, hidden_sizes, num_classes):
        super(TweetDisasterClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_sizes[0])
        self.relu = nn.ReLU()
        self.hidden_layers = nn.ModuleList()
        
        for i in range(len(hidden_sizes) - 1):
            self.hidden_layers.append(nn.Linear(hidden_sizes[i], hidden_sizes[i+1]))
        
        self.fc_last = nn.Linear(hidden_sizes[-1], num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)

        for hidden_layer in self.hidden_layers:
            out = hidden_layer(out)
            out = self.relu(out)
        
        out = self.fc_last(out)
        return out