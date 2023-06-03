import torch
import torch.nn as nn
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

# MNIST dataset: 
train_dataset = datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)

test_dataset = datasets.MNIST(root='./data', train=False, transform=transforms.ToTensor())

# Data loader:
train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

test_loader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

# Fully connected neural network with one hidden layer:
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(784, 500) 
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(500, 10)  
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        # no activation and no softmax at the end
        return out

model = NeuralNet()

# Loss and optimizer:
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  

# Train the model:
n_total_steps = len(train_loader)
num_epochs = 3

for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):  
        # resized: [100, 784]
        images = images.reshape(-1, 28*28)
        
        # Forward pass:
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward and optimize:
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print (f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{n_total_steps}], Loss: {loss.item():.4f}')

# Test the model:
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_loader:
        images = images.reshape(-1, 28*28)

        outputs = model(images)

        _, predicted = torch.max(outputs.data, 1)
        n_samples += labels.size(0)
        n_correct += (predicted == labels).sum().item()

    acc = 100.0 * n_correct / n_samples
    print(f'Accuracy of the network on the 10000 test images: {acc} %')
