import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import cv2
import os
import glob
import os.path


originalfolder = "/home/rk/Amy/aerial/aerialImg/"
destinationfolder = "/home/rk/Amy/aerial/temp/"

length = len(glob.glob(originalfolder + "*"))
if length != 0:
    print str(length) + " picture left."
    for i in range(2000):
        filename = os.path.basename(sorted(glob.glob(originalfolder+"*"))[0])
        os.rename(originalfolder + filename, destinationfolder + filename)
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
