
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

def swap_first_and_last(L):
    # Your code goes here
    return None

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
    if L.head == None:
        return -math.inf
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
    if length(L1) != length(L2):
        return False
    
    tempL1 = L1.head
    tempL2 = L2.head
    
    while tempL1 != None and tempL2 != None :
        if tempL1.data != tempL2.data:
            return False
        tempL1 = tempL1.next
        tempL2 = tempL2.next
        
    return True

def delete_first(L):
    if L == None:
        return L
    L.head = L.head.next
    return L

if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.draw()
    L2 = sll.List()
    L2.extend([3,6,1,2,9,7,4,8,5])
    L2.draw()
    
    print(first(L1))   # -inf
    print(first(L2))   # 3
    
    print(last(L1))    # -inf
    print(last(L2))    # 5
    
    swap_first_and_last(L1)
    L1.print()              # []
    swap_first_and_last(L2) # [5, 6, 1, 2, 9, 7, 4, 8, 3]
    L2.print()          
    
    print(length(L1))   # 0
    print(length(L2))   # 9
    
    print(sum_list(L1)) # 0
    print(sum_list(L2)) # 45
    
    print(max_list(L1)) # -inf
    print(max_list(L2)) # 9
    
    print(to_list(L1))  # []
    print(to_list(L2))  # [5, 6, 1, 2, 9, 7, 4, 8, 3]
    
    L3 = sll.List()
    L3.extend([3,6,1,2,9,7,4,8,5]) 
    
    L4 = sll.List()
    L4.extend([3,6,1,2,9,7,4,8,5])
    
    L5 = sll.List()
    L5.extend([3,6,1,2])
    
    print(identical(L1,L2))  # False
    print(identical(L2,L3))  # False
    print(identical(L3,L4))  # True
    print(identical(L4,L5))  # False

    delete_first(L2) 
    L2.print()       # [6, 1, 2, 9, 7, 4, 8, 3]