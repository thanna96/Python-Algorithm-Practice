'''
Created on Nov 24, 2019

@author: thann
'''

def isValid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if len(stack) == 0 or dict[char] != stack.pop():
                print("false")
                return False
        else:
            print("false")
            return False
        
    return len(stack) == 0

string = "[]())()[]{}{{}}"

isValid(string)