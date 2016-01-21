from random import randint


class Neuron(object):
    """This is a class that implements an artificial neuron."""
    def __init__(self, pixel):
        self.delta = randint(0, 100)
        self.image_segments = [pixel]

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
        for segment in self.image_segments:
            if self._segment_is_boundary(segment):
                boudaries_coordinates.append(
                    {k: segment.get(k, None) for k in ('y', 'x')}
                )
        return boudaries_coordinates

    def get_color(self):
        return (
            self.image_segments[0]['value'] if
            len(self.image_segments) > 0 else None
        )

    def _coordinates_in_segments(self, y, x):
        if y < 0 or x < 0:
            return False
        return [segment for segment in self.image_segments if
                (segment['y'], segment['x']) == (y, x)] != []

    def _segment_is_boundary(self, segment):
        y = segment['y']
        x = segment['x']
        return (
            not self._coordinates_in_segments(y - 1, x) or
            not self._coordinates_in_segments(y, x - 1) or
            not self._coordinates_in_segments(y, x + 1) or
            not self._coordinates_in_segments(y + 1, x)
        )
