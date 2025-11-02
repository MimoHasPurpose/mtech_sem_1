import torch.nn as nn
import torch.optim as optim
criteion=nn.CrossEntropyLoss()
optimizer=optim.SGD(net.parameters(),lr=0.001,momentum=0.9)