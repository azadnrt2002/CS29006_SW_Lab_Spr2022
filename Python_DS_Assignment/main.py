#Imports
from types import DynamicClassAttribute
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.analysis import plot_visualization
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image

def experiment(annotation_file, segmentor, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        segmentor: The image segmentor
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    dataset = Dataset(annotation_file, transforms)


    #Iterate over all data item

    for data in dataset :
        inp = data[img_fn]  
    #Get the predictions from the segmentor.
        pred_boxes, pred_mask, pred_class, pred_score = segmentor(inp)
    #Draw the segmentation maps on the image and save them.
        plot_visualization(pred_boxes,pred_mask)
    #Do the required analysis experiments.
    


def main():
    segmentor = InstanceSegmentationModel()
    experiment('./data/annotations.jsonl', segmentor, [FlipImage(), BlurImage()], None) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
