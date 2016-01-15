import sys
import random

from base_neuron import BaseNeuron
from weight import Weight
from output import NeuronOutput
from feature import DirectionZoneFeature

class Neuron(BaseNeuron):
    """This is a class that implements an artificial neuron."""
    def __init__(self, weight_range):
        super(self.__class__, self).__init__()
        # for i in range(num_inputs):
        #     self.weights.append((Weight(weight_range), False))

    def transfert(self, inputs):
        """Transfert method."""
        self.scalar = self.weights[len(self.weights) - 1]
        for i in range(len(self.weights) - 1):
            self.scalar += inputs[i] * self.weights[i].get_value()
        return self.scalar

    def activate(self, inputs):
        """Activate the artificial neuron."""
        feature = DirectionZoneFeature(inputs)
        zone_info = feature.process_single_zone(inputs)
        print 'zone_info.num_h_lines: %d' % zone_info.num_h_lines
        print 'zone_info.num_v_lines: %d' % zone_info.num_v_lines
        print 'zone_info.num_rd_lines: %d' % zone_info.num_rd_lines
        print 'zone_info.num_ld_lines: %d' % zone_info.num_ld_lines

        return NeuronOutput((zone_info.num_h_lines, zone_info.num_v_lines, zone_info.num_rd_lines, zone_info.num_ld_lines, zone_info.total_length_h_lines, zone_info.total_length_v_lines, zone_info.total_length_rd_lines, zone_info.total_length_ld_lines))

    def learn(self, inputs, expected):
        """Apply the learning rule on each weighted connection."""
        """Don't forget the bias !"""
        for i in range(len(self.weights)):
            self.weights[i].recompute(self.learning_rate, expected, self.output, inputs[i])

