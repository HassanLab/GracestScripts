# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:27:49 2018

@author: gah02
"""

import os
import pandas as pd
import xlrd
import csv
import yaml
import math
import numpy as np
from __future__ import print_function
from os.path import join, dirname, abspath
from collections import Counter
from xlrd.sheet import ctype_text

os.chdir("C:\\Users\\gah02\\Desktop")


df = pd.ExcelFile('imaging_progress.xlsx').parse('Imaging')

#make a loop which reads the directory 
filename = "58062_disc_4_D4CH4P.yml";

#make variables from the components of the filename
a,disc,c,ID = filename.split("_")
Sample,filetype = ID.split(".")

vial = int(a)
DiscNo = int(c)

#create lists from desired columns in the excel file
VialNo1 = df['Vial (1st)'].tolist()
VialNo2 = df['Vial (2nd)'].tolist()
GeneName = df['Gene'].tolist()
Quality = df['OVERALL'].tolist()
Notes1 = df['Result 1st'].tolist()	
Notes2 = 	df['Result 2nd'].tolist()

#make a new matrix with only desired information
matrix = [[i,j,k,l,m,n] for i,j,k,l,m,n in zip(VialNo1,VialNo2,GeneName,Quality,Notes1,Notes2)]

#modify the matrix based on the filename
V1 = []
V2 = []
GN = []
Q = []
N1 = []
N2 = []
  
for e in matrix:
    if e[0] == vial or e[1] == vial:
        
        V1.append(e[0])
        V2.append(e[1])
        GN.append(e[2])
        Q.append(e[3])
        N1.append(e[4])
        N2.append(e[5])
        
        
matrixNEW = [[i,j,k,l,m,n] for i,j,k,l,m,n in zip(V1,V2,GN,Q,N1,N2)]   

print(matrixNEW)     

#create a dictionary from the matrix
# Empty dict
dict1 = {}
# Fill in the entries one by one and maintain the specified order
from collections import OrderedDict
dict1 = OrderedDict()

dict1["Vial"] = V1
dict1["Vial2"] = V2
dict1["GeneName"] = GN
dict1["Quality"] = Q
dict1["Notes"] = N1
dict1["Notes2"] = N2
dict1["Microscope"] = yaml.load(open(filename))


#print(dict1)

#save the newly formated dict as a csv file
with open('discImage_file'+str(filename)+'.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in dict1.items()]



### The code below does not work yet, the intention is to leave out the "nan" variables

if not math.isnan(V1):
    dict1["Vial"] = V1
elif not math.isnan(V2):
    dict1["Vial"] = V2
    
    if not math.isnan(N1):
        dict1["Notes"] = N1
    elif not math.isnan(N2):
        dict1["Notes"] = N2