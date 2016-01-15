#!/usr/bin/env python

import sys
import os
import Image
import PIL
import re
from binascii import hexlify

class Processing():
    def __init__(self, filename):
        print 'Processing'
        self.main_picture = Image.open(filename)
        self.pixel_string = self.main_picture.tostring()

    def splitWithSpan(self, span):
        words = list(self.pixel_string)
        table = ["".join(words[i:i+span]) for i in range(0, len(words), span)]
        return table

    def convert_to_256(self):
        self.new_pxl_str = []
        for i in self.pixel_string:
#            print int(hexlify(i), 16)
            x = int(hexlify(i), 16)
            if x >= 0 and x < 64:
                self.new_pxl_str.append(0)
            elif x >= 64 and x < 128:
                self.new_pxl_str.append(1)
            elif x >= 128 and x < 192:
                self.new_pxl_str.append(2)
            elif x >= 192 and x < 256:
                self.new_pxl_str.append(3)
            else:
                self.new_pxl_str.append(9)

#        print self.new_pxl_str
        print len(self.new_pxl_str)

#        pixel_table = self.splitWithSpan(3)
#        table = set(pixel_table)
#        print list(table)

def main(argc, argv):
    if False == os.path.isfile(argv[1]):
        print "File [" + argv[1] + "] not found!"
        return False
    output = Processing(argv[1])
    output.convert_to_256()
    return True

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
