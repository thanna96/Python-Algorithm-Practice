'''
Created on Nov 24, 2019
    => Creates Binary Search tree
@author: thann
'''

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
            self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if self.root.left is None and self.root.right is None:
                self.root.left = Node(value)
            elif self.root.left is not None and self.root.left.val <= value:
                self.root.addRight(value)
            else:
                self.root.addLeft(value)

    def addLeft():

    def addRight():

    def Post():

    def Pre():

    def In():

    def remove():

    def search();
    
