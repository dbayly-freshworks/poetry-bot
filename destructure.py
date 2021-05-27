import nltk
nltk.ClassifierBasedPOSTagger
nltk.ClassifierBasedTagger
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from languages.english import generateEnglishSentence

pos=pos_tag(word_tokenize(generateEnglishSentence('S')))
print(pos)


