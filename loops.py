# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:01:06 2020

@author: acer
"""
lists = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in lists:
    if( item > 150):
        posi=lists.index(item)
        listsize=len(lists)
        print( "value of ",item ,"at position",posi," greater than 150 . total occupants of list is",listsize)
        break
    