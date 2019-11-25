'''
Linked-List Practice
=>Find the Nth node from the end of a LL
=>Find the middle node
@author: thanna
'''
import random

class Node:
    
    def __init__(self, value):
            self.value = value  
            self.next = None

class LinkedList:
        'Initialize List'
        def __init__(self):
            self.head = None
            
        'Insert Node at Start'
        def push(self, value):
            new = Node(value)
            new.next = self.head
            self.head = new
        
        'Insert Node at end'
        def append(self, value):
            new = Node(value)
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new
            
        'Insert Node at Nth index'
        def insert(self, n, value):
            new = Node(value)
            cur = self.head
            for x in range(n-1):
                if(cur.next is None):
                    print"Not enough elements"
                    return
                cur = cur.next
            new.next = cur.next
            cur.next = new
            
        'Delete Node'
        def remove(self, n):
            prev = self.head
            temp = prev.next
            
            'find the nth node'
            for x in range(n-1):
                if(temp is None or temp.next is None):
                    print"Node doesn't exist"
                    return
                prev = prev.next
                temp = prev.next
            
            'remove it'
            prev.next = temp.next
            temp = None
            
        'Print List'
        def printList(self):
            temp = self.head
            x = 0
            while(temp):
                print x,temp.value
                x = x + 1
                temp = temp.next          
        
        'Print Center Node'
        def getMiddle(self):
            temp_1 = self.head
            temp_2 = self.head
            
            while(temp_2 is not None and temp_2.next is not None):
                temp_1 = temp_1.next
                temp_2 = temp_2.next.next
                
            print temp_1.value
            
        'Print Nth node'
        def getN_start(self, n):
            temp = self.head
            
            for x in range(n):
                if(temp.next is None):
                    print"Not enough elements", x
                    return
                temp = temp.next
                
            print temp.value 
                
        'Print Nth from last node'
        def getN_end(self, n):
            temp = self.head
            slow = self.head
            i = 0
            while(temp.next is not None):
                i = i + 1
                temp = temp.next
                if(i > n):
                    slow = slow.next
            print slow.value

'Create Linked List with random values'
list = LinkedList()

for x in range(0,10):
    list.push(random.randrange(1,20,1))

print "List:"
list.printList()
print "remove node 5"
list.remove(5)
print "List:"
list.printList()
print "Insert at end"
list.append(12)
print "List:"
list.printList()
print "insert at index 5"
list.insert(5, 99)
print "List:"
list.printList()
print "Middle:"
list.getMiddle()
print "7th:"
list.getN_start(7)
print "7th from End:"
list.getN_end(7)
