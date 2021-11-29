# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas 
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
#print ("tup1[0]: ", tup1[0]);
#print ("tup2[1:5]: ", tup2[1:5]);

tup3=("misbah",8928442235,"wagholi")
#print (tup3[0])
a=tup1[2]+tup2[0]
#print (len(tup1))
#print (tup1+tup2)
osv=os.listdir(os.getcwd())
#print(osv)
pd1=pandas.read_csv("E:\\Python\\test\\NewCSV.csv")
#print (pd1.values)
#print (pd1)

#print (len(pd1.values))

#list_of_tuples = [tuple(a) for a in pd1.values]
#print(list_of_tuples)
#for i in list_of_tuples:
 #   if i[1]<30:
     # print (i[0])
    
story = urlopen("http://sixty-north.com/c/t.txt")
print ("i am in temp")
soup =  BeautifulSoup(story, "html.parser" ).encode('UTF-8')

#print (soup)
