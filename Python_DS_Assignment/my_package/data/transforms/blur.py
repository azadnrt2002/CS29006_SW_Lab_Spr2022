#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc 
from PIL import Image, ImageFilter
import imread,imresize



class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        # Write your code here
        self.radius=radius

        

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Write your code here
        img=numpy.array(image)
        return img.filter(ImageFilter.GaussianBlur(radius = self.radius))

        

