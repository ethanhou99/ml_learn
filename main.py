#!/usr/bin/python3

import os
import glob
import numpy as np
from PIL import Image
#from moviepy.editor import VideoFileClip

from resource.ssd import SSD300
from resource.utils import VehicleDetector

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #Ignore error msg

def process_images(detector): 
    filenames = glob.glob('test_images/*.jpg') #load img
    images = [np.asarray(Image.open(filename)) for filename in filenames] #img list
    results = [detector.detect(img) for img in images]
    for i, img in enumerate(results):
        image = Image.fromarray(img)
        image.save('output_images/test{}.jpg'.format(i+1), 'JPEG')

if __name__ == '__main__':
    input_shape=(300, 300, 3)
    model = SSD300(input_shape, num_classes=VehicleDetector.NUM_CLASSES)
    model.load_weights('./SSD300.hdf5', by_name=True) #modelname
    detector = VehicleDetector(model)

    process_images(detector)
    #process_videos(detector)
