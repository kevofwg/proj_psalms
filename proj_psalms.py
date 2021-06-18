import pycrafter6500
import numpy as np

import PIL.Image

import matplotlib.pyplot as plt



# make arrays for images

def make_arrays(h):

    x = np.arange(0, 1920, 1)

    y = np.arange(0, 1080, 1)

    #z = np.arange(-5, 5, 1)

    #z = 1

    xx, yy = np.meshgrid(x, y, sparse=True)

    #g = .20

    g = (2*np.pi)/(1080/6)
    z = g*h 
    # f = np.sin(g*xx)*np.cos(g*yy)+np.sin(g*yy)*np.cos(g*zz)+np.cos(g*xx)*np.sin(g*zz)

    f = (np.sin(g * xx) * np.cos(g * yy)) + (np.sin(g * yy) * np.cos(g * z)) + (np.cos(g * xx) * np.sin(g * z))


    h = plt.contourf(x, y, f//119)
     
    plt.show()
    return f


def start_show():

    images = []

    for i in [0,0.5,1]:
        f = make_arrays(i)
        images.append((f))
    
    import pycrafter6500

    dlp=pycrafter6500.dmd()


    dlp.stopsequence()


    dlp.changemode(3)


    exposure=[1000000]*30

    dark_time=[500000]*30

    trigger_in=[False]*30

    trigger_out=[1]*30


    dlp.defsequence(images,exposure,trigger_in,dark_time,trigger_out,0)


    dlp.startsequence()



#make_arrays()

start_show()




