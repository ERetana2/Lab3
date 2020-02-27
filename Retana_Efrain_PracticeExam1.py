# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:54:57 2020

@author: space
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

def nested_squares(ax,n,x0,y0,size):
    if n > 0:
        points = np.array([[x0 - size,y0 -size],[x0-size,y0+size],[x0+size,y0+size],[x0+size,y0-size],[x0 - size,y0 -size]])
        ax.plot(points[:,0],points[:,1],linewidth = 2, color = 'red')
        nested_squares(ax,n-1,x0 - size,y0,size/2)
        nested_squares(ax,n-1,x0 + size,y0 ,size/2)

def list_n_to_0(n):
#    if n == -1:
#        return []
#    result = list_n_to_0(n-1)
#    result.insert(0,n)
#    return result
    if n > -1:
        return [n] + list_n_to_0(n-1)
    return []

def sum_first_n(L,n):
    tempL = L.head
    
    sum = 0
    while tempL != None and n != 0:
       sum += tempL.data
       tempL = tempL.next
       n -= 1
    return sum

def sum_until(L,i):
    if L.head == None:
        return
    tempL1 = L.head
    sum = 0
    while tempL1.next.data != i or tempL1.next != None:
        sum += tempL1.data
        tempL1 = tempL1.next
    return sum

def next_to_last(L):
    if L.head ==None or L.head.next == None:
        return None
    tempL1 = L.head
    
    while tempL1.next.next != None:
        tempL1 = tempL1.next
    return tempL1.data

if __name__ == "__main__":

    plt.close("all") # Close all figures
    fig, ax = plt.subplots()
    nested_squares(ax,4,0,0,100)
    set_drawing_parameters_and_show(ax)
    
    print(list_n_to_0(0)) # [0]
    print(list_n_to_0(5)) # [5, 4, 3, 2, 1, 0]
    
    L= sll.List()
    L.extend([3,6,1,2,5])
    L.draw()
    
    print(sum_first_n(L,4))  # 12
    print(sum_first_n(L,10)) # 17
    
    print(sum_until(L,3))  # 0
    print(sum_until(L,1))  # 9
    print(sum_until(L,10)) # 17
    
    L1= sll.List()
    print(next_to_last(L1)) # None
    print(next_to_last(L))  # 2