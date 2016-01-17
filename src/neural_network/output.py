import sys

ascii_start = '!'
ascii_end = '~'
alpha_array = []

# visible character starts from '!' and ends with '~'
for i in range(ord(ascii_start), ord(ascii_end) + 1):
    alpha_array.append(chr(i))


class Output(object):
    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_valid(output):
        if type(output) != Output:
            raise ValueError('output is not a valid Output object.')
        return True

    def is_char(self):
        return self.value > ascii_start and self.value < ascii_end

    def get_index(self):
        return alpha_array.index(self.value) if self.is_char() else -1

    def get_print(self):
        index = self.get_index()
        return alpha_array[index]


class NeuronOutput(Output):
    def __init__(self, values):
        self.horizontal_lines = values[0] or 0
        self.vertical_lines = values[1] or 0
        self.left_diagonal_lines = values[2] or 0
        self.right_diagonal_lines = values[3] or 0

        self.horizontal_lines_length = values[4] or 0
        self.vertical_lines_length = values[5] or 0
        self.left_diagonal_lines_length = values[6] or 0
        self.right_diagonal_lines_length = values[7] or 0

    def is_valid(self):
        return self.horizontal_lines != 0 or self.vertical_lines != 0 or self.left_diagonal_lines != 0 or self.right_diagonal_lines != 0

    def output(self):
        print ('[horizontal_lines]: %s' % self.horizontal_lines)
        print ('[vertical_lines]: %s' % self.vertical_lines)
        print ('[left_diagonal_lines]: %s' % self.left_diagonal_lines)
        print ('[right_diagonal_lines]: %s' % self.right_diagonal_lines)
        print ('[horizontal_lines_length]: %s' % self.horizontal_lines_length)
        print ('[vertical_lines_length]: %s' % self.vertical_lines_length)
        print ('[left_diagonal_lines_length]: %s' % self.left_diagonal_lines_length)
        print ('[right_diagonal_lines_length]: %s' % self.right_diagonal_lines_length)

class SuperNeuronOutput(Output):
    def __init__(self, char):
        super(self.__class__, self).__init__(char)
        self.outputs = []
        self.horizontal_lines = 0
        self.vertical_lines = 0
        self.left_diagonal_lines = 0
        self.right_diagonal_lines = 0
        self.horizontal_lines_length = 0
        self.vertical_lines_length = 0
        self.left_diagonal_lines_length = 0
        self.right_diagonal_lines_length = 0
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def is_char(self):
        return self.value > ascii_start and self.value < ascii_end

    def get_index(self):
        return alpha_array.index(self.value) if self.is_char() else -1

    def get_print(self):
        index = self.get_index()
        return alpha_array[index]

    def print_alpha(self):
        for i in alpha_array:
            sys.stdout.write(i)
        sys.stdout.write('\n')

    def add_output(self, output):
        if type(output).__name__ != 'NeuronOutput':
            raise ValueError('output is not a valid NeuronOutput object.')
        self.outputs.append(output)
        self.horizontal_lines += output.horizontal_lines
        self.vertical_lines += output.vertical_lines
        self.left_diagonal_lines += output.left_diagonal_lines
        self.right_diagonal_lines += output.right_diagonal_lines
        self.horizontal_lines_length += output.horizontal_lines_length
        self.vertical_lines_length += output.vertical_lines_length
        self.left_diagonal_lines_length += output.left_diagonal_lines_length
        self.right_diagonal_lines_length += output.right_diagonal_lines_length

    def print_output(self):
        print ('[horizontal_lines]: %d' % self.horizontal_lines)
        print ('[vertical_lines]: %d' % self.vertical_lines)
        print ('[left_diagonal_lines]: %d' % self.left_diagonal_lines)
        print ('[right_diagonal_lines]: %d' % self.right_diagonal_lines)
        print ('[horizontal_lines_length]: %d' % self.horizontal_lines_length)
        print ('[vertical_lines_length]: %d' % self.vertical_lines_length)
        print ('[left_diagonal_lines_length]: %d' % self.left_diagonal_lines_length)
        print ('[right_diagonal_lines_length]: %d' % self.right_diagonal_lines_length)

    def is_valid(self):
        return self.horizontal_lines != 0 or self.vertical_lines != 0 or self.left_diagonal_lines != 0 or self.right_diagonal_lines != 0

#    def is_valid(self, output):
#        if type(output) != type(self):
#            raise ValueError('output is not a valid Output object.')
#        return output.is_char()

    def _get_surrounding_segments(self, segment):
        y = segment.y
        x = segment.x
        raise NotImplementedError()

    def _get_surrounding_segment(self, y, x, direction):
        raise NotImplementedError()
