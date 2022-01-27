#Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, misc
import imread,imresize



class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.

        '''

        
        # Write your code here
        self.degrees=degrees

    def __call__(self, sample):
        '''
            Arguments:
            image(sample) (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        img = numpy.array(sample)
        return scipy.ndimage.rotate(img,self.degrees)
