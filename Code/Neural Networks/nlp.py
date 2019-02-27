# Author: Maciej Majchrzak, Kamila Michel
# Reference: https://youtu.be/FLZvOKSCkxY

# Goal of the python code below is to familiarize ourselves with NLP (Natural Language Processing)

# Imports
import nltk
import random
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union, gutenberg, wordnet, movie_reviews
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import sentiment_mod as s
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# Download the required NLTK data
#nltk.download()

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

def speechTagging():
    # CC	coordinating conjunction
    # CD	cardinal digit
    # DT	determiner
    # EX	existential there (like: "there is" ... think of it like "there exists")
    # FW	foreign word
    # IN	preposition/subordinating conjunction
    # JJ	adjective	'big'
    # JJR	adjective, comparative	'bigger'
    # JJS	adjective, superlative	'biggest'
    # LS	list marker	1)
    # MD	modal	could, will
    # NN	noun, singular 'desk'
    # NNS	noun plural	'desks'
    # NNP	proper noun, singular	'Harrison'
    # NNPS	proper noun, plural	'Americans'
    # PDT	predeterminer	'all the kids'
    # POS	possessive ending	parent\'s
    # PRP	personal pronoun	I, he, she
    # PRP$	possessive pronoun	my, his, hers
    # RB	adverb	very, silently,
    # RBR	adverb, comparative	better
    # RBS	adverb, superlative	best
    # RP	particle	give up
    # TO	to	go 'to' the store.
    # UH	interjection	errrrrrrrm
    # VB	verb, base form	take
    # VBD	verb, past tense	took
    # VBG	verb, gerund/present participle	taking
    # VBN	verb, past participle	taken
    # VBP	verb, sing. present, non-3d	take
    # VBZ	verb, 3rd person sing. present	takes
    # WDT	wh-determiner	which
    # WP	wh-pronoun	who, what
    # WP$	possessive wh-pronoun	whose
    # WRB	wh-abverb	where, when

    # Part of Speech tagging
        # tags different words into categories
    # To get valid results its best to train on two different datasets
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            print(tagged)   # print tagged words

    except Exception as e:
        print(str(e))
    
    return

def chunking():
    # Chunking - grouping words into meaningful chunks. One of the main goals of chunking is to group into what are 
    # known as "noun phrases." These are phrases of one or more words that contain a noun, maybe some descriptive 
    # words, maybe a verb, and maybe something like an adverb. The idea is to group nouns with the words that are in relation to them.
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""   # RB - find any adverb, NNP - proper noun
            chunkParser = nltk.RegexpParser(chunkGram)  # pass chunk as a regular expression
            chunked = chunkParser.parse(tagged) # pass tag into chunkParser

            # Accessing data via program
            for subtree in chunked.subtrees():
                    print(subtree)

            # Getting just the chunks, ignoring the rest
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                    print(subtree)

            # chunked.draw() # draw chunk
            print(chunked)
            
    except Exception as e:
        print(str(e))
    
    return

