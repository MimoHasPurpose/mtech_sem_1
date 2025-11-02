import torch
import os
from torch import nn
from torch.utils.data import dataloader
from torchvision import datasets, transforms

device=torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
# print(device)


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1=nn.Conv2d(3,6,5)
        self.fc1=nn.Linear(16*5*5,152)
    def forward(self, x):
        return x
