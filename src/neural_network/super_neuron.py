import sys
from random import randint
from collections import namedtuple

from base_neuron import BaseNeuron
from neuron import Neuron


def normalize_nb_lines(nb_lines):
    return 1.0 - ((float(nb_lines) / 10.0) * 2.0)


def normalize_line_length(nb_pixel, nb_pix_zone):
    return float(nb_pixel) / float(nb_pix_zone)


def roundup_div(n, d):
    return (n + d / 2) / d


class SuperNeuron(BaseNeuron):
    """This is a class that implements an artificial neuron."""
    def __init__(self, image, image_size, color_histogram):
        super(self.__class__, self).__init__()
        self.FeatureSimilarity = namedtuple('FeatureSimilarity', 'percentage name value')
        self.Feature = namedtuple('Feature', 'num_h_lines num_v_lines num_rd_lines num_ld_lines')
        self.segments_number = 4
        self.outputs = []
        self.neurons = []
        self.output = SuperNeuronOutput('')
        self.features_data = {}
        for i in range(self.segments_number):
            self.weights.append((Weight(weight_range), False))
            self.neurons.append(Neuron(weight_range))

    def transfert(self, image):
        segments = []
        image_y, image_x = self._get_image_dimensions(image)

        if VERBOSE:
            print ('[self.segments_number]: %d' % self.segments_number)
            print ('[image_y/image_x]: [%d/%d]' % (image_y, image_x))

        if image_y * image_x >= self.segments_number:
            num_rows = num_columns = 8
            segment_height, segment_width = self._get_segment_dimensions(image_y, image_x, num_rows, num_columns)
            rows_size = num_rows * segment_height
            columns_size = num_columns * segment_width

            if VERBOSE:
                print ('[segment_height/segment_width]: [%d/%d]' % (segment_height, segment_width))
                print ('[num_rows/num_columns]: [%d/%d]' % (num_rows, num_columns))
                print ('[rows_size/columns_size]: [%d/%d]' % (rows_size, columns_size))

            Segment = namedtuple('Segment', 'y x data')
            segment_row = 0
            segment_column = 0
            for i in range(1, self.segments_number + 1):
                segment_row = (i - 1) / num_columns
                segment_column = (i - 1) % num_columns
                segments.append(Segment(segment_row, segment_column, []))
                row_min_range = self._get_segment_first_range(segment_height, segment_row)
                row_max_range = (
                    image_y if segment_row == num_rows
                    else self._get_segment_last_range(segment_height, segment_row, image_y))
                column_min_range = self._get_segment_first_range(segment_width, segment_column)
                column_max_range = (
                    image_x if segment_column == num_columns
                    else self._get_segment_last_range(segment_width, segment_column, image_x))

                y = 0
                for row in range(row_min_range, row_max_range):
                    segments[i - 1].data.append([])
                    x = 0
                    for column in range(column_min_range, column_max_range):
                        segments[i - 1].data[y].append(image[row][column])
                        x += 1
                    y += 1
            if VERBOSE:
                self._display_segments(segments)
        else:
            print 'Cannot get an even size for each segment.'

        return segments

    def transfert_bis(self, image):
        """
        Return a structure with informations about the next
        zone on wich we need to make data treatment
        """
        self.zone_li = list()
        self.main_image = image
        self.zone_size_x = roundup_div(self.main_image.shape[0], self.segments_number / 2)
        self.zone_size_y = roundup_div(self.main_image.shape[1], self.segments_number / 2)
        img_shape = self.main_image.shape
        segments = []
        for cur_y in xrange(0, img_shape[0], self.zone_size_y):
            for cur_x in xrange(0, img_shape[1], self.zone_size_x):
                height_mat = cur_y + self.zone_size_y
                width_mat = cur_x + self.zone_size_x
                extracted_matrix = self.main_image[cur_y: height_mat,
                                                   cur_x: width_mat]
                segments.append(extracted_matrix)
        return segments

    def activate(self, inputs):
        """Activate the artificial neuron."""
        neurons = []
        outputs = []
        segments = self.transfert_bis(inputs)
        for i in range(len(self.neurons)):
            outputs.append(self.neurons[i].activate(segments[i]))
            outputs[i].output()
        self._process_outputs(outputs)

        self.features_data = {
            'a': [
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ],
            'b': [
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ],
            'c': [
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ],
            'd': [
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                self.Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ]
        }

        feature_set = self._find_most_similar_feature_set()
        print type(feature_set)
        print type(feature_set.value)
        if feature_set is not None:
            print '[feature_set.percentage]: %s' % feature_set.percentage
            print '[feature_set.name]: %s' % feature_set.name
            if feature_set.value is not None:
                print '[feature_set.num_h_lines]: %s' % feature_set.value.num_h_lines
                print '[feature_set.num_v_lines]: %s' % feature_set.value.num_v_lines
                print '[feature_set.num_rd_lines]: %s' % feature_set.value.num_rd_lines
                print '[feature_set.num_ld_lines]: %s' % feature_set.value.num_ld_lines
        return feature_set.name

    def train(self):
        self.features_set[feature_name].append(self.output)

    def get_output(self):
        """Returns the processed output to be checked by the Supervisor."""
        output = _find_most_similar_feature_set()
        return self._process_outputs(outputs)

    def learn(self, inputs, expected):
        """Apply the learning rule on each weighted connection."""
        """Don't forget the bias !"""
        for i in range(self.segments_number):
            self.neurons[i].learn(inputs, expected)

    def _get_difference_percentage(self, src, dst):
        return 0 if src == 0 and dst == 0 else ((max(src, dst) - min(src, dst)) * 100) / max(src, dst)

    def _get_feature_set_similarity(self, feature_set, output):
        if feature_set == None or output == None:
            return 0

        src_h_lines = feature_set.num_h_lines
        dst_h_lines = output.horizontal_lines
        src_v_lines = feature_set.num_v_lines
        dst_v_lines = output.vertical_lines
        src_rd_lines = feature_set.num_rd_lines
        dst_rd_lines = output.right_diagonal_lines
        src_ld_lines = feature_set.num_ld_lines
        dst_ld_lines = output.left_diagonal_lines

        hr_lines_percentage = self._get_difference_percentage(src_h_lines, dst_h_lines)
        vr_lines_percentage = self._get_difference_percentage(src_v_lines, dst_v_lines)
        rd_lines_percentage = self._get_difference_percentage(src_rd_lines, dst_rd_lines)
        ld_lines_percentage = self._get_difference_percentage(src_ld_lines, dst_ld_lines)

        difference_percentage = (hr_lines_percentage
                + vr_lines_percentage
                + rd_lines_percentage
                + ld_lines_percentage) / 4

        return 100 - difference_percentage

    def test(self):
        Feature = namedtuple('Feature', 'num_h_lines num_v_lines num_rd_lines num_ld_lines')
        src_feature = Feature(1, 2, 3, 4)
        dst_feature = Feature(4, 3, 2, 1)
        similarity_percentage = self._get_feature_set_similarity(src_feature, dst_feature)
        print '[SIMILARITY PERCENTAGE]: %d' % similarity_percentage
        return similarity_percentage

    def test_find_most_similar_feature_set(self):
        self.features_data = {
            'a': [
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ],
            'b': [
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ],
            'c': [
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ],
            'd': [
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)),
                Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
            ]
        }

        self.output = Feature(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

        feature_set = self._find_most_similar_feature_set()
        print '[feature_set.percentage]: %s' % feature_set.percentage
        print '[feature_set.name]: %s' % feature_set.name
        print '[feature_set.num_h_lines]: %s' % feature_set.value.num_h_lines
        print '[feature_set.num_v_lines]: %s' % feature_set.value.num_v_lines
        print '[feature_set.num_rd_lines]: %s' % feature_set.value.num_rd_lines
        print '[feature_set.num_ld_lines]: %s' % feature_set.value.num_ld_lines

    def _find_most_similar_feature_set(self):
        most_similar_feature_set = self.FeatureSimilarity(0, None, None)
        for key, value in self.features_data.iteritems():
            for feature_set in value:
                similarity_percentage = self._get_feature_set_similarity(feature_set, self.output)
                if similarity_percentage > most_similar_feature_set.percentage:
                    most_similar_feature_set = self.FeatureSimilarity(similarity_percentage, key, feature_set)
        return most_similar_feature_set

    def _process_outputs(self, outputs):
        for i in range(len(outputs)):
            if outputs[i].is_valid():
                self.output.add_output(outputs[i])
        self.output.print_output()
        return self.output

    def _get_segment_first_range(self, segment_dimension, segment_cell):
        return segment_dimension * segment_cell

    def _get_segment_last_range(self, segment_dimension, segment_cell, image_dimension):
        return segment_dimension * (segment_cell + 1) if segment_dimension * (segment_cell + 1) <= image_dimension - 1 else image_dimension - 1

    def _get_image_dimensions(self, image):
        """Returns the image dimensions as a tuple."""
        return (len(image), len(image[0]) if len(image) > 0 else 0)

    def _get_segment_dimensions(self, y, x, num_rows, num_columns):
        """Returns an image segment dimensions as a tuple."""
        return (int(round(y / num_rows)), int(round(x / num_columns)))

    def _remove_empty_segments(self, segments):
        i = 0
        while i < len(segments):
            if len(segments[i].data) == 0:
                segments.pop(i)
            else:
                i += 1
        self.segments_number = len(segments)
        return segments

    def _display_segments(self, segments):
        print('')
        for i in range(len(segments)):
            print('====SEGMENT #%d [%d, %d]====' % (i + 1, segments[i].y, segments[i].x))
            for y in range(len(segments[i].data)):
                for x in range(len(segments[i].data[y])):
                    sys.stdout.write('%d, ' % segments[i].data[y][x])
                print('')
            print('')
