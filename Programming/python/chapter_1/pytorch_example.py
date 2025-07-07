import torch
from torch import nn

model = nn.Sequential(nn.Linear(10, 5), nn.ReLU(), nn.Linear(5, 1))
input_tensor = torch.randn(1, 10)
output = model(input_tensor)
print(output)
