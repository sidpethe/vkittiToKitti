#!/usr/bin/python

import os
import glob
import numpy as np
import labels
import cv2
import PIL.Image as Image

i=glob.glob('*.txt')
labeldict=dict()
for textfilename in i:
    print("Running File %s :\n"%textfilename)
    splitname=textfilename.split("_")
    relpath=os.path.join(splitname[0],splitname[1])
    f=open(textfilename,'r+')
    linenum=0
    for line in f:
        if not linenum:
            linenum+=1
            continue
        linesplit=line.split(" ")
        k=linesplit[0].split(":")
        if len(k)>1:
            classname=k[0]
            tid=int(k[1])
        else:
            classname=k[0]
            tid=0
        # Store the rgb of every class, instance as mentioned in txt file into dict. l[3],l[2],l[1] for BGR -> RGB
        rgb=(int(linesplit[3]),int(linesplit[2]),int(linesplit[1]))
        classname=classname.lower()
        #Recording changes in names of classes in changes(eg. tree is vegetation)
        #NOTE: Changed all labels in labels.py to remove spaces. Eg. traffic sign -> trafficsign
        changes={'tree':'vegetation','misc':'unlabeled','van':'car'}
        #Change classname if part of changes, default: keep same classname
        classname=changes.get(classname,classname)
        labelid=labels.name2label[classname].id
        labeldict[rgb]=((labelid*256)+tid)
    f.close()
    files=glob.glob(relpath+'/*.png')
    for filename in files:
        print("Running File %s\n"%filename)
        im=cv2.imread(filename)
        im2=np.zeros(im.shape[:-1])
        for i in range(im.shape[0]):
            for j in range(im.shape[1]):
                #read the rgb value for each pixel
                #create new file with labeldict[rgb] value as pixel
                im2[i,j]=labeldict[(im[i,j,0],im[i,j,1],im[i,j,2])]
        im2=np.array(im2,dtype=np.int16)
        savepath=os.path.join('converted',filename)
        print(savepath)
        if not os.path.exists(savepath[:-9]):
            os.makedirs(savepath[:-9])
        im2=Image.fromarray(im2)
        im2.save(savepath,'PNG')
        
    
        
