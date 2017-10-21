
# coding: utf-8

# In[199]:


import numpy as np
import scipy
from scipy.misc import imread, imsave, imresize
import skimage
from skimage import data
from matplotlib import pyplot as plt
from skimage.util.shape import view_as_blocks
from skimage.transform import rescale, resize, downscale_local_mean
from skimage import feature
from skimage.transform import warp, AffineTransform
from skimage import io
get_ipython().magic(u'matplotlib inline')
from PIL import Image

img = np.array(Image.open('checkerboard.png').convert('L'))
# img =io.imread('checkerboard.png')
image=skimage.color.rgb2gray(img)
plt.imshow(image,cmap='gray')
plt.show()



# In[200]:


# rows =3
# columns= 2
# mylist = [[0 for x in range(columns)] for x in range(rows)]
# for i in range(rows):
#     for j in range(columns):
#         mylist[i][j] = '%s,%s'%(i,j)
# print mylist









Sigma = 0
rows =7
mycoords=[rows]
for i in range(rows):
    mycoords.append([feature.corner_peaks(feature.corner_harris(image,sigma=Sigma), min_distance=12,threshold_rel=0)])
    Sigma = 0.2 + Sigma
#     print ' i : %d , Sigma : %f ' % (i,Sigma
# k : float, optional 
# Sensitivity factor to separate corners from edges, typically in range [0, 0.2].
# Small values of k result in detection of sharp corners.  
# method : {‘k’, ‘eps’}, optional
# Method to compute the response image from the auto-correlation matrix.
#     mycoords.append([feature.corner_peaks(feature.corner_harris(image,method='k',k=1,sigma=sigma), min_distance=12,threshold_rel=0)])
 


print mycoords [1][0][:][:,0]
print mycoords [1][0][:][:,1]
print '++++++++++++++++++++++'
print mycoords [6][0][:][:,0]
print mycoords [6][0][:][:,1]


# In[201]:



def plot_coords(index, title, im, coords):
    plt.subplot(index)
    plt.imshow(image)
#   plt.plot(mycoords[1][:, 1], mycoords[1][:, 0], '+r', markersize=5)
#     plt.plot( mycoords[1][0][:][:,1],mycoords[1][0][:][:,0], '+r', markersize=5)
    plt.plot( mycoords[6][0][:][:,1],mycoords[6][0][:][:,0], '+r', markersize=6)
    plt.title(title)
    plt.axis('off')

plt.gray()
index = 111
plot_coords(index, '', image, mycoords)
# plt.tight_layout(w_pad=0)
plt.show()

