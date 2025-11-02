for epoch in range(10):




# model saving
PATH='MODELS'
torch.save(net.state_dict(),PATH)