import sys

from neuron import Neuron
from .. import DEBUG
from ..clustering.ktools import KPos, KColor


class SuperNeuron(object):
    """This is a class that implements an artificial neuron."""
    def __init__(self, image, image_size, color_histogram):
        self.image = image
        self.image_size = image_size
        self.color_histogram = color_histogram
        self.imploded_image = []
        self.neurons = []

        for cluster in self.color_histogram:
            pixels = [(y, x) for y, row in enumerate(image) for x, column in enumerate(row) if column == cluster[0]]
            if pixels != []:
                self.neurons.append(Neuron(cluster[0], pixels))
        if DEBUG:
            print '\n-----\n'
            self.display_neurons()
            print '\n-----\n'

    def transfert(self, image):
        for neuron in self.neurons:
            neuron.activate(image)
        return None

    def learn(self, inputs, expected):
        """Applies the learning rule on each weighted connection."""
        for neuron in self.neurons:
            neuron.learn(inputs, expected)

    def merge_neighbour_neurons(self):
        for i in range(len(self.neurons)):
            if i >= len(self.neurons):
                break
            neuron = self.neurons[i]
            boundaries = neuron.get_boundaries()
            if boundaries == []:
                return None

            for other_neuron in self.neurons:
                if other_neuron == neuron:
                    continue
                for boundary in boundaries:
                    if self._boundary_in_neuron(other_neuron, boundary):
                        if neuron.get_color() == other_neuron.get_color():
                            self._merge_neurons(neuron, other_neuron)
        if DEBUG:
            print '\n-----\n'
        self._implode_neurons()
        return None

    def _find_first_element_by_value(self, value):
        for y in range(len(self.image)):
            for x in range(len(self.image[y])):
                if self.image[y][x] == value:
                    return {'y': y, 'x': x, 'value': self.image[y][x]}
        return None

    def merge_neurons(self):
        for neuron in self.neurons:
            centroid = neuron.get_initial_centroid()
            for other_neuron in self.neurons:
                if neuron == other_neuron:
                    continue
                other_centroid = other_neuron.get_initial_centroid()
                centroid_color = self.image[centroid[0]][centroid[1]]
                other_centroid_color = self.image[other_centroid[0]][other_centroid[1]]
                if centroid_color != neuron.color:
                    kcolor = KColor(centroid_color)
                    if kcolor.distance(other_centroid_color) == 1 or kcolor.distance(other_neuron.color) == 0:
                        print 'Merging neurons #%d and #%d' % (self.neurons.index(neuron), self.neurons.index(other_neuron))
                        neuron.color = neuron.color if len(neuron.pixels) > len(other_neuron.pixels) else other_neuron.color
                        neuron.pixels.extend(other_neuron.pixels)
                        self.neurons.remove(other_neuron)
                        centroid = neuron.get_initial_centroid()

    def _implode_neurons(self):
        for y in range(len(self.image)):
            self.imploded_image.append([])
            for x in range(len(self.image[y])):
                self.imploded_image[y].append(0)
        for neuron in self.neurons:
            for segment in neuron.image_segments:
                self.imploded_image[segment['y']][segment['x']] = segment['value']

    def display_neurons(self):
        print 'Neurons: %d' % len(self.neurons)
        print '---'
        for neuron in self.neurons:
            print 'Number: %d' % self.neurons.index(neuron)
            print 'Neuron.Length: %s' % len(neuron.pixels)
            print 'Neuron.Color:', neuron.color
            print 'Neuron.Centroid:', neuron.get_initial_centroid()
            print 'Neuron.Centroid.Color:', self.image[neuron.get_initial_centroid()[0]][neuron.get_initial_centroid()[1]]
            print '---'

    def _display_image(self, image):
        for y in range(len(image)):
            for x in range(len(image[y])):
                sys.stdout.write('%d%s' % (
                    image[y][x],
                    ', ' if x < len(image[y]) - 1 else '\n')
                )
