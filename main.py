#!/usr/bin/python

import nltk
from nltk.corpus import treebank
from nltk.tree import *
"""




-- Find/construc CFG for english 

"""


def demo1():
    t = treebank.parsed_sents('wsj_0001.mrg')[1]
    t.draw()

def demo2():
    t = Tree.fromstring('(S (NP I) (VP (V enjoyed) (NP my cookie)))')
    t.draw()

def demo3():
    t1  = Tree('e',['beep'])
    t2  = Tree('o',['boop'])

def main():
    print("Hello World!")
    # demo1()
    demo2()
    #demo3()

if __name__ == "__main__":
    main()
