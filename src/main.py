#!/usr/bin/python

import os
import sys
from .clustering.core import Core


def get_arguments(arguments):
    error = None
    print arguments
    if not arguments or \
       len(arguments) != 2 or \
       os.path.isfile(arguments[0]) == False or \
       arguments[1].isdigit() == False:
        error = 'Usage: %s [FILE] [NUMBER_OF_CLUSTERS]' % sys.argv[0]

    return arguments, error


def main():
    arguments, error = get_arguments(sys.argv[1:])
    if error is not None:
        print error
        return False

    image = arguments[0]
    number_of_clusters = arguments[1]

    print '[image]: %s' % image
    print '[number_of_clusters]: %s' % number_of_clusters

    core = Core(number_of_clusters)
    core.run()
    core.info()

if __name__ == '__main__':
    main()
