# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:08:13 2018

@author: gah02
"""
import xlrd
import matplotlib.pyplot as plt
import os
import glob
import sys
import fnmatch
import numpy as np

os.getcwd()
os.chdir('C:\\Users\\gah02'+'\\Desktop')
os.listdir(os.getcwd())
xlrd.open_workbook('AF353_data.xlsx')
b = xlrd.open_workbook('AF353_data.xlsx') 
b.sheet_by_index(0)
b2 = b.sheet_by_index(0)
data = [[b2.cell_value(c,r) for c in range (b2.nrows)] for r in range (b2.ncols)]

temp = []
x = []
counter = 1

for rows in data :
    for e in rows :
        temp.append (counter)
        if type (e) != int and type (e) != float :
            rows.remove(e)
    x.append(temp)
    temp = []
    counter += 1
            
fig = plt.figure()
ax = plt.subplot (111)

data2 = [sum(i)/len(i) for i in data]
stdev1 = np.std(data[0])
stdev2 = np.std(data[1])
stdev_all = [stdev1,stdev2]
pos = [1,2]
pos1 = [1]
pos2 = [2]
ax.bar(pos1,data2[0],yerr=stdev1,alpha = 0.3,color='r')
ax.bar(pos2,data2[1],yerr=stdev2,alpha = 0.3,color='b')




#bp = ax.boxplot (data, whis=np.inf, widths=0.3, zorder=0)

#for box in bp ['boxes'] :
#    box.set (color='black', linewidth=1)
#    
#    bp['medians'][0].set (color='r', linewidth=2, alpha = 0.5)
#    bp['medians'][1].set (color='b', linewidth=2, alpha = 0.5)
    
for i,j in zip(x,data) :
    if i[0] == 1 :
        ax.scatter (i,j, color = 'r', alpha = 0.5)
    if i[0] == 2 :
        ax.scatter (i,j, color = 'b', alpha = 0.5)
            
ax.set_xlim (0,3)
plt.title ('Y in function of X', fontsize = 14)
plt.xlabel ('Grace', fontsize = 12)
plt.ylabel ('Bonjour', fontsize = 12)
x_labels = ['Data_1', 'Data_2']
x_positions = np.arange (1,3)
plt.xticks (x_positions, x_labels)

plt.savefig('Plot_Grace.jpg',dpi=200)
