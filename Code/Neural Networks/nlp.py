# Author: Maciej Majchrzak
# Reference: https://youtu.be/FLZvOKSCkxY

# Imports
from nltk.tokenize import sent_tokenize, word_tokenize 

# Download the required NLTK data
# nltk.download()

# tokenizing
    # form of grouping things
    # work tokenizers, sentence tokenizers
# lexicon
    # words and their means
# corporas
    # body of text, ex: medical jounals, presidential speeches, english language
    
exampleText = "This is being done for main group project. Main goal of this assignment is to get more familliar with python programming language. Another objective is to develop AI chatbot with ability to interact and engage with a human being."

# Tokenize exampleText into sentences
print(sent_tokenize(exampleText), "\n")

# Print each sentence seperately
for i in sent_tokenize(exampleText):
    print(i)

# Tokenize exampleText into words
print("\n", word_tokenize(exampleText), "\n")

# Print each word seperately
for i in word_tokenize(exampleText):
    print(i)