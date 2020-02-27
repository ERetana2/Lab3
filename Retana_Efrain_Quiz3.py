"""
@Author: Efrain Retana
@Professor: Olac Fuentes
@Assignment: Quiz 3
"""


import numpy as np
import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def sorted_rows(A):
    # iterate through the whole matrix and compare if values are sorted
    for i in range(len(A)):
#        for j in range(len(A[i]) - 1):
#            if(A[i][j] > A[i][j+1]):
#                return False
        TF = issortedrows(A,i)
#        all(A[i][j] > A[i][j + 1] for j in range(len(A[i])))
    return True

def second(L):
    # if L has less than two Nodes return None
    if L.head.next == None or L.head == None:
        return None
    return L.head.next.data # return the data of the second Node

def count_occurrences(L,i) :
    # Count the number of times that i appears in L while L is not None
    count = 0  
    tempL = L.head
    while tempL != None:
        if tempL.data == i:
            count += 1
        tempL = tempL.next
    return count

def remove_all_but_first_and_last(L):
    # if list has less than two Nodes return
    # set the next node to the head point to the tail of the list
    if L.head == None or L.head.next == None:
        return
    L.head.next = L.tail
    
if __name__ == "__main__":
    plt.close('all')
    A1 = np.array([[1,2,3],[4,5,6],[2,3,9]])
    A2 = np.array([[1,2,3],[4,3,6],[7,8,9]])
    print(A1)
    print(A2)
    print(sorted_rows(A1)) # True 
    print(sorted_rows(A2)) # False
    
    L1 = sll.List()
    L1.append(2302)
    L1.draw()
    L2 = sll.List()
    L2.extend([3,6,1,2,9,7,4,8,6,5])
    L2.draw()
    
    print(second(L1))  # None
    print(second(L2))  # 6
    
    L= sll.List()
    L.extend([3,6,1,2,9,7,4,8,6,5])
    L.draw()
    
    print(count_occurrences(L,0)) # 0
    print(count_occurrences(L,6)) # 2
    print(count_occurrences(L,5)) # 1
    
    L= sll.List()
    L.extend([3,6,1,2,9,7,4,8,6,5])
    L.draw()
    
    remove_all_but_first_and_last(L)
    
    L.print() # [3, 5]

