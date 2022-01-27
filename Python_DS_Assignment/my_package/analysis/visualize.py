#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc 
import imread,imresize
from PIL import Image, ImageDraw as D
def plot_visualization(pred_boxes,pred_mask): # Write the required arguments
  pred_mask = D.Draw(pred_mask)
  # The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
  for i in range(len(pred_boxes)):
    pred_mask.rectangle([(pred_boxes[0],pred_boxes[1]),(pred_boxes[2],pred_boxes[3])],outline="white")
 
  pred_mask.show()


