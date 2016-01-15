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
        self.width, self.height = self.main_picture.size

    def splitWithSpan(self, ptr, span):
        words = list(ptr)
        table = [", ".join(words[i:i+span]) for i in range(0, len(words), span)]
        return table

    def get_256(self, value):
        norm = ""
        if value >= 0 and value < 64:
            norm = "0"
        elif value >= 64 and value < 128:
            norm = "1"
        elif value >= 128 and value < 192:
            norm = "2"
        elif value >= 192 and value < 256:
            norm = "3"
        return norm

    def norm_preview(self):
        self.pxl_str = []
        ptr = list(self.main_picture.getdata())
        for i in ptr:
            old = i
            ls = list(i)
            ls[0] = (int(self.get_256(ls[0])) + 1) * 64 - 1
            ls[1] = (int(self.get_256(ls[1])) + 1) * 64 - 1
            ls[2] = (int(self.get_256(ls[2])) + 1) * 64 - 1
            ls[3] = (int(self.get_256(ls[3])) + 1) * 64 - 1
            i = tuple(ls)
            print "Old:"
            print old
            print "New:"
            print i
            print
        self.display = Image.new("RGB", self.main_picture.size)
        self.display.putdata(ptr)
        self.display.show()
        self.main_picture.show()
        

    def convert_to_256(self):
        self.pxl_tab = []
        tmp = []
        line = []
        l = 0
        k = 0
        for i in self.pixel_string:
            tmp.append(self.get_256(int(hexlify(i), 16)))
            k += 1
            if k == 3:
                k = 0
                tmp = ["".join(tmp)]
                line.append(tmp)
                tmp = []
            l += 1
            if l == self.width:
                self.pxl_tab.append(line)
                line = []
                l = 0
            

        print self.pxl_tab
#        print len(self.new_pxl_str)

#        pixel_table = self.splitWithSpan(self.new_pxl_str, 3)
#        table = set(pixel_table)
#        print list(table)

def main(argc, argv):
    if False == os.path.isfile(argv[1]):
        print "File [" + argv[1] + "] not found!"
        return False
    output = Processing(argv[1])
    output.norm_preview()
#    output.convert_to_256()
    return True

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
