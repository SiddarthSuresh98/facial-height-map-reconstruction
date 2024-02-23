import numpy as np
import matplotlib.pyplot as plt

def prepareData(imArray, ambientImage):
    for i in range(imArray.shape[2]):
        imArray[:,:,i] = imArray[:,:,i] - ambientImage
        imArray[:,:,i][imArray[:,:,i]<0] = 0
    return imArray/ np.max(imArray)

