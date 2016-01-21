from random import randint


class Neuron(object):
    """This is a class that implements an artificial neuron."""
    def __init__(self, color, pixels):
        """
        color: tuple (R, G, B)
        pixels: list of tuples [(y, x), ...]
        """
        self.delta = randint(0, 100)
        self.color = color
        self.pixels = pixels

    def activate(self, inputs):
        """Activates the artificial neuron."""
        if inputs is None:
            raise TypeError
        return None

    def learn(self, inputs, expected):
        """Applies the learning rule on each weighted connection."""
        if inputs is None or expected is None:
            raise TypeError
        self.delta = randint(0, 100)

    def get_boundaries(self):
        boudaries_coordinates = []
        for segment in self.pixels:
            if self._segment_is_boundary(segment):
                boudaries_coordinates.append(
                    {k: segment.get(k, None) for k in ('y', 'x')}
                )
        return boudaries_coordinates

    def get_color(self):
        return self.color

    def get_initial_centroid(self):
        y = sum(pixel[0] for pixel in self.pixels)
        x = sum(pixel[1] for pixel in self.pixels)
        return (y / len(self.pixels), x / len(self.pixels))

    def _coordinates_in_segments(self, y, x):
        if y < 0 or x < 0:
            return False
        return [segment for segment in self.pixels if
                (segment[0], segment[1]) == (y, x)] != []

    def _segment_is_boundary(self, segment):
        y = segment['y']
        x = segment['x']
        return (
            not self._coordinates_in_segments(y - 1, x) or
            not self._coordinates_in_segments(y, x - 1) or
            not self._coordinates_in_segments(y, x + 1) or
            not self._coordinates_in_segments(y + 1, x)
        )
