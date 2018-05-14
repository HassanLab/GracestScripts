# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:20:55 2018

@author: gah02
"""

import os

os.chdir("C:\\Users\\gah02\\Documents\\UPMC\\Master's Thesis\\Plots")
     
file = "Data_Grace_58061_disc_1_HJ4QFN.csv";
file2 = "Data_Grace_58062_disc_1_K21OU5.csv";

# import the needed libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.colors as colors 


                            
# make a workbook
workbook = pd.read_csv(file)
# make workbook into matrix, otherwise you cannot call variables
data = pd.DataFrame.as_matrix(workbook)

workbook2 = pd.read_csv(file2)
data2 = pd.DataFrame.as_matrix(workbook2)

def get_color():
    for item in ['r', 'g', 'b', 'c', 'm', 'y', 'k']:
        yield item

color = get_color()

x = []
y = []
x2 = []
y2 = []


#for every element(e) in data (for loop)
for e in data:
    x.append(e[0]) # make an appendix for the x values
    y.append(e[1])
#acolor = next(color)
    #plt.scatter(x, y, color=acolor, marker='o')
    
for e in data2:
    x2.append(e[0]) 
    y2.append(e[1])
      
plt.figure(figsize=(20,10))
distplot = plt.subplot(1,1,1)

distplot.scatter(x,y,alpha=1,s=15,c='blue')
distplot.scatter(x2,y2,alpha=1,s=15,c='red')

distplot.axis('tight')




fit = np.polyfit(x, y, 16)  #10 is equal to degree of fitting 
line = np.poly1d(fit)
xp = np.linspace(-400, 700, 100)

distplot.plot(xp, line(xp))



fit2 = np.polyfit(x2, y2, 16)  #10 is equal to degree of fitting 
line2 = np.poly1d(fit2)
xp2 = np.linspace(-242, 851, 100)

distplot.plot(xp2, line2(xp2))

fit = np.polyfit(x, y, 16)  #10 is equal to degree of fitting 
line = np.poly1d(fit)
xp = np.linspace(-400, 700, 100)

distplot.plot([0,0], [0,40])
