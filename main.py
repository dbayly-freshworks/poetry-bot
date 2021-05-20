#!/usr/bin/python

from languages.aabblangtree import startTree
import nltk
from nltk.corpus import treebank
from nltk.tree import *
from languages.aabblang import *
"""




-- Find/construc CFG for english 

"""

# nltk sample tree 
def demo1():
    t = treebank.parsed_sents('wsj_0001.mrg')[1]
    t.draw()
# nltk sample formatted string
def demo2():
    t = Tree.fromstring('(S (NP I) (VP (V enjoyed) (NP my cookie)))')
    t.draw()
# nltk tree demo
def demo3():
    t1  = Tree('e',['beep'])
    t2  = Tree('o',['boop'])
    t3 = Tree('r',[t1,t2])
    t3.draw()
# abstract grammar validation demo
def demo4(): 
    str = 'a a b b a a b b .'
    str = str.split()
    current = str [0]
    del str[0]
    print(start([],current,str))
# abstract grammar failed validation demo
def demo5(): 
    str = 'a a b b . a a b b a'
    str = str.split()
    current = str [0]
    del str[0]
    print(start([],current,str, []))

#Abstract language tree generation demo
def demo6():
    t = Tree('root',startTree([],'a',['a','b','b','a','a','.']))
    t.draw()

def main():
    print("Hello World!")
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    demo6()

if __name__ == "__main__":
    main()
