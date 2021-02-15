import os

proPath = 'C:/Users/yi.zhong/Documents/Python_IDE_New/ProjectOne'
os.chdir(proPath)
print('the current path is %s', os.getcwd())
## this is how to run a script from a python interpreter example
## exec(open("python_practice.py").read())
## this is for the image example
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# print('sucessful export all packages')
# im = np.zeros((20, 20))
# im[5:-5, 5:-5] = 1
# im = ndimage.distance_transform_bf(im)
# print(im.shape)
# print(im.data)
# print('the min value of im after transformation')
# print(np.min(im))
# print(type(im))
# print('the maxium of im after transformation')
# print(np.max(im))

# plt.figure(figsize=(16, 5))
# plt.subplot(141)
# plt.imshow(im, interpolation='nearest')
# plt.axis('off')
# plt.title('Original Image', fontsize=20)
# ### this is for generate a array of normal distribution data
# im_noise = im + 0.2 * np.random.randn(*im.shape)
# plt.subplot(142)
# plt.imshow(im_noise)
# plt.axis('off')
# plt.title('Noise Image', fontsize=20)
# ### this is for the filter image
# im_filter = ndimage.median_filter(im_noise, 3)
# plt.subplot(143)
# plt.imshow(im_filter)
# plt.axis('off')
# plt.title('filter image', fontsize=20)
#
# ### this ste I will get the erroe pattern
# im_error = abs(im_noise - im_filter)
# plt.subplot(144)
# plt.imshow(im_error, cmap=plt.cm.hot, interpolation='nearest')
# plt.title('error', fontsize=20)
# plt.axis('off')
# plt.subplots_adjust(left=0.1, right=0.9, wspace=0.01, top=0.9,bottom=0.0)
# plt.show()
im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
plt.figure(figsize=(13,5))
plt.subplot(141)
plt.axis('off')

plt.title('Original', fontsize=15)
plt.imshow(im, cmap=plt.cm.gray)
# #### this is the
im1 = ndimage.rotate(im,15, axes=(1,0), mode='constant')
plt.subplot(142)
plt.axis('off')
plt.imshow(im1)
plt.title('1,0 rotation')
im2 = ndimage.rotate(im, 15, axes=(0,1), mode='constant')
plt.subplot(143)
plt.imshow(im2)
plt.axis('off')
plt.title('0,1 rotation')

im2 = ndimage.gaussian_filter(im2, 8, mode='constant')
### this step is for the edge detection
sbx = ndimage.sobel(im2, axis=0)
print(type(sbx))
print('the shape of im2 is ')
print(im2.shape)
print(sbx.shape)
print(np.min(sbx))
print(np.max(sbx))
sby = ndimage.sobel(im2, axis=1)
sob = np.hypot(sbx, sby)
print(sob.shape)
plt.subplot(144)
plt.imshow(sob)
plt.title('Whole Gradient')
plt.axis('off')
plt.subplots_adjust(left=0.1, top=0.9, wspace=0.01, right=0.9)
noise_im = im2 + 0.2 * np.random.random(im2.shape)
print(np.min(noise_im))
test = np.random.random(im2.shape)
print(type(test))
print(test.shape)
plt.show()

