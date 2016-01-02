#!/usr/bin/python

import os
import sys
import logging
import argparse

from . import get_debug

DEBUG = get_debug()
LOGGER = logging.getLogger(__name__)


def get_arguments(arguments):
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-f', '--file', help='The image file to process',
                        required=True)
    parser.add_argument('-c', '--clusters', help='Number of clusters',
                        required=True)
    parser.add_argument('-d', '--debug', help='Specify debug mode (0 or 1)',
                        required=False)
    arguments = vars(parser.parse_args())

    if os.path.isfile(arguments['file']) == False:
        sys.stderr.write('FileError: Given file doesn\'t not found\n')
        parser.print_help()
        sys.exit()

    if arguments['clusters'].isdigit() == False:
        sys.stderr.write('ArgumentError: Clusters must be a number\n')
        parser.print_help()
        sys.exit()

    try:
        arguments['clusters'] = int(arguments['clusters'])
    except ValueError:
        sys.stderr.write('ArgumentError: Clusters must be a number\n')
        parser.print_help()
        sys.exit()

    if arguments['debug'] is not None:
        if arguments['debug'] not in ('0', '1'):
            parser.print_help()
            sys.exit()
        os.environ['DEBUG'] = arguments['debug']
        global DEBUG
        DEBUG = get_debug()

    return arguments


def main():
    arguments = get_arguments(sys.argv[1:])

    image = arguments['file']
    number_of_clusters = arguments['clusters']

    if DEBUG:
        LOGGER.info('image -> %s' % image)
        LOGGER.info('number_of_clusters -> %s' % number_of_clusters)

    from .core import Core
    core = Core(number_of_clusters)
    core.run()
    if DEBUG:
        core.info()

if __name__ == '__main__':
    main()
