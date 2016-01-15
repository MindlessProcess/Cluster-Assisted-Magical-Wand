from neuron import Neuron
from supervisor import *
import sys
import os
import cv2
import thinning
import numpy

from feature import DirectionZoneFeature
from pre_process import ImageDataTreatment
LEARNING_RATE = 1
RANGE_MIN = -1
RANGE_MAX = 1
VERBOSE = len(sys.argv) > 1 and '-v' in sys.argv

def display_image(image):
    for y in range(len(image)):
        for x in range(len(image[y])):
            sys.stdout.write('%d, ' % image[y][x])
        print('')

def main():
    if False == os.path.isfile(sys.argv[1]):
        print "File [" + sys.argv[1] + "] not found!"
        return False
    data_canvas = ImageDataTreatment(sys.argv[1])
    data_canvas.preprocess_apply()
    numpy.set_printoptions(threshold='nan')

    super_neuron = SuperNeuron((RANGE_MIN, RANGE_MAX))
    character = super_neuron.activate(data_canvas.main_picture)
    print 'Found: %c' % character

if __name__ == '__main__':
    main()
