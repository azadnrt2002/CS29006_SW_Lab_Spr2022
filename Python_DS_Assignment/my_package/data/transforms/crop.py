#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc 
import imread,imresize


class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type
  
        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        img = numpy.array(image)
        y,x=img.shape
        if img.crop_type=='center' :
            return img[(y/2)-(h/2):(y/2)+(h/2),(x/2)-(w/2):(x/2)+(w/2)]
        else :
            return img[:h,:w]
        


        # Write your code here

        

 