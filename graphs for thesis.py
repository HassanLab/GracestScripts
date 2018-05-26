# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:01:46 2018

@author: gah02
"""

import os

os.chdir("C:\\Users\\gah02\\Documents\\new segmented files\\csv files")
 
   

file = "58060_disc_4_9OW3HM.csv";

# import the needed libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.colors as colors 
import math
import statistics
from math import pi
from uncertainties import ufloat
                            
# make a workbook
workbook = pd.read_csv(file)
# make workbook into matrix, otherwise you cannot call variables
data = pd.DataFrame.as_matrix(workbook)

# create varibales for the values and coordinates
x = []
y = []
z = []
a = []
t = []
v = []
#for every element(e) in data (for loop)
for e in data:
    if e[4] > 3000:
        if e[4] < 18783:
            x.append(e[1]) # make an appendix for the values
            y.append(e[2])
            z.append(e[3])
            a.append(e[10])
            t.append(e[8])
            v.append(e[4])
 
      
#calculate the average diameter of nuclei in the sample
vA = np.mean(v)
r3 = vA/(pi*(4/3))
radius = r3 ** (1. / 3)
diameter = radius * 2




#Use these variables for the MF detection and generation of the line fitting the MF
xmf = []
ymf = []
zmf = []
amf = []
tmf = []
vmf = []                     
for e in data:
    if e[4] > 3000:
        if e[4] < 18783:
            if e[2] < 600:
                if e[10] > 18:
                    #if e[10] < 26:
                        xmf.append(e[1]/diameter) 
                        ymf.append(e[2]/diameter) 
                        zmf.append(e[3]/diameter) 
                        amf.append(e[10]/diameter)
                        tmf.append(e[8]/diameter) 
                        vmf.append(e[4]/diameter)
                        

xA = []
yA = []
zA = []
aA = []
tA = []

#for every element(e) in data (for loop)
for e in data:
    if e[4] > 3000:
        if e[4] < 18783:
            
            xA.append(e[1]/diameter) 
            yA.append(e[2]/diameter)
            zA.append(e[3]/diameter)
            aA.append(e[10]/diameter)
            tA.append(e[8]/diameter)
         
     
        


maxX = math.ceil(max(xmf))
minX = math.floor(min(xmf))
fit = np.polyfit(xmf, ymf, 6)  #the last number is equal to degree of fitting, usually use 6 
line = np.poly1d(fit)
xp = np.linspace(int(minX),int(maxX), 200)



plt.figure(figsize=(20,10))
ax = plt.subplot(1,1,1)

#Finding the MF (after you find the MF and detect the line, then comment out the next 3 lines)
#ax.scatter(xmf,ymf,alpha=1,s=30,c=amf,\
#norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(amf),vmax=max(amf)),cmap='Reds')

#ax.plot(xp, line(xp))

#ax.axis('scaled')

#ax.scatter(xA,yA,alpha=1,s=30,c=aA,\
#norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(aA),vmax=max(aA)),cmap='Reds')
#ax.axis('scaled')
#ax2 = plt.subplot(1,2,2)
#ax.scatter(x,y,alpha=0.8,s=25,c=a,cmap='Reds')
ax.scatter(xA,yA,alpha=1,s=30,c=tA,\
norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(tA),vmax=max(tA)),cmap='Blues')
#ax.scatter(xmf,ymf,alpha=0.8,s=35,c=a,\
#ax.scatter(xmf,ymf,alpha=1,s=20,c=amf,cmap='Reds')
#ax.scatter(x,y,alpha=0.8,s=20,c=t,cmap='Blues')
ax.scatter(xmf,ymf,alpha=0.6,s=30,c=amf,\
norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(amf),vmax=max(amf)),cmap='Reds')
#ax.scatter(x,y,alpha=0.5,s=20,c=t,cmap='Blues')
ax.plot(xp, line(xp))  #x and y need to have same resolution

#ax2.scatter(t,a,alpha=0.3,s=35,c=t,cmap='Blues')
ax.axis('scaled')
#ax2.axis('scaled')
#ax.set_xlabel('atonal',fontsize=20)

MF = (xp, line(xp))
MFx = MF[0] * diameter 
MFy = MF[1] * diameter   


          
          

import math
from scipy.spatial.distance import pdist, squareform



for e in data:
    if e[4] > 3000:
        if e[4] < 18783:
               xp1 = np.asarray(xA)
               yp1 = np.asarray(yA)
                
               p1 = np.c_[np.array(xp1),np.array(yp1)]
                
               p2 = np.c_[np.array(xp),np.array(line(xp))]
            
    
  
    

distance = []
position = []


for e in p1:
    shortest = 50000
    place = 6
    for n,d in enumerate (p2):
        
        dist = math.sqrt( ((e[0]-d[0])**2)+((e[1]-d[1])**2) )
        
        if shortest > dist:
            shortest = dist
            place = n
    position.append(place)
    distance.append(shortest)       #same indent level as for loop




sign = []
for m,f,k in zip(position,p1, distance): #loop over both simultaneously 
    if m != 0 and m != 199:
        fn1 = p2[m+1] 
        fn2 = p2[m-1]
        calculation = ((fn1[0] - fn2[0])*(f[1] - fn2[1]) - (fn1[1] - fn2[1])*(f[0] - fn2[0])) 
    elif m == 0:
        fn1 = p2[m+1]
        fn2 = p2[m]
        calculation = ((fn1[0] - fn2[0])*(f[1] - fn2[1]) - (fn1[1] - fn2[1])*(f[0] - fn2[0]))
    elif m == 199:
        fn1 = p2[m]
        fn2 = p2[m-1]
        calculation = ((fn1[0] - fn2[0])*(f[1] - fn2[1]) - (fn1[1] - fn2[1])*(f[0] - fn2[0]))
    if calculation < 0:
        k = -k
        sign.append(k)
    elif calculation >= 0:
        sign.append(k)




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
plot = distplot.scatter(sign,t,alpha=1,s=15,c=t,\
norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=min(t),vmax=max(t)),cmap='Blues')
#ax.scatter(xmf,ymf,alpha=0.5,s=35,c=amf,cmap='Reds')
#ax.plot(xp, line(xp))  #x and y need to have same resolution
plt.colorbar(plot,cax=cax)  

distplot.plot([0,0], [0,round(max(t))]) 

signMAX = math.ceil(max(sign))
signMIN = math.floor(min(sign))
fit2 = np.polyfit(sign, t, 6)  #last number is equal to degree of fitting 
line2 = np.poly1d(fit2)
xp5 = np.linspace(int(signMIN), int(signMAX), int(maxX))

distplot.plot(xp5, line2(xp5))


# Save line coordinates as a npy file in the correct folder
lineE = xp5, line2(xp5)
os.chdir("C:\\Users\\gah02\\Documents\\UPMC\\Master's Thesis\\Plots")
arr = np.array(lineE)
np.save('LINE'+str(file)+'.npy',arr)




#Fix the positions of the auto titles! This currently does not work
plt.title ('TG Expression Across Disc', fontsize = 14)
plt.xlabel ('Distance From MF', fontsize = 12)
plt.ylabel ('TG Expression', fontsize = 12)







    
 # If you rather save it as an excel file:   
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




#Makes the 3D Plot
fig = plt.figure(figsize=(20,10))
ax = plt.axes(projection='3d')

zdata = z
xdata = x
ydata = y
ax.scatter3D(xdata, ydata, zdata, c=a, cmap='Reds',s=16);
ax.axis('scaled')






