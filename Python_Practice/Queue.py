'''
Created on Nov 24, 2019
=> Create a Queue with 2 Stacks 
@author: thann
'''

class Queue:
    
        'Initialize List'
        def __init__(self):
            self.stack1 = []
            self.stack2 = []
            
        'Insert Node in Back'
        def enQueue(self, value):
            while len(stack1 != 0):
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()

            self.stack1.append(value)

            while len(self.stack2) != 0:
                self.stack1.append(self.stack2[-1])
                self.stack2.pop()
        
        'Remove Node in Front'
        def deQueue(self):
          