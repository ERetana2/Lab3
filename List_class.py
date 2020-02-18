
"""
@author: Efrain Retana
"""
import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def first(L):
    if L.head != None:
        return L.head.data
    return -math.inf

def last(L):
    if L.tail != None:
        return L.tail.data
    return -math.inf

def length(L):
    tempL = L.head
    length = 0
    while tempL != None:
        length += 1
        tempL = tempL.next
    return length
        
def sum_list(L):
    tempL = L.head
    sum = 0
    while tempL != None:
        sum += tempL.data
        tempL = tempL.next
    return sum

def max_list(L):
    tempL = L.head
    max = 0
    while tempL != None:
        if tempL.data > max:
            max = tempL.data
        tempL = tempL.next
    return max

def to_list(L):
    tempL= L.head
    A = []
    while tempL != None:
        A.append(tempL.data)
        tempL = tempL.next
    return A

def identical(L1,L2):
    tempL1 = L1.head
    tempL2 = L2.head
    identical = True
    
    while tempL1 != None and tempL2 != None :
        if
