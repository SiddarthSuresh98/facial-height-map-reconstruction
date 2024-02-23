import numpy as np    
def getSurface(surfaceNormals, method):
    p = surfaceNormals[:,:,0]/surfaceNormals[:,:,2]
    q = surfaceNormals[:,:,1]/surfaceNormals[:,:,2]
    if method == 'row-column':
        fz = np.zeros((surfaceNormals.shape[0], surfaceNormals.shape[1]))
        for i in range(fz.shape[0]):
            for j in range(fz.shape[1]):
                fz[i,j] += np.sum(p[i,0:j])
                fz[i,j] += np.sum(q[0:i,j]) 
        return fz               
    if method == 'column-row':
        fz = np.zeros((surfaceNormals.shape[0], surfaceNormals.shape[1]))
        for i in range(fz.shape[0]):
            for j in range(fz.shape[1]):
                fz[i,j] += np.sum(q[0:i,j]) 
                fz[i,j] += np.sum(p[i,0:j])
        return fz
    if method == 'average':
        fz = np.zeros((surfaceNormals.shape[0], surfaceNormals.shape[1]))
        for i in range(fz.shape[0]):
            for j in range(fz.shape[1]):
                fz[i,j] += np.sum(q[0:i,j]) 
                fz[i,j] += np.sum(p[i,0:j])
        for i in range(fz.shape[0]):
            for j in range(fz.shape[1]):
                fz[i,j] += np.sum(p[i,0:j])
                fz[i,j] += np.sum(q[0:i,j])
        for i in range(fz.shape[0]):
            for j in range(fz.shape[1]):
                fz[i,j] /= 2
        return fz
    if method == 'random':
        fz = np.zeros((surfaceNormals.shape[0], surfaceNormals.shape[1]))
        for i in range(fz.shape[0]):
            for j in range(fz.shape[1]):
                #row-column
                fz[i,j] += np.sum(q[0:i,j]) 
                fz[i,j] += np.sum(p[i,0:j])
                #column-row
                fz[i,j] += np.sum(q[0:i,j]) 
                fz[i,j] += np.sum(p[i,0:j])
                #zig-zag
                row = 0
                col = 0
                while row < i and col < j:
                    #down step
                    row +=1
                    fz[i,j] += q[row,col]
                    #right step
                    col +=1
                    fz[i,j] += p[row,col]
                #zig-zag
                row = 0
                col = 0
                while row < i and col < j:
                    #right step
                    col +=1
                    fz[i,j] += p[row,col]
                    #down step
                    row +=1
                    fz[i,j] += q[row,col]
                fz[i,j] /=4
        return fz