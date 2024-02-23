import numpy as np
from scipy.linalg import lstsq
import matplotlib.pyplot as plt
from displaySurfaceNormals import *
from displayOutput import *

subjectName = 'debug'

def photometricStereo(imarray, lightdirs):
    #pixel values is imarray
    #albedo is p
    #surface normals is N
    #source vectors is lightdirs
    k = 1
    lightdirs = k * lightdirs
    h, w, n = imarray.shape
    imarray = np.reshape(imarray,((h*w),n))
    p = []
    N = []
    for i in range(h*w):
        g,res,rank,s = lstsq(lightdirs,imarray[i,:])
        p.append(np.linalg.norm(g))
        N.append(g/np.linalg.norm(g))
    p = np.reshape(np.array(p),(h,w))
    N = np.reshape(np.array(N),(h,w,3))
    return p,N
