import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import cv2
import os
import glob
import os.path
#from pywinauto.findwindows import find_window
#from pywinauto.win32functions import SetForgroundWindow

#First create a folder named "undecied" in the destination folder
originalfolder = "/home/rk/Amy/aerial/aerialImg/"
#originalfolder = "/home/rk/Amy/aerial/aerialDB/water/"
destinationfolder = "/home/rk/Amy/aerial/aerialDB/"

while len(glob.glob(originalfolder + "*")) != 0:
    print str(len(glob.glob(originalfolder + "*"))) + " picture left."
    categories=[]
    for i in range(len(glob.glob(destinationfolder+"*"))):
        categories.append(os.path.basename(sorted(glob.glob(destinationfolder+"*"))[i]))
    #print categories
    listCategories = list(range(len(categories)))
    # draw the picture out
    filename = os.path.basename(sorted(glob.glob(originalfolder + "*"))[0])
    print "Filename:"+filename
    print "<Hit Enter To Close>"
    img = cv2.imread(originalfolder + filename)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image',1600,1200)
    cv2.imshow('image',img) 
    cv2.waitKey(1000)
    cv2.destroyWindow('image')
    """
    img = mpimg.imread(originalfolder + filename)
    imgplot = plt.imshow(img)
    plt.axis("off")
    # wait for hit keyboard to close the picture
    plt.draw()
    plt.pause(1)
    plt.waitforbuttonpress(0)
    currentfig = plt.gcf()
    plt.close(currentfig)
    """
    # print the categories
    print "q!: Exit programme.\n"
    print "dd: Delete this picture.\n"
    for i in range(len(categories)):
	    print str(i) + ":" + categories[i]# + "\n"
	# select and put the pic to the destination folder
    try:
        mode = raw_input('Select folder:')
        if mode=="q!":
            exit(0)
        elif mode=="dd":
            os.remove(originalfolder + filename)
            print "Have deleted the file " + "\"" + filename + "\""
            print "---------------------------"
            continue
        mode = int(mode)
        if mode>=len(categories):
            print "Number entered is wrong!"
            continue
        dir = destinationfolder + categories[mode] + '/'
        if os.path.isfile(dir + filename):
            temp = 1
            while os.path.isfile(dir + filename + "_" + str(temp)):
                temp = temp + 1
            os.rename(originalfolder + filename, dir + filename + "_" + str(temp))
        else:
            os.rename(originalfolder + filename, dir + filename)
        print "Have moved the file " + "\"" + filename + "\"" + " to " + "\"" + dir + "\""
    except ValueError:
        print "Input is not a number!"
    print "---------------------------"

print "The fold is empty!"


