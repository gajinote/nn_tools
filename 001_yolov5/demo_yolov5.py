#!python3
import os
import sys
import numpy as np
import math
import time
import cv2
import torch
import argparse

fps = ""
detectfps = ""
framecount = 0
detectframecount = 0
time1 = 0
time2 = 0

LABELS = [
'aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow',
'diningtable','dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']

parser = argparse.ArgumentParser()
args = parser.parse_args()

if __name__ == '__main__':
  print(args)