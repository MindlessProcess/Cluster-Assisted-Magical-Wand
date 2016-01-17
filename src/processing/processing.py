#!/usr/bin/env python

import sys
import os
import Image
import PIL
import re

###
### Processing will handle these parsed results:
###

###  self.width, self.height

###
###  self.output: (pixelwise normalized image)
###
###  [ [ (0, 0, 0), (1, 0, 1), ..., (0, 0, 0) ],
###    [ ...                      , (0, 0, 0) ],
###    [ ...                      , (0, 0, 0) ] ]
###

###
###  self.histogram: (pixel count of the same color)
###
###       R  G  B   Pixel Count
###
###  [ [ (0, 0, 0), X ],
###    [ (0, 0, 1), X ],
###    [ (0, 0, 2), X ],
###    [ ...          ] ]
###


class Processing():
    def __init__(self, filename):
        print 'Processing...'
#        HEX_MAX = 256
        self.main_picture = Image.open(filename)
        self.pixel_string = self.main_picture.tostring()
        self.width, self.height = self.main_picture.size
        self.histogram = []
        for R in range(0, 4):
            for G in range (0, 4):
                for B in range(0, 4):
                    self.histogram.append([(R, G, B), 0])
#        print self.histogram
#        print len(self.histogram)

    def get_256(self, value):
        norm = -1
        if value >= 0 and value < 64:
            norm = 0
        elif value >= 64 and value < 128:
            norm = 1
        elif value >= 128 and value < 192:
            norm = 2
        elif value >= 192 and value < 256:
            norm = 3
        return norm

    def update_histogram(self, rgb):
        for i in self.histogram:
            if rgb == i[0]:
                i[1] += 1

    def norm_preview(self):
        # preprocess parser
        self.output = []
        line = []
        l = 0

        # display purposes
        ptr = list(self.main_picture.getdata())
        p_ls = []
        for i in ptr:
            # parser
            val = i
            pix = (self.get_256(val[1]), self.get_256(val[2]), self.get_256(val[3]))
            self.update_histogram(pix)
            line.append(pix)
            l += 1
            if l == self.width:
                self.output.append(line)
                line = []
                l = 0

            # display purposes
            ls = list(i)            
            ls[0] = (self.get_256(ls[0]) + 1) * 64 - 1
            ls[1] = (self.get_256(ls[1]) + 1) * 64 - 1
            ls[2] = (self.get_256(ls[2]) + 1) * 64 - 1
            ls[3] = (self.get_256(ls[3]) + 1) * 64 - 1
            p_ls.append(tuple(ls))

# histogram debug material
#        print self.histogram
#        print len(self.histogram)
#        res = 0
#        for i in self.histogram:
#            res += i[1]
#        print res
#        print self.width * self.height

#display purposes
#        self.display = Image.new("RGB", self.main_picture.size)
#        self.display.putdata(p_ls)
#
#        self.display.show()
#        self.main_picture.show()
        
### TO BE COMMENTED LATER

def main(argv):
    if False == os.path.isfile(argv[1]):
        print "File [" + argv[1] + "] not found!"
        return False
    output = Processing(argv[1])
    output.norm_preview()
    return True

if __name__ == "__main__":
    main(sys.argv)


####
####   ANYTHING BELOW THIS IS DEPRECATED OR TOO OLD...
####

#    def convert_to_256(self):
#        self.pxl_tab = []
#        tmp = []
#        line = []
#        l = 0
#        k = 0
#        for i in self.pixel_string:
#            tmp.append(self.get_256(int(hexlify(i), 16)))
#            k += 1
#            if k == 3:
#                k = 0
#                tmp = ["".join(tmp)]
#                line.append(tmp)
#                tmp = []
#            l += 1
#            if l == self.width:
#                self.pxl_tab.append(line)
#                line = []
#                l = 0
#        print self.pxl_tab
#        print len(self.new_pxl_str)
#        pixel_table = self.splitWithSpan(self.new_pxl_str, 3)
#        table = set(pixel_table)
#        print list(table)

#    def splitWithSpan(self, ptr, span):
#        words = list(ptr)
#        table = [", ".join(words[i:i+span]) for i in range(0, len(words), span)]
#        return table
