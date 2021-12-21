import torch
import numpy as np
import torch.nn as nn
import dataloader
import torch.utils.data as Data
import matplotlib.pyplot as plt
import torch.optim as optim
from torchvision import models
from efficientnet_pytorch import EfficientNet


def pretrained_efficientnetb7():
    model = EfficientNet.from_pretrained('efficientnet-b7', num_classes=8)
    nn.Dropout(0.5, inplace=True)
    return model


def run_model(net, optimizer, train_loader, Epoch, Loss_fuc):
    high_acc = 0

    for epoch in range(Epoch):
        accuracy = 0
        count = 0
        totalLoss = 0
        for x, y in train_loader:
            x = x.float()
            print(x,y)
            if use_cuda:
                y = np.array(y, int) 
                y = torch.Tensor(y) 
                x, y = x.cuda(), y.cuda()
            output = net(x)
            count += len(x)
            _, pred_label = torch.max(output, 1)
            accuracy += (pred_label == y).sum().item()
            loss = Loss_fuc(output, y)
            totalLoss += loss.item()*len(y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        train_acc = accuracy/count
        print("Train Loss: {}".format(totalLoss / count))
        print("Train Accuracy: {}".format(accuracy / count))

        print('Save model')
        if train_acc > high_acc:
            torch.save(
                net, f'result/"Efficientnet-b7"_{str(train_acc)}.pkl')
            high_acc = train_acc

    return net

if __name__ == '__main__':
    # Hyper parameter
    batch_size = 12
    Learning_rate = 0.001
    Epoch = 50
    Loss_fuc = nn.CrossEntropyLoss()
    net = pretrained_efficientnetb7()
    optimizer = optim.SGD(net.parameters(), lr=Learning_rate,
                        momentum=0.9, weight_decay=0.0005)


    use_cuda = False
    if torch.cuda.is_available():
        print("use_cuda")
        use_cuda = True


    # data loader
    train_data = dataloader.Loader('train', 'train')
    train_loader = Data.DataLoader(
        dataset=train_data, batch_size=batch_size, shuffle=True, num_workers=2)

    if use_cuda:
        net = net.cuda()

    model = run_model(net, optimizer, train_loader, Epoch, Loss_fuc)
