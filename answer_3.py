# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FsWMvfUh4d3MuzeI4J0-Gg39NrYyl1Pq
"""

import os

Lines = []
path = 'folder/'
fileList = os.listdir(path)
for file in fileList:
   file = open(os.path.join('folder/'+ i), 'r')
   Lines.append(file.read())

print(Lines)