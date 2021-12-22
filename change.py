from os import walk
import json
import h5py
from PIL import Image
from torchvision import transforms
mypath = "datasets"

classes = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']
# f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    print(filenames)
for tmpfile in filenames:
    with open(mypath+'/'+tmpfile, newline='') as jsonfile:
        data = json.load(jsonfile)
    for tmpval in data:
        tmpfilename  = (tmpval['filename'].split("/",1))[1]
        image = transforms.ToTensor() (Image.open('./train/'+tmpfile[:-4]+'/'+tmpfilename))
        image_size = image.size()
        fp = open('train/'+tmpfile[:-4]+'/'+tmpfilename[:-4]+".txt", "w")

        for tmpanno in tmpval['annotations']:
            # annotations
            label_idx = int(classes.index(tmpanno["class"]))
            x_center = (tmpanno['x'] + tmpanno['width']/2)/image_size[2]
            y_center = (tmpanno['y'] + tmpanno['height']/2)/image_size[1]
            width = tmpanno['width']/image_size[2]
            height = tmpanno['height']/image_size[1]
            fp.write(str(label_idx) + ' ' + str(x_center) + ' ' +
            str(y_center) + ' ' + str(width) + ' '+ str(height) + '\n')
