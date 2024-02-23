import numpy as np
import matplotlib.pyplot as plt
import copy

def showImage(i):
    plt.imshow(i)
    plt.show()

#Sum squared distance
def ssd(i1,i2):
    return np.sum((i1-i2)**2)

#function to crop from the center
def crop(img,cropW,cropH):
    y,x = img.shape
    startx = x//2-(cropW//2)
    starty = y//2-(cropH//2)    
    print(np.shape(img[startx:startx+cropW,starty:starty+cropH]))
    return img[startx:startx+cropW,starty:starty+cropH]

def alignChannels(img, max_shift):
    #showImage(img[:,:,0])
    #showImage(img[:,:,1])
    #showImage(img[:,:,2])
    np.random.seed(0)
    print(np.shape(img))
    h,w,_ = np.shape(img)
    #set shape for final images.
    c1I = np.random.random((img.shape[0],img.shape[1]))
    c2I = np.random.random((img.shape[0],img.shape[1]))
    # 2 channels, i,j
    shift = np.random.random((2,2))
    #Setting channel shift to a high number
    channel1_shift = 99999999
    channel2_shift = 99999999
    #Cropping works for most toy images and all Produkin. Derived results for toy set without cropping as that gave better results.
    #for toy set, comment other a,b,c and uncomment the following a,b,c
    #a = img[:,:,0]
    #b = img[:,:,1]
    #c = img[:,:,2]
    a = crop(img[:,:,0], w-30,h-30)
    b = crop(img[:,:,1], w-30,h-30)
    c = crop(img[:,:,2], w-30,h-30)
    #producing cropped test image
    test_img = np.random.random((a.shape[0],a.shape[1],3))
    test_img[:,:,0] = a
    test_img[:,:,1] = b
    test_img[:,:,2] = c
    #looping over all shifts in range -max_shift, max_shift in both x and y directions
    for i in range(-max_shift[0], max_shift[0]+1):
        for j in range(-max_shift[1], max_shift[1]+1):
            #checking ssd for test image and setting shift to original image for channel2
            if ssd(test_img[:,:,0], np.roll(test_img[:,:,1],shift=[i,j],axis=[0,1])) < channel1_shift:
                shift[0] = [i,j]
                c1I = np.roll(img[:,:,1],shift=[i,j],axis=[0,1])
                channel1_shift = ssd(test_img[:,:,0],np.roll(test_img[:,:,1],shift=[i,j],axis=[0,1]))
            #checking ssd for test image and setting shift to original image for channel3
            if ssd(test_img[:,:,0],np.roll(test_img[:,:,2],shift=[i,j],axis=[0,1])) < channel2_shift:
                shift[1] = [i,j]
                c2I = np.roll(img[:,:,2],shift=[i,j],axis=[0,1])
                channel2_shift = ssd(test_img[:,:,0],np.roll(test_img[:,:,2],shift=[i,j],axis=[0,1]))
    #Setting the final image
    final_image = np.random.random((img.shape[0],img.shape[1],img.shape[2]))
    final_image[:,:,0] = img[:,:,0]
    final_image[:,:,1] = c1I
    final_image[:,:,2] = c2I
    return final_image,shift
                

