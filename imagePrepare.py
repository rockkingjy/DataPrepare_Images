import cv2
import os
import glob
import os.path


originalfolder = "/home/rk/Amy/aerial/aerialImg/"
destinationfolder1 = "/home/rk/Amy/aerial/aerialImgnondeleted1/"
destinationfolder2 = "/home/rk/Amy/aerial/aerialImgnondeleted2/"
destinationfolder3 = "/home/rk/Amy/aerial/aerialImgnondeleted3/"
destinationfolder4 = "/home/rk/Amy/aerial/aerialImgnondeleted4/"

length = len(glob.glob(originalfolder + "*"))
print length
if length != 0:
    for i in range(10000):
        filename = os.path.basename(sorted(glob.glob(originalfolder+"*"))[0])
        os.rename(originalfolder + filename, destinationfolder1 + str(i+4353) + ".jpg")
        print i
    for i in range(10000):
        filename = os.path.basename(sorted(glob.glob(originalfolder+"*"))[0])
        os.rename(originalfolder + filename, destinationfolder2 + str(i+14353) + ".jpg")
        print i
    for i in range(10000):
        filename = os.path.basename(sorted(glob.glob(originalfolder+"*"))[0])
        os.rename(originalfolder + filename, destinationfolder3 + str(i+24353) + ".jpg")
        print i
    for i in range(length-30000):
        filename = os.path.basename(sorted(glob.glob(originalfolder+"*"))[0])
        os.rename(originalfolder + filename, destinationfolder4 + str(i+34353) + ".jpg")
        print i
    print "Move finished."


