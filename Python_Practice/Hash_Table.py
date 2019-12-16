'''
Created on Nov 24, 2019
=> Create Hash Table without Dictionary 
=> Find the missing elements in a sorted range using a Hash Table.
    ->Given an array arr[0..n-1] of distinct elements and a range 
    ->[low, high], find all numbers that are in range, but not in array. 
    ->The missing elements should be printed in sorted order.
@author: thann
'''

import random

class HashTable(object):

    def __init__(self, length = 4):
        self.array = [None] * length
    
    #Creates Hashing index
    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    #Adds kvp to table
    def add(self, key, value):

        if self.is_full():
            self.double()

        index = self.hash(key)
        if self.array[index] is not None:

            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key,value])

        else:
            self.array[index] = []
            self.array[index].append([key,value])

    #returns value of a key
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            return
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            return

    def is_full(self):
        items = 0
        for item in self.array:
            if item is not None:
                items += 1
        return items > len(self.array)/2

    def double(self):
        bigTable = HashTable(length = len(self.array)*2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for kvp in self.array[i]:
                bigTable.add(kvp[0], kvp[1])

        self.array = bigTable.array

#Finds missing elements in range of array
def missing_elems(array):
    hTable = HashTable(max(array))
    
    for i in range(len(array)):
        hTable.add(array[i],i)

    for i in range(max(array)):
            if hTable.get(i) is None:
                print(i)
        
# Initialize and store rand values in array:
array = []
for x in range(0,10):
    array.append(random.randrange(1,20,1))
#print array before and after to find missing values:
#print(array)
missing_elems(array)

#Done without hash Table in ~O(n^2):
for i in range(max(array)):
    if i not in array:
        print(i)


