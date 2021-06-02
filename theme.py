import spacy
import random
# spacy vectors
nlp = spacy.load("en_core_web_lg")
from languages.english import generateEnglishSentence

# nouns list
nounFile=open('./languages/english words/nouns.txt', 'r+')
nouns=(nounFile.read().split())
nounFile.close()

# themes list
themeFile=open('./languages/english words/themes.txt', 'r+')
themes=(themeFile.read().split())
themeFile.close()
theme=random.choice(themes)
poem=generateEnglishSentence('S')

# check if vector
def checkVector(item):
  tokens = nlp(item)
  for token in tokens: 
    return token.has_vector
    
# check similarity
def isSimilar(theme, poem): 
    doc1=nlp(poem)
    doc2=nlp(theme)
    return (doc1, "<->", doc2, doc1.similarity(doc2))

# Analyze syntax
def analyzeSyntax(poem):
  text = (poem)
  doc = nlp(text)
  return ("Noun phrases:", [chunk.text for chunk in doc.noun_chunks], "Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
  
print("generated poem: ", poem)
print('poem syntax analysis: ', analyzeSyntax(poem))
print('similarity analysis: ', isSimilar(theme, poem))
print(f'{theme} has vector: ', checkVector(theme))
print(f'{poem} has vector: ', checkVector(poem))