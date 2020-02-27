# Code to implement and display singly-linked lists
# Programmed by Olac Fuentes
# Last modified February 12, 2020

import matplotlib.pyplot as plt
import math
import numpy as np

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
        if self.head is None: #List is empty
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next
#----------------------------------------
#PROBLEM 2
    def extend(self,python_list):
        for d in python_list:
            self.append(d)
#--------------------------------
#PROBLEM 3
    def insert(self,i,x):
        tempL1 = L1.head

        if self.head == None : 
            return
        if i == 0:
            self.head = ListNode(x,self.head)
            
        while i > 1 and tempL1  != None:
            tempL1 = tempL1.next
            i -= 1
        newNode = ListNode(x,None)
        tempL1.next,newNode.next = newNode,tempL1.next
#------------------------------------------------------
#PROBLEM 4
    def remove(self,x):
        if self.head == None:
            return ValueError
        if self.head.data == x:
             self.head = None
             return
        tempL1 = L1.head
        
        while tempL1.next.data != x:
            if tempL1.next == None:
                return ValueError
            tempL1 = tempL1.next
        tempL1.next = tempL1.next.next
#--------------------------------------
# PROBLEM 5
    def pop(self,*arg):
        if self.head == None:
            return
        tempL1 = self.head
        
        if None in arg:
            while tempL1.next.next != None:
                tempL1 = tempL1.next
            save_val = tempL1.next.data
            tempL1.next = None
            return save_val
        else:
            for i in arg:
                while i != 1 and tempL1.next != None:
                    tempL1 = tempL1.next
                    i = i - 1
                if i != 1 and tempL1.next == None:
                    return ValueError
                save_val = tempL1.next.data
                tempL1.next = tempL1.next.next
                return save_val
            
#-----------------------------------
#PROBLEM 6
    def clear(self):
        self.head == None
#------------------------------------
#PROBLEM 7
    def index(self,i,firstBounds = 0,secondBounds = math.inf):
        if self.head == None:
            return
        
        tempL1 = self.head
        currIndex = 0
        iterLength = secondBounds - firstBounds
        
        while tempL1 != None and currIndex != iterLength:
            while tempL1 != None and firstBounds != 0:
                tempL1 = tempL1.next
                firstBounds -= 1
            if tempL1.data == i:
                return currIndex 
            tempL1 = tempL1.next
            currIndex += 1
        if tempL1 == None or currIndex == iterLength:
             return ValueError 
#----------------------------------------------------------
#PROBLEM 8
    def count(self,x):
        count = 0
        if self.head == None:
            return
        tempL1 = self.head
        
        while tempL1 != None:
            if tempL1.data == x:
                count += 1
            tempL1 = tempL1.next
        return count
#-------------------------------------
#PROBLEM 9
    def sort(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return self 
        
        dataList = []
        tempL1 = self.head
        
        while tempL1 != None:
            dataList.append(tempL1.data)
            tempL1 = tempL1.next
        dataList.sort()
        tempL1 = self.head
        while tempL1 != None:
            tempL1.data = dataList.pop(0)
            tempL1 = tempL1.next
        
        
#--------------------------------------
#PROBLEM 10
    def reverse(self):
        if self.head == None:
            return
        tempL1 = self.head
        dataList = []
        while tempL1 != None:
            dataList.append(tempL1.data)
            tempL1 = tempL1.next
        tempL1 = self.head
        while tempL1 != None:
            tempL1.data = dataList.pop()
            tempL1 = tempL1.next
        
    
#------------------------------------
#PROBLEM 11
    def copy(self):
        if self.head == None:
            return
        tempL1 = self.head
        ListCopy = List()
        
        while tempL1 != None:
            newNode = ListNode(tempL1.data)
            ListCopy.append(newNode)
            tempL1 = tempL1.next
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
    L1.extend([5,1,4,2,6])
#    L1.insert(0,8)
#    L1.remove(2)
#    print(L1.pop(3))
    print(L1.index(1))
    L1.reverse()
    L1.print()
#    L1.draw('Empty list')
#    L1.extend(list(np.random.permutation(10)))
#    L1.draw('Unsorted list')
#    L1 = List()
#    L1.extend(list(np.arange(10)))
#    L1.draw('Sorted list')
#    L1.tail = L1.head.next.next
#    L1.draw('Bad list!')
#    L1.tail = None
#    L1.draw('Another bad list!')


