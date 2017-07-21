import os, cv2
import numpy as np
from PIL import Image
from random import shuffle
import matplotlib.pyplot as plt

f = []
labels = []
traindir = 'images/Latin/%s/'

for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	prev = len(f)
	fnames = os.listdir(traindir % c)
	f.extend(fnames)
	labels.extend([c] * len(fnames))

processed = []
j = 0
for i in range(len(f)):
        image = Image.open((traindir % labels[i]) + f[i])
        cpy = image.copy()
        cpy = cpy.resize((28,28))
        #image = cv2.imread((traindir % labels[i]) + f[i])
        
        processed.append(np.array(cpy)[:,:,3])
        image.close()
        j += 1
        if j % 100 == 0:
                print(j, np.array(processed).shape)

for i in range(len(labels)):
        vec = [0] * 26
        vec[ord(labels[i]) - ord('A')] = 1
        labels[i] = np.array(vec)

labels = np.array(labels)
shuffler = list(zip(processed, labels))
shuffle(shuffler)
processed, labels = zip(*shuffler)
savedata = np.array(processed)
np.save('train.npy', savedata)
np.save('train_labels.npy', labels)
print(savedata.shape)
