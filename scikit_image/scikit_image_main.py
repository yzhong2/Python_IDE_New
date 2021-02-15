import numpy as np
import skimage
from skimage import data
from scikit_image_function import *
from skimage import img_as_float
import os

print(skimage.__version__)

### this is for testing the checkshape function
check = checkshape(dim_array = (8, 8), filename='check.pdf')
### this data is from skimage data set
camera = data.camera()
plt.imshow(camera)
plt.savefig('person_look.png')
### this data is for

camera_multiple = camera * 3
print(camera_multiple.shape)
print(type(camera_multiple))
print(camera_multiple.dtype)
print('the max of camera_multile is ')
print(camera_multiple.max())
print('the max of camera is')
print(camera.max())

### this is for image filter
camera_multiple_float = img_as_float(camera_multiple)
print('type of camera_multiple_float')
print(camera_multiple_float.max())
print('this is min value for camera_multiple_float min')
print(camera_multiple_float.min())

### this for filtering the image
from skimage import filters
print('this is for filters')

camera_filter = filters.sobel(camera)
plt.subplot(141)
plt.imshow(camera)
plt.subplot(142)
plt.imshow(camera_filter)

plt.show()



