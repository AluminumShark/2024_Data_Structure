
##Important! You shouldn't use statistics library! ("import statistics" is not allowed)

import math
class MinHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getSize(self):
        return self.size
    def insert(self, item): #insert new item 
    ### TODO ### 
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        self.__swim(len(self.array) - 1)
        self.size += 1
    def peek(self):  #Find Minimum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMin(self): 
    ### TODO ###
    ### You need not return or print anything with this function. ###
        value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.__sink(0)
        self.size -= 1
        return value
    def showMinHeap(self):  #Show MinHeap with array
        return self.array
    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
    def __swim(self, i):
        while (i > 0) and (self.array[(i - 1) // 2] > self.array[i]):
            self.__swap(i, (i - 1) // 2)
            i = (i - 1) // 2
    def __sink(self, i):
        while i * 2 + 1 < len(self.array):
            left = i * 2 + 1
            right = i * 2 + 2
            smallest = i
            if left < len(self.array) and self.array[left] < self.array[smallest]:
                smallest = left
            if right < len(self.array) and self.array[right] < self.array[smallest]:
                smallest = right
            if smallest != i:
                self.__swap(i, smallest)
                i = smallest
            else:
                break

class MaxHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getSize(self):
        return self.size
    def insert(self, item): #insert new item
    ### TODO ###
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        self.__swim(len(self.array) - 1)
        self.size += 1
    def peek(self):    #Find Maximum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMax(self):   #Find Maximum item
    ### TODO ###
    ### You need not return or print anything with this function. ###
        value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.__sink(0)
        self.size -= 1
        return value
    def showMaxHeap(self):   #Show MaxHeap with array
        return self.array
    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
    def __swim(self, i):
        while (i > 0) and (self.array[(i - 1) // 2] < self.array[i]):
            self.__swap(i, (i - 1) // 2)
            i = (i - 1) // 2
    def __sink(self, i):
        while i * 2 + 1 < len(self.array):
            left = i * 2 + 1
            right = i * 2 + 2
            largest = i
            if left < len(self.array) and self.array[left] > self.array[largest]:
                largest = left
            if right < len(self.array) and self.array[right] > self.array[largest]:
                largest = right
            if largest != i:
                self.__swap(i, largest)
                i = largest
            else:
                break
                
class FindMedian: 
    def __init__(self):
    ### TODO ###
    ### Your own data structure. Implementing with heap structure is highly recommended. ###
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
    def AddNewValues(self, NewValues):  # Add NewValues(a list of items) into your data structure
    ### TODO ### 
    ### input: a list of values ###
    ### You need not return or print anything with this function. ###
        for value in NewValues:
            if len(self.max_heap.array) == 0 or value <= self.max_heap.peek():
                self.max_heap.insert(value)
            else:
                self.min_heap.insert(value)
            if len(self.max_heap.array) > len(self.min_heap.array) + 1:
                pop = self.max_heap.removeMax()
                self.min_heap.insert(pop)
            elif len(self.max_heap.array) < len(self.min_heap.array):
                pop = self.min_heap.removeMin()
                self.max_heap.insert(pop)
    def ShowMedian(self):  # Show Median of your data structure
    ### TODO ### 
    ### You need not print anything but "return Median". ###
    ###The return value should always be a float number. ###
        if len(self.max_heap.array) > len(self.min_heap.array):
            return float(self.max_heap.peek())
        elif len(self.max_heap.array) < len(self.min_heap.array):
            return float(self.min_heap.peek())
        else:
            return float((self.max_heap.peek() + self.min_heap.peek()) / 2)
    def RemoveMedian(self): # Remove median
    ### TODO ###
    ### You need not return or print anything with this function. ###
    ### If there are even number of elements, remove the larger one ###
    ### For example, if array=[1, 2, 3, 5], remove 3 ###
        if len(self.max_heap.array) > len(self.min_heap.array):
            self.max_heap.removeMax()
        elif len(self.max_heap.array) < len(self.min_heap.array):
            self.min_heap.removeMin()
        else:
            self.max_heap.removeMax()
        if len(self.max_heap.array) > len(self.min_heap.array) + 1:
                pop = self.max_heap.removeMax()
                self.min_heap.insert(pop)
        elif len(self.max_heap.array) < len(self.min_heap.array):
            pop = self.min_heap.removeMin()
            self.max_heap.insert(pop)