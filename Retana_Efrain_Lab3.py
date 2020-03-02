"""
# Draw Fuction Implemented by Olac Fuentes

@Professor: Olac Fuentes
@author: Efrain Retana
@TA : Oscar Galindo
@Assignment: Lab 3
"""

import matplotlib.pyplot as plt
import math
import time

class ListNode:
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    # Constructor
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail

    def print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()
#---------------------------------------------
#PROBLEM 1
    def append(self,x):
        #adds a node to the element after the tail of list
        if self.head is None: #List is empty
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next
        
#----------------------------------------
#PROBLEM 2
    def extend(self,python_list):
        #appends all the set of numbers in the given list 
        for d in python_list:
            self.append(d)
#---------------------------------------
    def length(self):
        if self.head is None:
            return
        length = 0
        tempL1 = self.head
        
        while tempL1 != None:
            length += 1
            tempL1 = tempL1.next
        return length
        
#--------------------------------
#PROBLEM 3
    def insert(self,i,x):
        if self.head is None:
            return None
        if self.length() < i:
            raise ValueError('Index out of Bounds')
        tempL1 = self.head
        if i == 0:
            self.head = ListNode(x,self.head.next)
        else:
            while i > 1:
                tempL1 = tempL1.next
                i -= 1
            tempL1.next = ListNode(x,tempL1.next)
            if tempL1.next.next is None:
                self.tail = tempL1.next
        
            
#------------------------------------------------------
#PROBLEM 4
    def remove(self,x):
        #iterate through list until it finds x in list
        if self.head == None: # if head reference is empty
            return ValueError
        if self.head.data == x: # if head data == x set head to next
             self.head = self.head.next
             return
        tempL1 = L1.head
        #iterate until it finds the x value in the list, and if there is none, return valueError
        while tempL1.next.data != x:
            if tempL1.next == None:
                return ValueError
            tempL1 = tempL1.next
        tempL1.next = tempL1.next.next
#--------------------------------------
# PROBLEM 5
    def pop(self,i = math.inf): # removes the element at index i, or if no index given
        # removes the last element
        
        if self.head == None: # if list is empty retur
            return
        tempL1 = self.head
            #if optional parameter is not used
        # remove the last node and return its value
        if i == math.inf:
            while tempL1.next.next != None:
                tempL1 = tempL1.next
            save_val = tempL1.next.data
            self.tail = tempL1
            tempL1.next = None
            
            return save_val
        else:
        # if optional parameter is used iter until index
            while i != 1 and tempL1.next != None:
                tempL1 = tempL1.next
                i = i - 1
            if i != 1 and tempL1.next == None: # if we reach None or index 1, then the pop value
                                                # is out of index
                return ValueError
            save_val = tempL1.next.data
            tempL1.next = tempL1.next.next # remove the node index in the array and return its value
            return save_val
            
#-----------------------------------
#PROBLEM 6
    def clear(self):
        # clear the whole list
        self.head = None
        self.tail = None
#------------------------------------
#PROBLEM 7
    def index(self,i,firstBounds = 0,secondBounds = math.inf):
        if self.head == None:
            return
        # iterate through the given indexes firstBounds and SecondBounds
        # and search for value of i in the range and return the index starting from firstBounds
        tempL1 = self.head
        currIndex = 0
        iterLength = secondBounds - firstBounds #length of beginning  to the starting index
        
        while tempL1 != None and currIndex != iterLength:
            #iterate to iterlength index
            while tempL1 != None and firstBounds != 0:
                tempL1 = tempL1.next
                firstBounds -= 1
            # start searching for the num i in the range of indices provided
            if tempL1.data == i:
                return currIndex 
            tempL1 = tempL1.next
            currIndex += 1
        # if number was not there, then return a ValueError
        if tempL1 == None or currIndex == iterLength:
             return ValueError 
#----------------------------------------------------------
#PROBLEM 8
    def count(self,x):
        #counts the number of times num x appears in the list
        count = 0
        if self.head == None: # if head reference is empty
            return
        tempL1 = self.head
        
        #run through list and increment count is x is in the current node
        while tempL1 != None:
            if tempL1.data == x:
                count += 1
            tempL1 = tempL1.next
        return count
#-------------------------------------
#PROBLEM 9
    def sort(self):
        # if the the head reference is empty return None
        if self.head == None:
            return None
        if self.head.next == None: # if there is only one element, return the list
            return self 
        # create a native list and append all the elements from the linked list
        dataList = []
        tempL1 = self.head
        
        while tempL1 != None:
            dataList.append(tempL1.data)
            tempL1 = tempL1.next
        # sort the python list
        dataList.sort()
        tempL1 = self.head
        # replace all the elements in the linked list with the new sorted elements
        while tempL1 != None:
            tempL1.data = dataList.pop(0)
            tempL1 = tempL1.next
        
        
#--------------------------------------
#PROBLEM 10
    def reverse(self):
        if self.head == None: # head reference is None
            return
        # append all the elements in the linked list into a python native list
        tempL1 = self.head
        dataList = []
        
        while tempL1 != None:
            dataList.append(tempL1.data)
            tempL1 = tempL1.next
        # set each of the data in the linked list equal to the popped item in the native list
        tempL1 = self.head
        while tempL1 != None:
            tempL1.data = dataList.pop()
            tempL1 = tempL1.next
        
    
