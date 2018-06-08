import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from os import listdir
from PIL import Image
import tensorflow as tf
import matplotlib.image as mpimg
import skimage.measure


'''
r=6
def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = cv.imread(path + image)
        loadedImages.append(img)

    return loadedImages

path = '/home/tarun/brail/input/'
imgs= loadImages(path)

thresh=[]
for image in imgs:
    thresh.append(cv.threshold(image, 200, 255, cv.THRESH_BINARY)[1])


plt.subplot(2, 2, 1)
plt.imshow(imgs[r])

plt.subplot(2, 2, 2)
plt.imshow(thresh[r])

plt.subplot(2, 2, 3)
plt.hist(imgs[r].ravel(),256,[0,256])

plt.subplot(2, 2, 4)
plt.hist(thresh[r].ravel(),256,[0,256])

plt.show()
'''
#code for neural network

#pooling
poolLC = 6
def pool(image):
    img = np.array(Image.open(image))
    img=skimage.measure.block_reduce(img, (poolLC,poolLC), np.max)
    #img = tf.layers.max_pooling2d(img, [2,2], [2,2])
    return img

Image.fromarray(pool('input/444.jpg')).show()
#pool('input/444.jpg')
