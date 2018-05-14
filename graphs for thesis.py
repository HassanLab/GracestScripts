# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:01:46 2018

@author: gah02
"""

import os

os.chdir("C:\\Users\\gah02\\Documents\\UPMC\\Master's Thesis\\Plots")
     
file = "58062_disc_1_K21OU5.csv";

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
# create an x varibale
x = []
y = []
z = []
a = []
t = []
#for every element(e) in data (for loop)
for e in data:
    x.append(e[1]) # make an appendix for the x values
    y.append(e[2])
    z.append(e[3])
    a.append(e[10])
    t.append(e[8])
 
xmf = []
ymf = []
zmf = []
amf = []
tmf = []
    
for e in data:
    if e[2] < 500:
        if e[10] > 10:
            #if e[10] > 10:
                xmf.append(e[1]) # i
                ymf.append(e[2]) # j
                zmf.append(e[3]) # k
                amf.append(e[10])# l
                tmf.append(e[8]) # m
        
fit = np.polyfit(xmf, ymf, 10)  #10 is equal to degree of fitting 
line = np.poly1d(fit)
xp = np.linspace(0, 2044, 100)


#import itertools
#for i,j,k,l,m in itertools.product(range(xa), range(ya), range(za),range(aa), range(ta)):
#    if l > 50:
 #       xa.append(e[1]) # i
  #      ya.append(e[2]) # j
   #     za.append(e[3]) # k
    #    aa.append(e[10])# l
     #   ta.append(e[8]) # m



plt.figure(figsize=(20,10))
ax = plt.subplot(1,1,1)
#ax2 = plt.subplot(1,2,2)
#ax.scatter(x,y,alpha=0.8,s=25,c=a,cmap='Reds')
ax.scatter(x,y,alpha=1,s=35,c=t,\
norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(t),vmax=max(t)),cmap='Blues')
#ax.scatter(xmf,ymf,alpha=0.8,s=35,c=a,\
ax.scatter(xmf,ymf,alpha=1,s=20,c=amf,cmap='Reds')
#ax.scatter(x,y,alpha=0.8,s=20,c=t,cmap='Blues')
#ax.scatter(x,y,alpha=1,s=20,c=a,\
#norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(a),vmax=max(a)),cmap='Reds')
#ax.scatter(x,y,alpha=0.5,s=20,c=t,cmap='Blues')
ax.plot(xp, line(xp))  #x and y need to have same resolution

#ax2.scatter(t,a,alpha=0.3,s=35,c=t,cmap='Blues')
ax.axis('scaled')
#ax2.axis('scaled')
#ax.set_xlabel('atonal',fontsize=20)


import math
from scipy.spatial.distance import pdist, squareform

xp1 = data[:,1]
yp1 = data[:,2]
#p1 = np.c_[([xp1]),([yp1])]
p1 = np.c_[np.array(xp1),np.array(yp1)]
#p1 = data[:, 1], data[:,2]                          #[xp[0], [line(xp)][0]]
#p2 = [xp, line(xp)]
p2 = np.c_[np.array(xp),np.array(line(xp))]


distance = []
position = []


#dtype=np.int8
for e in p1:
    shortest = 50000
    place = 6
    for n,d in enumerate (p2):
        #g = squareform(pdist(p1, 'euclidean'))
        dist = math.sqrt( ((e[0]-d[0])**2)+((e[1]-d[1])**2) )
        #return ((b.X - a.X)*(c.Y - a.Y) - (b.Y - a.Y)*(c.X - a.X)) > 0
        if shortest > dist:
            shortest = dist
            place = n
    position.append(place)
    distance.append(shortest)       #same indent level as for loop
    
sign = []
for m,f,k in zip(position,p1, distance): #loop over both simultaneously 
    if m != 0 and m != 99:
        fn1 = p2[m+1] 
        fn2 = p2[m-1]
        calculation = ((fn1[0] - fn2[0])*(f[1] - fn2[1]) - (fn1[1] - fn2[1])*(f[0] - fn2[0])) 
    elif m == 0:
        fn1 = p2[m+1]
        fn2 = p2[m]
        calculation = ((fn1[0] - fn2[0])*(f[1] - fn2[1]) - (fn1[1] - fn2[1])*(f[0] - fn2[0]))
    elif m == 99:
        fn1 = p2[m]
        fn2 = p2[m-1]
        calculation = ((fn1[0] - fn2[0])*(f[1] - fn2[1]) - (fn1[1] - fn2[1])*(f[0] - fn2[0]))
    if calculation < 0:
        k = -k
        sign.append(k)
    elif calculation >= 0:
        sign.append(k)

ato = []
#thresh = 70
for e in a:
    if e > 0:
    #if e > thresh:
        #ato.append(thresh)
        ato.append(e)
    else:
        ato.append(e)


from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors 
        
plt.figure(figsize=(20,10))
distplot = plt.subplot(1,1,1)
divider = make_axes_locatable(distplot)
cax = divider.append_axes('right',size='5%',pad=0.05)
#ax2 = plt.subplot(1,2,2)
#ax.scatter(x,y,alpha=0.8,s=25,c=a,cmap='Reds')
#distplot.scatter(distance,t,alpha=1,s=35,c=t,cmap='Blues')
#distplot.scatter(distance,t,alpha=0.5,s=35,c='blue')
plot = distplot.scatter(sign,t,alpha=1,s=15,c=ato,\
norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(ato),vmax=max(ato)),cmap='Reds')
#ax.scatter(xmf,ymf,alpha=0.5,s=35,c=amf,cmap='Reds')
#ax.plot(xp, line(xp))  #x and y need to have same resolution
plt.colorbar(plot,cax=cax)   

fit2 = np.polyfit(sign, t, 16)  #10 is equal to degree of fitting 
line2 = np.poly1d(fit2)
xp5 = np.linspace(-242, 851, 100)

distplot.plot(xp5, line2(xp5))

import xlsxwriter

path = os.getcwd()
name = 'Data_Grace_'+str(file)+'.xlsx'

if name in os.listdir(path) : 
    os.remove(name)

workbook = xlsxwriter.Workbook(name)
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)

bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'X', bold)
worksheet.write('B1', 'Y', bold)

index = 2

for i,j in zip(xp5,line2(xp5)) :
    worksheet.write('A'+str(index), i)
    worksheet.write('B'+str(index), j)
    index += 1
    
workbook.close()



fig = plt.figure(figsize=(20,10))
ax = plt.axes(projection='3d')

zdata = z
xdata = x
ydata = y
ax.scatter3D(xdata, ydata, zdata, c=a, cmap='Reds',s=16);
ax.axis('scaled')