def chinking():
    # Chinking - is a lot like chunking, it is basically a way for you to remove a chunk from a chunk. The chunk that 
    # you remove from your chunk is your chink.
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            
            chunkGram = r"""Chunk: {<.*>+}
                                        }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)  # pass chunk as a regular expression
            chunked = chunkParser.parse(tagged) # pass tag into chunkParser

            chunked.draw() # draw chunk
            
    except Exception as e:
        print(str(e))

    return

def namedEntityRecognition():
    # Named Entity Recognition
    # NE Type and Examples
    # ORGANIZATION - Georgia-Pacific Corp., WHO
    # PERSON - Eddy Bonte, President Obama
    # LOCATION - Murray River, Mount Everest
    # DATE - June, 2008-06-29
    # TIME - two fifty a m, 1:30 p.m.
    # MONEY - 175 million Canadian Dollars, GBP 10.40
    # PERCENT - twenty pct, 18.75 %
    # FACILITY - Washington Monument, Stonehenge
    # GPE - South East Asia, Midlothian
    trainText = state_union.raw("2005-GWBush.txt")   # used to train
    exampleText = state_union.raw("2006-GWBush.txt")    # used to test

    customSentenceTokenizer = PunktSentenceTokenizer(trainText)   # custom tokenizer
    tokenized = customSentenceTokenizer.tokenize(exampleText)   # sentence

    try:
        for t in tokenized: # loop through tokenized
            words = word_tokenize(t)    # tokenize words
            tagged = nltk.pos_tag(words)    # part of speech tagging
            
            namedEnt = nltk.ne_chunk(tagged, binary=True)   # classifies as named entity
            namedEnt.draw()
            
    except Exception as e:
        print(str(e))
    return

def lemmatizing():
    # Lemmatizing 
    # Similar operation to stemming is called lemmatizing. The major difference between these is, as you saw earlier, 
    # stemming can often create non-existent words. So, your root stem, meaning the word you end up with, is not something you 
    # can just look up in a dictionary. A root lemma, on the other hand, is a real word. Many times, you will wind up with a very 
    # similar word, but sometimes, you will wind up with a completely different word.

    lemmatizer = WordNetLemmatizer()

    print(lemmatizer.lemmatize("cats"))
    print(lemmatizer.lemmatize("cacti"))
    print(lemmatizer.lemmatize("geese"))
    print(lemmatizer.lemmatize("rocks"))
    print(lemmatizer.lemmatize("python"))
    print(lemmatizer.lemmatize("better", pos="a"))  # adjective
    print(lemmatizer.lemmatize("best", pos="a"))
    print(lemmatizer.lemmatize("run"))
    print(lemmatizer.lemmatize("run",'v'))  # verb

    return

def corpora():
    # Corpora - The NLTK corpus is a massive collection of all kinds of natural language data sets 
    # C:\Users\Ltrmex\AppData\Roaming\nltk_data\corpora
    print(nltk.__file__) # location of the NLTK module's __init__.py

    sample = gutenberg.raw("bible-kjv.txt") # access sample text

    tok = sent_tokenize(sample)

    for x in range(5):
        print(tok[x])
    return


def WordNet():
    # WordNet is a part of Copra. It allows to take words and checks for synonyms,
    # antonysm, definitions or context of that word.

    # Declare synonyms antonysm
    syns = wordnet.synsets("program") 
    synonyms = []
    antonyms= []
    
    # Output list of synsets for word program
    print(syns[0].name())
    # Outut only the word
    print(syns[0].lemmas()[0].name())
    # Checks for definition
    print(syns[0].definition())
    # Checks for examples
    print(syns[0].examples())

    # Loops through list of synonyms for word good
    for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
            synonyms.append(l.name())
            # Checks for antonyms to word good
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    print(set(synonyms))
    print(set(antonyms))

    # Similarity Part

    # Declare words
    w1 = wordnet.synset("car.n.01")
    w2 = wordnet.synset("wheel.n.01")

    # Calculate % of similarity between w1 and w2
    print(w1.wup_similarity(w2))

    w1 = wordnet.synset("house.n.01")
    w2 = wordnet.synset("window.n.01")

    # Calculate % of similarity between w1 and w2
    print(w1.wup_similarity(w2))
    return
# Combine the votes of all of the classifiers, and then classified the text whatever the majority vote was
# Inherit from ClassifierI class from Nl
class VoteClassifier(ClassifierI):
    def __init__(self, *classfiers): #Always run without calling and passes list of classiers through vote classfier
        self._classfiers = classfiers 
    def classify(self, features): # synonymous with the NLTK classfiers 
        votes = []
        for c in self._classfiers:
            v = c.classify(features) # for each classfier get vote
            votes.append(v)
        return mode(votes) # Most votes

    def confidence(self, features):
        votes = []
        for c in self._classfiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes)) # counts how many occurances of that most popular vote were in that list
        conf = choice_votes/len(votes)
        return conf

def textClassification():
    #Acces a file
    short_pos = open("/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/Neural Networks/positive.txt", "r").read()
    short_neg = open("/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/Neural Networks/negative.txt", "r").read()

    # declare list of documents
    documents = []

    for r in short_pos.split('\n'):
        documents.append((r, "pos"))
    
    for r in short_neg.split('\n'):
        documents.append((r, "neg"))

    all_words= []

    # Converts words
    short_pos_words = word_tokenize(short_pos)
    short_neg_words = word_tokenize(short_neg)

    for w in short_pos_words:
        all_words.append(w.lower())
    
    for w in short_neg_words:
        all_words.append(w.lower())

    # Converts all_words to NLTK frequency distribution
    all_words = nltk.FreqDist(all_words) # ordered from most common to the least common word
    # Outputs 20 most common words
    #print(all_words.most_common(20))
    # Amout of word in movie_reviews
    # print(all_words["dog"]) 

    # Limit on amount of words
    word_features = list(all_words.keys()) [:5000]  # Sets the amout of words

    def find_features(document):
        # Find feature
        words = word_tokenize(document)
        features = {}
        for w in word_features: # if on of top 3000 words is withind this document will return true
            features[w]= (w in words)
        return features

    #print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
    
    featuresets = [(find_features(rev), category) for (rev, category) in documents]
    
    random.shuffle(featuresets)
    # Declare sets for dataset with positive data examples
    training_set = featuresets[:10000] # trains
    testing_set = featuresets[10000:]# feed through the feature sets

    # Declare sets for dataset with negative data examples
    #training_set = featuresets[:100] # trains
    #testing_set = featuresets[100:]# feed through the feature sets
    
    # Naive Bayes algorithm it's type of classifier that's works on very independent assuption
    # for each feature
    # posterior it's likehood of somethng positive

    classifier = nltk.NaiveBayesClassifier.train(training_set)
    #classifier_f = open("naivebayes.pickle","rb") #read in bytes
    #classifier = pickle.load(classifier_f)
    #classifier_f.close()
    # outputs accuracy
    print("Original Naive Bayes Algotithm:",(nltk.classify.accuracy(classifier, testing_set))*100)
    classifier.show_most_informative_features(20) # Shows most popular words on both sides

    # Saving traning algorith Part
    # Pickle  can save python objects

    #save_classifier = open("naivebayes.pickle","wb") #write in bytes
    #pickle.dump(classifier, save_classifier)
    #save_classifier.close()

    # Multinomial Naive Base classfier
    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(training_set)
    print("MNB_classifier accuracy percent:",(nltk.classify.accuracy(MNB_classifier, testing_set))*100)

    # Gaussian Naive Base classfier
    #GaussianNB_classifier = SklearnClassifier(GaussianNB())
    #GaussianNB_classifier.train(training_set)
    #print("GaussianNB accuracy percent:",(nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)
    
    # Bernoulli Naive base classfier
    BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
    BernoulliNB_classifier.train(training_set)
    print("BernoulliNB_classifier accuracy percent:",(nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

    # LogisticRegression classfier
    LogisticRegression_classfier =SklearnClassifier(LogisticRegression())
    LogisticRegression_classfier.train(training_set)
    print("LogisticRegression classfier accuracy percent:",(nltk.classify.accuracy(LogisticRegression_classfier, testing_set))*100)
   
    # SGDClassifier classfier
    SGDClassifier_classfier = SklearnClassifier(SGDClassifier())
    SGDClassifier_classfier.train(training_set)
    print("SGDClassifier accuracy percent:",(nltk.classify.accuracy(SGDClassifier_classfier, testing_set))*100)
   
    # SVC classfier least accure
    #SVC_classfier = SklearnClassifier(SVC())
    #SVC_classfier.train(training_set)
    #print("SVC classfier accuracy percent:",(nltk.classify.accuracy(SVC_classfier, testing_set))*100)
    
    # LinearSVC classfier
    LinearSVC_classfier = SklearnClassifier(LinearSVC())
    LinearSVC_classfier.train(training_set)
    print("LinearSVC_classfier accuracy percent:",(nltk.classify.accuracy(LinearSVC_classfier, testing_set))*100)
    
    # NuSVC classfier
    NuSVC_classfier = SklearnClassifier(NuSVC())
    NuSVC_classfier.train(training_set)
    print("NuSVC_classfier accuracy percent:",(nltk.classify.accuracy(NuSVC_classfier, testing_set))*100)

    voted_classifier = VoteClassifier(
                                  NuSVC_classfier,
                                  LinearSVC_classfier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classfier)

    print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)
    #print("Classification:", voted_classfier.classify(testing_set[0][0]), "Confidence %", voted_classfier.confidence(testing_set[0][0]))


    #print("Classification:", voted_classfier.classify(testing_set[1][0]), "Confidence %", voted_classfier.confidence(testing_set[1][0]))
    #print("Classification:", voted_classfier.classify(testing_set[2][0]), "Confidence %", voted_classfier.confidence(testing_set[2][0]))
    #print("Classification:", voted_classfier.classify(testing_set[3][0]), "Confidence %", voted_classfier.confidence(testing_set[3][0]))
    #print("Classification:", voted_classfier.classify(testing_set[4][0]), "Confidence %", voted_classfier.confidence(testing_set[4][0]))
    #print("Classification:", voted_classfier.classify(testing_set[5][0]), "Confidence %", voted_classfier.confidence(testing_set[5][0]))
    return

def sentimenAnalysis():
    print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
    print(s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
    return

def tweeterDemo():
    #consumer key, consumer secret, access token, access secret.
    ckey="kNlyGXH4RdKlmiNPtLnsBpAPA"
    csecret="MxYcqgDjueHcRvZV5bzkBQHPR218CkDgBkt90GpZiEIRIbuwOE"
    atoken="1092197457860222976-xTBpWFgzfXVm6tsiT1wi6xsTpTo2qz"
    asecret="gdmIAkUHWBFKsOU1ecVyxMMlKMYtBbg7GNTdBTvndl7sT"

    class listener(StreamListener):
        def on_data(self, data):
            all_data = json.loads(data)
            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True

        def on_error(self, status):
            print(status)


    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["happy"])
    return
# preprocessing()
stopWords()
# stemming()
# speechTagging()
# chunking()
# chinking()
# namedEntityRecognition()
# lemmatizing()
# corpora()
# WordNet()
# textClassification()
# sentimenAnalysis()
# tweeterDemo()



