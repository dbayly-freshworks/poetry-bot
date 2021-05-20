""" 
Tree generating 

Simple language, only accepts pairs of 'a's, or pairs of 'b''s. May end in a period.
S => S.
S => S a a
S => S b b
S=> ε

"""
from nltk.tree import *

a = ['a']
b = ['b']

def startTree(prev, current,next):
    if(current in a or current in b):
        prev, current, next = shift(prev,current,next)
        return rule2(prev,current,next)
    elif (current == '.' and len(next) == 0):        
        return Tree('end', ['.'])
    else :
        print ("error at word",current)
        return False
#First of pair
def rule1(prev, current, next):
    print("rule 1:",prev,current,next)
    if (len(next) == 0 and current == '.' ):
        return Tree('end', ['.'])
    if((current in a or current in b) and current == next[0]):
        prev, current, next = shift(prev,current,next)
        return rule2(prev,current,next)
    else:
        print ("Rule 1 error at word",current)
        return False
#Second of pair 
def rule2(prev,current,next):
    print("rule 2:",prev,current,next)
    if(len(next) == 0 ):
        print ("error at word",current)
        return False 
    if((current in a or current in b) and (current != next[0])):
        oldcurrent = current
        prev, current, next = shift(prev,current,next)
        return Tree('pair',[oldcurrent,oldcurrent,rule1(prev,current,next)])
    else:
        print ("Rule 2 error at word",current)
        return False

def shift(prev,current,next):
    prev.append(current)
    current = next[0] 
    del next[0]
    return [prev,current,next]


