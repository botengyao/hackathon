from Feature import fft
import pandas as pd
import os
import csv
import numpy as np


def getfile(pathname):
    path = []
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if not file.startswith('.') and os.path.isfile(os.path.join(root, file)):
                p = os.path.join(root, file)
                path.append(p)
    return path


def addlabel():
    path = getfile('./ppig')
    filename = './ppig/data.txt'
    file = open(filename, "w")
    for i in range(len(path)):
        temp = path[i].replace('/', '.').split('.')[-3]
        if(temp[-1] == "g"):
            continue
        label = temp[-1]
        print(path[i])
        features = fft(path[i]).getFFT()
        for feature in features:
            file.write(str(int(feature)))
            file.write(" ")
        file.write(label)
        file.write("\n")
    file.close()


path = getfile('./ppig/')
addlabel()
# print(path)
# a = fft("./ppig/label0/ofarm.wav")
