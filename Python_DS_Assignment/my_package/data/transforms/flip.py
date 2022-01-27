#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc 
import imread,imresize



class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''


        # Write your code here
        self.flip_type=flip_type


        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        img = numpy.array(image)
        if self.flip_type=='horizontal' :
            return np.flip(img,0)
        else :
            return np.flip(img,1)

        
       