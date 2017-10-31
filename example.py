import nltk
import sys

sentence = "Go to the end of the corridor" if len(sys.argv) == 1 else sys.argv[1]

print("SENTENCE: " + setence)

tokens = nltk.word_tokenize(sentence)
print("TOKENS: " + str(tokens))

tagged = nltk.pos_tag(tokens)
print("TAGS: " + str(tagged))
