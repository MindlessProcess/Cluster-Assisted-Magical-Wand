import sys

from neuron import Neuron
from .. import DEBUG


class SuperNeuron(object):
    """This is a class that implements an artificial neuron."""
    def __init__(self, image, image_size, color_histogram):
        self.image = image
        self.image_size = image_size
        self.color_histogram = color_histogram
        self.imploded_image = []
        self.neurons = []
        for y in range(image_size[0]):
            for x in range(image_size[1]):
                self.neurons.append(Neuron(image[y][x], y, x))
        if DEBUG:
            self._display_neurons()
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
        if DEBUG:
            self._display_neurons()
        return None

    def _boundary_in_neuron(self, neuron, boundary):
        segments = neuron.image_segments
        y = boundary['y']
        x = boundary['x']
        return (
            self._boundaries_are_neighbours(segments, y - 1, x) or
            self._boundaries_are_neighbours(segments, y, x - 1) or
            self._boundaries_are_neighbours(segments, y, x + 1) or
            self._boundaries_are_neighbours(segments, y + 1, x)
        )

    def _boundaries_are_neighbours(self, segments, y, x):
        if y < 0 or x < 0:
            return False
        return [segment for segment in segments if
                (segment['y'], segment['x']) == (y, x)] != []

    def _merge_neurons(self, neuron_into_merge, neuron_to_merge):
        if DEBUG:
            print "Merging two neurons !"
        neuron_into_merge.image_segments.extend(neuron_to_merge.image_segments)
        self.neurons.remove(neuron_to_merge)
        return None

    def _implode_neurons(self):
        for y in range(len(self.image)):
            self.imploded_image.append([])
            for x in range(len(self.image[y])):
                self.imploded_image[y].append(0)
        for neuron in self.neurons:
            for segment in neuron.image_segments:
                self.imploded_image[segment['y']][segment['x']] = segment['value']

    def _display_neurons(self):
        print 'Displaying neurons:\n'
        print 'Neurons: %d' % len(self.neurons)
        print '---'
        for neuron in self.neurons:
            print 'Neuron: %s' % neuron.image_segments

    def _display_image(self, image):
        for y in range(len(image)):
            for x in range(len(image[y])):
                sys.stdout.write('%d%s' % (
                    image[y][x],
                    ', ' if x < len(image[y]) - 1 else '\n')
                )
