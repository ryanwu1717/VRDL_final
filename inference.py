import torchvision.transforms as transform
import os
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from os import walk

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def inference(imagePath, modelPath):
    # with open("/home/yoyo30169/VRDL dataset/datasets/classes.txt", "r") as f:
    #     classes = f.read().split("\n")
    classes = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']
    inputSize = 448
    data_transforms_test = transform.Compose([
        transform.Resize(inputSize),
        transform.CenterCrop(inputSize),
        transform.ToTensor(),
        transform.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    model = torch.load(modelPath).to(device)
    model.eval()
    image = Image.open(imagePath).convert('RGB')
    image_tensor = data_transforms_test(image).float()
    image_tensor = image_tensor.unsqueeze_(0).to(device)
    output = model(image_tensor)
    # score, pred_int = torch.max(output.data, 1)
    # prediction = classes[int(pred_int)]

    # print(score, prediction)

    return output


# with open('testing_img_order.txt') as f:
#     test_images = [x.strip() for x in f.readlines()]  # all the testing images
mypath = "test"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
submission = []
for img in f :  # image order is important to your result
    predicted_class = inference('TEST/' +img, '"Efficientnet-b7"_0.998.pkl')  # the predicted category
    submission.append(output)

submission.to_csv('result/S2.csv', index=False)
