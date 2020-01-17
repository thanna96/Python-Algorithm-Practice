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

def insert(root, node):
        if root is None:
            root = node
        else:
            if root.value < node.value:
                if root.right is None:
                    root.right = node
                else:
                    insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)

def In(root):
    if root:
        In(root.left)
        print(root.val)
        In(root.right)

def Post(root):
    if root:
        Post(root.left)
        Post(root.right)
        print(root.value)

def Pre(root):
   if root:
        print(root.value)
        Post(root.left)
        Post(root.right)

def Search(root, node):
    if root:
        if root is node:
            return True
        else:
            remove(root.right, node)
            remove(root.left, node)

def minNode( node): 
    cur = node 
    while(cur.left is not None): 
        cur = cur.left  
    return cur 

def remove(root, key):
    if root is None:
        return root
    
    if key < root.value:
        root.left = remove(root.left, key)

    elif: key > root.value:
        root.right = remove(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minNode(root.right)

        root.value = temp.value 

        root.right = remove(root.right, temp.value)

    return root
        