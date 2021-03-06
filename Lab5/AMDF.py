# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:07:50 2017

@author: Lulu
"""
#獨奏音樂之音高偵測(AMDF與Auto-correlation方法)。準備不同獨奏音樂一分鐘音檔兩個。
#AMDF : Average Magnitude Difference Function
#ACF : Auto-Correlation Function
#use python3

def auto_correlation():
    pass


import numpy as np
import pylab as P
import math as m
import scipy.io.wavfile
from scipy.ndimage.interpolation import shift

FSample, samples = scipy.io.wavfile.read("01-1.wav")
samples = samples.astype(int)
length = (len(samples))

framesize = 1024
frameNum = m.floor(length/framesize)
startFrame = 0
#frameNum = 1

index = 0
Frame = np.zeros(framesize,dtype=np.int32)
ShiftFrame = np.zeros(framesize,dtype=np.int32)
amdf = np.zeros(framesize,dtype=np.int32)
amdfFinal = np.zeros(frameNum,dtype=np.int32)

index = 0
i = 0
j = 0

#average movingdifference function
from scipy.signal import argrelextrema
radius = 2

for index in range(0,frameNum,1):
    Frame = samples[(startFrame+index)*framesize:(startFrame+index+1)*framesize]
    #Frame = samples[48000:48000+framesize]
    ShiftFrame = Frame
    amdf = np.zeros(framesize,dtype=np.int32)
    for i in range(0,framesize,1):
        ShiftFrame = shift(Frame, i, cval=0)
        for j in range(i,framesize,1):
            amdf[i] = amdf[i] + abs(Frame[j] - ShiftFrame[j])
    amdf[0:5] = 1000000
    amdf[framesize-50:framesize] = 1000000
    amdfFinal[index] = np.argmin(amdf)
    amdf_locMin = argrelextrema(amdf, np.less, order=radius)
        

print(amdf_locMin)
print(amdfFinal)

time = np.zeros(framesize,dtype=np.int16)
for a in range(0,framesize,1):
    time[a] = a

P.plot(time,amdf)
P.xlabel('time (s)')
P.ylabel('amdf')