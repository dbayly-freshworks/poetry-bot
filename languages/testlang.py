""" 
Simple language, only accepts pairs of 'a's, or pairs of 'b''s. May end in a period.
S => S.
S => S a a
S => S b b
S=> ε

"""
a = ['a']
b = ['b']

def start(prev, current,next):
    print(prev, current, next)
    if(current in a or current in b):
        prev, current, next = shift(prev,current,next)
        return rule1(prev,current,next)
    elif (current == '.'):        
        return True
    else :
        print ("error at word",current)
        return False

def rule1(prev, current, next):
    if((current in a or current in b) and prev[:-1] != next[0]):
        prev, current, next = shift(prev,current,next)
        return rule1(prev,current,next)
    elif (current == '.'):
        return True
    else:
        print ("error at word",current)
        return False



def shift(prev,current,next):
    print(prev,current,next)
    prev.append(current)
    current = next[0] 
    del next[0]
    return [prev,current,next]

print(start([],'a',['a','b','c','.']))
