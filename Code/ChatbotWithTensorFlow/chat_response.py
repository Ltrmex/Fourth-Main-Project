# References:
# https://media.readthedocs.org/pdf/pyttsx3/latest/pyttsx3.pdf
# https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077, 
# https://sourcedexter.com/tensorflow-text-classification-python/

# Imports for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# Imports for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random
import pyttsx3

# Other imports
import pickle
import json

# restore all of our data structures
data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import our chat-bot intents file
with open('C:/Users/Ltrmex/Desktop/Fourth-Main-Project/parsed.json') as json_data:
    intents = json.load(json_data)

# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))


p = bow("is your shop open today?", words)
print (p)
print (classes)


# load our saved model
model.load('./model.tflearn')

# create a data structure to hold user context
context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        return random.choice(i['responses'])

            results.pop(0)
    
#print(classify('is your shop open today?'))
#print(response('is your shop open today?'))
#print(response("thanks, your great"))

input_test = ""

while input_test != "exit":
    # Pytsx is a cross-platform text-to-speech wrapper.
    engine = pyttsx3.init()
    # Imports id for female voice
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    # Sets the type of voice.
    engine.setProperty('voice', en_voice_id)
    # Sets the speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-5)
    # Sets the speech volume
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    # User input text.
    input_test = input("You: ")
    # Say user input using pyttsx3 library.
    engine.say(input_test)
    # Waits until next input.
    engine.runAndWait()
    # Output chatbot random reponse for given user input.
    result = response(input_test)
    print("Chatbot: ", result)
    # Say chatbot output using pyttsx3 library.
    engine.say(result)
    # Waits until next input.
    engine.runAndWait()
    
    
    

            