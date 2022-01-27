#Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, misc
import imread,imresize
from PIL import Image




class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file=annotation_file
        self.transforms=transforms
        
        

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.annotation_file)
        
        

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_png_ann: the segmentation annotation image (in the form of a numpy array) (shape: (1, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image.
            5. Return the dictionary of the transformed image and annotations as specified.
        '''
        image = numpy.array(imread(self.annotation_file[idx][img_fn]))
        image = image.transpose(2,1,0)

        gt_png_ann = numpy.array(imread(self.annotation_file[idx][png_ann_fn]))
        gt_png_ann = np.expand_dims(gt_png_ann, axis=0)

        gt_png_ann = gt_png_ann/255.
        image = image/255.

        for trans in self.transforms :
            image = trans(image)
            gt_png_ann = trans(gt_png_ann)

        return {{"img_fn": image, "png_ann_fn":gt_png_ann ,"bboxes": [{"bbox": [189.82, 111.18, 72.06, 67.41],"category": "tv","category_id": 72}, {"bbox": [4.19, 148.57, 150.17, 178.69],"category": "chair","category_id": 62}, {"bbox": [201.58, 198.92, 296.3, 176.08],"category": "couch","category_id": 63}, {"bbox": [0.0, 235.0, 500.0, 140.0],"category": "carpet","category_id": 101}, {"bbox": [145.0, 167.0, 153.0, 82.0],"category": "shelf","category_id": 156}, {"bbox": [0.0, 0.0, 255.0, 257.0],"category": "wall-concrete","category_id": 172}, {"bbox": [249.0, 0.0, 251.0, 341.0],"category": "wall-other","category_id": 173}, {"bbox": [4.0, 111.0, 494.0, 264.0],"category": "stuff-other","category_id": 183}]}}


         
        