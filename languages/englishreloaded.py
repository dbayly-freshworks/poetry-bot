#!/usr/bin/python
import random
from nltk.tree import *
dtFile = open('./languages/english words/determiners.txt','r')
determiners = dtFile.read().split()
dtFile.close()

viFile = open('./languages/english words/intransitive-verbs.txt','r')
intransitives_verbs = viFile.read().split()
viFile.close()

vtFile = open('./languages/english words/transitive-verbs.txt','r')
transitive_verbs = vtFile.read().split()
vtFile.close()

ppFile = open('./languages/english words/prepositions.txt','r')
prepositions = ppFile.read().split()
ppFile.close()

nnFile = open('./languages/english words/nouns.txt','r')
nouns = nnFile.read().split()
nnFile.close()

nnsFile = open('./languages/english words/plural-nouns.txt','r')
plural_nouns = nnsFile.read().split()
nnsFile.close()

nnpFile = open('./languages/english words/proper-nouns.txt','r')
proper_nouns = nnpFile.read().split()
nnpFile.close()

ajFile = open('./languages/english words/adjectives.txt','r')
adjectives = ajFile.read().split()
ajFile.close()

def validateEnglish(arr):
    print(arr)
    if(len(arr)==1):
        print('Complete sentence!')
        return arr[0]=='S'
    if(len(arr)==2): 
        if(arr[0]=='NP' and arr[1]=='VP'):
            return validateEnglish(['S'])
    for x in range(len(arr)):
        result = checkSingle(arr[x])
        if(result):
            arr[x] = result
            return validateEnglish(arr)
        if x == len(arr)-1:
            return False
        else: 
            result = checkPair(arr[x],arr[x+1])
            if(result != False):
                arr[x] = result
                del arr[x+1]
                return validateEnglish(arr)

def checkSingle(token):
    if(token == 'Vi'):
        return 'VP'
    if(token == 'NN'):
        return 'Ng'
    if(token == 'NNS'):
        return 'Ng'
    if(token =='NNP'):
        return 'Ng'
    return False

def checkPair(str1,str2):
    if (str1=='Vt' and str2 == 'NP'):
        return 'VP'
    if(str1=='VP' and str2 == 'PP'):
        return 'VP'
    if(str1=='DT'):
        if(str2 =='NNs' or str2 == 'NNp' or str2 == 'NN'):
            return 'NP'
    if(str1=='NP' and str2 =='PP'):
        return 'NP'
    if(str1=='IN' and str2 =='NP'):
        return 'PP'
    if(str1 == 'Ng' and str2 == 'NN'):
        return 'Ng'
    if(str1 == 'Aj' and str2 == 'Ng'):
        return 'Ng'
    if(str1 == 'Ng' and str2 == 'Ng'):
        return 'Ng'
    if(str1 =='NP' and str2 =='NP'):
        return 'NP'
    if(str1 =='VP' and str2 =='VP'):
        return 'NP'

    return False

def checkWord(word):
    word = word.lower()
    print(word)
    if(word in determiners):
        return 'DT'
    if(word in intransitives_verbs):
        return 'Vi'
    if(word in prepositions):
        return 'PP'
    if(word in transitive_verbs):
        return 'Vt'
    if(word in nouns):
        return 'NN'
    if(word in plural_nouns):
        return 'NNs'
    if(word in proper_nouns):
        return 'NNp'
    if(word in adjectives):
        return 'Aj'
    print("Word not found")
    raise Exception("Word not found",word)

def englishReloadedFilterThenCheck(phrase):
    arr = phrase.split()
    try:
        result=map(checkWord, arr)
        return validateEnglish(list(result))
    except Exception:
        return False

def generateEnglishReloadedSentence(token):
    if(token == 'S'):
        return generateEnglishReloadedSentence('NP')+ " "+generateEnglishReloadedSentence('VP')
    if(token == 'VP'):
        results = random.choice([['Vi'],['Vt','NP'],['VP','PP']])
        return reduce(concatReduce,map(generateEnglishReloadedSentence,results))
    if(token == 'NP'):
        results = random.choice([['DT','Ng'],['NP','PP']])
        return reduce(concatReduce,map(generateEnglishReloadedSentence,results))
    if(token == 'PP'):
        return generateEnglishReloadedSentence('IN')+" "+generateEnglishReloadedSentence('NP')
    if(token =='Ng'):
        results = random.choice([['NN'],['NNp'],['NNs'],['Ng','Ng'],['Aj','Ng']])
        return reduce(concatReduce,map(generateEnglishReloadedSentence,results))
    if(token == 'Vi'):
        return random.choice(intransitives_verbs)
    if(token == 'Vt'):
        return random.choice(transitive_verbs)
    if(token == 'DT'):
        return random.choice(determiners)
    if(token == 'NN'):
        return random.choice(nouns)
    if(token == 'NNs'):
        return random.choice(plural_nouns)
    if(token == 'NNp'):
        return random.choice(proper_nouns)
    if(token == 'Aj'):
        return random.choice(adjectives)
    if(token == 'IN'):
        return random.choice(prepositions)
    print("YER OFF THE EDGE OF THE MAP!",token)

def concatReduce(a,b):
    return a +" " + b

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value



def generateEnglishReloadedTree(token):
    if(token == 'S'):
        leftChild = generateEnglishReloadedTree('NP')
        rightChild = generateEnglishReloadedTree('VP')
        return Tree('S',[leftChild,rightChild])
    if(token == 'VP'):
        results = random.choice([['Vi'],['Vt','NP'],['VP','PP']])
        children =  list(map(generateEnglishReloadedTree,results))
        return Tree('VP',children)
    if(token =='Ng'):
        results = random.choice([['NN'],['NNp'],['NNs'],['Ng','Ng'],['Aj','Ng']])
        return Tree('Ng',map(generateEnglishReloadedTree,results))
    if(token == 'NP'):
        results = random.choice([['DT','Ng'],['NP','PP']])
        children = list(map(generateEnglishReloadedTree,results))
        return Tree('NP', children )
    if(token == 'PP'):
        leftChild = generateEnglishReloadedTree('IN')
        rightChild = generateEnglishReloadedTree('NP')
        return Tree('PP', [leftChild,rightChild])
    if(token == 'Vi'):
        return Tree('Vi',[random.choice(intransitives_verbs)])
    if(token == 'Vt'):
        return Tree('Vt',[random.choice(transitive_verbs)])
    if(token == 'DT'):
        return Tree('DT',[random.choice(determiners)])
    if(token == 'NN'):
        return Tree('NN',[random.choice(nouns)])
    if(token == 'NNs'):
        return Tree('NNs',[random.choice(plural_nouns)])
    if(token == 'NNp'):
        return Tree('NNp',[random.choice(proper_nouns)])
    if(token == 'Aj'):
        return Tree('Aj',[random.choice(adjectives)])
    if(token == 'IN'):
        return Tree('IN',[random.choice(prepositions)])
    print("YER OFF THE EDGE OF THE MAP!",token)
# generateEnglishTree('S').draw()
# print(generateEnglishSentence('S'))
# print(filterThenCheck('most clarinet up few cotton below a vase for any goal out much plane in lot scooter clean this car by much dragon'))
# The quick brown fox jumped over the lazy dog 
# englishReloadedFilterThenCheck('The quick brown fox jump over the lazy dog')