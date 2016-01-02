#!/usr/bin/python

import os
import sys
import argparse

from .clustering.core import Core


def get_arguments(arguments):
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-f', '--file', help='The image file to process',
                        required=True)
    parser.add_argument('-c', '--clusters', help='Number of clusters',
                        required=True)
    arguments = vars(parser.parse_args())

    if os.path.isfile(arguments['file']) == False:
        sys.stderr.write('FileError: Given file doesn\'t not found\n')
        parser.print_help()
        sys.exit()

    if arguments['clusters'].isdigit() == False:
        sys.stderr.write('ArgumentError: Clusters must be a number\n')
        parser.print_help()
        sys.exit()

    return arguments


def main():
    arguments = get_arguments(sys.argv[1:])

    image = arguments['file']
    number_of_clusters = arguments['clusters']

    print '[image]: %s' % image
    print '[number_of_clusters]: %s' % number_of_clusters

    core = Core(number_of_clusters)
    core.run()
    core.info()

if __name__ == '__main__':
    main()
