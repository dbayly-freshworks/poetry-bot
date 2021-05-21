#!/usr/bin/python

from languages.aabblangtree import startTree
import nltk
from nltk.corpus import treebank
from nltk.tree import *
from languages.aabblang import validate
from languages.english import filterThenCheck, generateEnglishSentence, generateEnglishTree

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
def demo4(str): 
    str = str.split()
    current = str [0]
    del str[0]
    print(validate([],current,str))
#Abstract language tree generation demo
def demo5(): 
    t = Tree('root',startTree([],'a',['a','b','b','a','a','.']))
    t.draw()


def demo6(str):
    print(filterThenCheck(str))

def demo7():
    generatedSentence  =  generateEnglishSentence('S')
    print(generatedSentence)
    return generatedSentence

def demo8():
    generatedEnglishTree = generateEnglishTree('S')
    generatedEnglishTree.draw()
def main():
    # demo1()
    # demo2()
    # demo3()
    # demo4( 'a a b b a a b b .' )
    # demo4('a a b b . a a b b a')
    # demo5()
    # demo6('The man sleep')
    # demo7()
    # demo6(demo7())
    demo8()


if __name__ == "__main__":
    main()
