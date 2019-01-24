# Author: Maciej Majchrzak
# Reference: https://youtu.be/FLZvOKSCkxY

# Goal of the python code below is to familiarize ourselves with NLP (Natural Language Processing)

# Imports
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download the required NLTK data
# nltk.download()

# tokenizing
    # form of grouping things
    # work tokenizers, sentence tokenizers

def preprocessing():    
    exampleText = "This is being done for main group project. Main goal of this assignment is to get more familiar with python programming language. Another objective is to develop AI chatbot with ability to interact and engage with a human being."

    # Tokenize exampleText into sentences
    print(sent_tokenize(exampleText), "\n")

    # Print each sentence seperately
    for t in sent_tokenize(exampleText):
        print(t)

    # Tokenize exampleText into words
    print("\n", word_tokenize(exampleText), "\n")

    # Print each word seperately
    for t in word_tokenize(exampleText):
        print(t)
    
    return

def stopWords():
    # Stop words  
        # As long as data analytics are concerned there's no much use for stop words (which give english more meaning) such as "our", "the", "a", etc

    exampleSentence = "Purpose of this sentence is to show how to filter stop words"
    stopWords = set(stopwords.words("english"))    # set of english language stop words

    # Print stop words
    print(stopWords, "\n")

    words = word_tokenize(exampleSentence)  # tokenize exampleSentence
    filteredSentence = []   # empty array to hold our filtered words
    filteredSentence2 = [w for w in words if not w in stopWords]    # one line code for same purpose

    # Loop tokenized words
    for w in words:
            if w not in stopWords:  # check each word if it is stop word
                filteredSentence.append(w)  # append to filteredSentence if not a stop word

    # Print the original sentence
    print(exampleSentence)

    # Print the filtered sentence
    print(filteredSentence)
    print(filteredSentence2)

    return



def stemming():
    # Stemming 
        # different affixes of words eg. swim & swimming mean the same things, so stemming is used to save space in database of words
    porterStemmer = PorterStemmer()
    exampleWords = ["playing", "plays", "played", "playfully"]  # array of words to be stemmed

    # Loop through exampleWords
    for w in exampleWords:
        print(porterStemmer.stem(w))    # stem each word and print it

    # Example sentence
    exampleSentence = "Today I played with python playfully to determine if playing would give me new knowledge."

    # Tokenize exampleSentence and loop through words
    for w in word_tokenize(exampleSentence): 
        print(porterStemmer.stem(w))    # print stemmed words

    return

# preprocessing()
# stopWords()
# stemming()