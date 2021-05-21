#!/usr/bin/python
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

def validateEnglish(arr):
    print(arr)
    if(len(arr)==1):
        print('Complete sentence!')
        return arr[0]=='S'
    if(len(arr)==2): 
        if(arr[0]=='NP' and arr[1]=='VP'):
            return validateEnglish(['S'])
    for x in range(len(arr)):
        if(arr[x]=='Vi'):
            arr[x] = 'VP'
            return validateEnglish(arr)
        if x == len(arr)-1:
            return False
        else: 
            result = checkPair(arr[x],arr[x+1])
            if(result != False):
                arr[x] = result
                del arr[x+1]
                return validateEnglish(arr)

def checkPair(str1,str2):
    if (str1=='Vt' and str2 == 'NP'):
        return 'VP'
    if(str1=='VP' and str2 == 'PP'):
        return 'VP'
    if(str1=='DT' and str2 =='NN'):
        return 'NP'
    if(str1=='NP' and str2 =='PP'):
        return 'NP'
    if(str1=='IN' and str2 =='NP'):
        return 'PP'
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
    print("Word not found")
    raise Exception("Word not found",word)

def filterThenCheck(phrase):
    arr = phrase.split()
    try:
        result=map(checkWord, arr)
        return validateEnglish(list(result))
    except Exception:
        return False
