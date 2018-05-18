# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:17:30 2018

@author: gah02
"""

import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.colors as colors
import matplotlib 

os.chdir("C:\\Users\\gah02\\Documents\\UPMC\\Master's Thesis\\Plots")

filenames = os.listdir("C:\\Users\\gah02\\Documents\\UPMC\\Master's Thesis\\Plots") 


#Make the entire folder of files into a dictionary
dictionary = {}
for file in filenames:
    array_loaded = np.load(file)
    dictionary[file] = array_loaded

#print using a key from the dictionary
dictionary["LINE58067_disc_2_DWYW27.csv.npy"]



# Create figure 
fig=plt.figure()
fig.show()
ax=fig.add_subplot(111)
ax.plot(dictionary["LINE58067_disc_2_DWYW27.csv.npy"][0], dictionary["LINE58067_disc_2_DWYW27.csv.npy"][1])

