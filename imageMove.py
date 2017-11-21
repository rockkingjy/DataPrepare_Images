import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import cv2
import os
import glob
import os.path


originalfolder = "/home/rk/Amy/aerial/aerialImgnondeleted4/"
destinationfolder = "/home/rk/Amy/aerial/aerialImgnondeleted4_back/"
ori = "/home/rk/Amy/aerial/aerialImgnondeleted4.txt"

with open(ori,'rU') as f:
    lines = f.readlines()
    length = len(lines)
    print length
if not os.path.exists(destinationfolder):
    os.makedirs(destinationfolder)

for i in range(length):
    filename = lines[i]
    print i, filename
    os.rename(originalfolder + filename.rstrip(), destinationfolder + filename.rstrip())
print "Move finished."

"""
originalfolder = "/home/rk/Amy/aerial/temp/"
destinationfolder = "/home/rk/Amy/aerial/arialImgdeleted/"

length = len(glob.glob(originalfolder + "*"))
if length != 0:
    print str(length) + " picture left."
    for i in range(length):
        print i
        filename = os.path.basename(sorted(glob.glob(originalfolder+"*"))[0])
        os.rename(originalfolder + filename, destinationfolder + filename)
    print "Move finished."
"""
