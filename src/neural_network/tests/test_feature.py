from feature import DirectionZoneFeature
from segmenter import Segmenter, HistogramDirection
import unittest
import numpy as np
import pytest

"""
Just alias to avoid long property call
inside the TestFeature class
"""
W = 255
H = HistogramDirection.horizontal
RD = HistogramDirection.right_diagonal
V = HistogramDirection.vertical
LF = HistogramDirection.left_diagonal

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.image = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, W, 0, W, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, W, 0, 0, W, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, W, 0, 0, 0, W, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, W, W, W, W, W, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0],
                               [0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0],
                               [0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        self.segmented_image = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, W, 0, W, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, W, 0, 0, W, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, W, 0, 0, 0, W, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, W, W, W, W, W, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0],
                                         [0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0],
                                         [0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    def test_feature(self):
        segmenter = Segmenter()
        segmenter.use_labeling()
        #  Once the picture is segmented we beed to apply the zone feature on it
        feature = DirectionZoneFeature()
        feature.process_zones()