#------------------------------------
#PROBLEM 11
    def copy(self):
        if self.head == None: # if head reference None
            return
        tempL1 = self.head
        ListCopy = List() # create new empty list
        # append the old data to the new list(creating a new node)
        while tempL1 != None:
            ListCopy.append(tempL1.data)
            tempL1 = tempL1.next
        # return the newly created copy
        return ListCopy
#----------------------------------------

    def _rectangle(self,x0,y0,dx,dy):
        # Returns the coordinates of the corners of a rectangle
        # with bottom-left corner (x0,y0), dx width and dy height
        x = [x0,x0+dx,x0+dx,x0,x0]
        y = [y0,y0,y0+dy,y0+dy,y0]
        return x,y

    def draw(self,figure_name=' '):
        # Assumes the list contains no loops
        fig, ax = plt.subplots()
        x, y = self._rectangle(0,0,20,20)
        ax.plot(x,y,linewidth=1,color='k')
        ax.plot([0,20],[10,10],linewidth=1,color='k')
        ax.text(-2,15, 'head', size=10,ha="right", va="center")
        ax.text(-2,5, 'tail', size=10,ha="right", va="center")
        t = self.head
        x0 = 40
        while t !=None:
            x, y = self._rectangle(x0,0,30,20)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0+15,x0+15],[0,20],linewidth=1,color='k')
            ax.text(x0+7,10, str(t.data), size=10,ha="center", va="center")
            if t.next == None:
                ax.text(x0+22,10, '/', size=15,ha="center", va="center")
            else:
                ax.plot([x0+22,x0+40],[10,10],linewidth=1,color='k')
                ax.plot([x0+37,x0+40,x0+37],[7,10,13],linewidth=1,color='k')
            t = t.next
            x0 = x0+40
        if self.head == None:
            ax.text(12,15, '/', size=10,ha="center", va="center")
        else:
            ax.plot([10,40],[15,15],linewidth=1,color='k')
            ax.plot([37,40,37],[12,15,18],linewidth=1,color='k')

        if self.tail == None:
            ax.text(12,5, '/', size=10,ha="center", va="center")
        else:
            xt = 40
            t = self.head
            while t!= self.tail:
                t = t.next
                xt+=40
            ax.plot([10,10,xt+15,xt+15],[5,-10,-10,0],linewidth=1,color='k')
            ax.plot([xt+12,xt+15,xt+18],[-3,0,-3],linewidth=1,color='k')

        ax.set_title(figure_name)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.set_size_inches(1.2*(x0+200)/fig.get_dpi(),100/fig.get_dpi())
        plt.show()

if __name__ == "__main__":
    # It won't execute when this file is imported
    plt.close('all')
    L1 = List()
    # APPEND 1
    start_time = time.time_ns()
    L1.append(0)
    end_time = time.time_ns()
    print('Append Total Process Time: %10.20f' % (end_time - start_time))
    L1.draw('Append')
    # EXTEND 2
    start_time = time.time_ns()
    L1.extend([5,1,4,2,6,3])
    end_time = time.time_ns()
    print('Extend Total Process Time: %10.25f' % (end_time - start_time))
    L1.draw('Extend')
    # INSERT 3
    start_time = time.time_ns()
    L1.insert(5,8)
    end_time = time.time_ns()
    print('Insert Total Process Time: %10.25f' % (end_time - start_time))
    L1.draw('Insert')
    # REMOVE 4
    start_time = time.time_ns()
    L1.remove(4)
    end_time = time.time_ns()
    print('Remove Total Process Time: %10.25f' % (end_time - start_time))
    L1.draw('Remove')
    # POP 5a
    start_time = time.time_ns()
    print(L1.pop(2))
    end_time = time.time_ns()
    print('Pop Total Process Time: %10.25f' % (end_time - start_time))
    L1.draw('Pop a')
    # POP 5b
    start_time = time.time_ns()
    print(L1.pop())
    end_time = time.time_ns()
    print('Pop Total Process Time: %10.25f' % (end_time - start_time))
    L1.draw('Pop b')
    # CLEAR 6
    start_time = time.time_ns()
    L1.clear()
    end_time = time.time_ns()
    print('Clear Total Process Time: %10.25f' % (end_time - start_time))
    L1.draw('Clear')
    #-------------------------
    L1.extend([5,1,4,2,6,8,4])
    L1.draw('Current List')
    #------------------------
    # INDEX 7a
    start_time = time.time_ns()
    print(L1.index(2))
    end_time = time.time_ns()
    print('Index Total Process Time: %10.25f' % (end_time - start_time))
    # INDEX 7b
    start_time = time.time_ns()
    print(L1.index(6,2,5))
    end_time = time.time_ns()
    print('Index From Total Process Time: %10.25f' % (end_time - start_time))
    #COUNT 8
    start_time = time.time_ns()
    print(L1.count(4))
    end_time = time.time_ns()
    print('Count Total Process Time: %10.25f' % (end_time - start_time))
    # SORT 9
    start_time = time.time_ns()
    L1.sort()
    end_time = time.time_ns()
    print('Sort Total Process Time: %10.25f' % (end_time - start_time))
    L1.draw('Sorted List')
    # REVERSE 10
    start_time = time.time_ns()
    L1.reverse()
    end_time = time.time_ns()
    print('Reverse Total Process Time: %10.21f' % (end_time - start_time))
    L1.draw('Reversed List')
    # COPY 11
    print('Memory Allocation L1:',L1)
    L1.print()
    print('Memory Allocation L1 Copy:',L1.copy())
    L1.copy().print()



