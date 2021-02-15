import numpy as np
import matplotlib.pyplot as plt

### this function is to form a check board
### also the function will save the image into a file
def checkshape(dim_array, filename) :
    check = np.zeros(dim_array) ### this is initial np array
    check[::2, 1::2] = 1  # 0 value means black and white value means 1
    check[1::2, ::2] = 1
    #plt.figure()
    plt.imshow(check, cmap='gray', interpolation='nearest')
    #plt.show()
    #plt.close()
    ### this is for saving the image into the file
    plt.savefig(filename)
    return check


# check = checkshape((8, 8))
# print('check is ')
# print(check)