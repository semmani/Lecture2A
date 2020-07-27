"""
this chatbot trains models with the intents, but we have to alter it, so that it responds from the data that we have on Cattle disease
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from nltk.stem.lancaster import LancasterStemmer
import nltk
nltk.download('punkt')

stemmer = LancasterStemmer()

# Libraries needed for Tensorflow processing
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import random
import json

#loading intents.json
with open('intents.json') as json_data:
    intents = json.load(json_data)
print(intents)
words = []
classes = []
documents = []
ignore_words = ['?']
# looping thru intents pattern
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)  # tokenizing words
        words.extend(w) # adding words into the list
        # add words in a documents
        documents.append((w, intent['tag']))
        # add tags to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#stemming
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# removing duplicated classes--> sorted() works by appending each no in a
# new list and then doesnt adds if the same no or words exits already
classes = sorted(list(set(classes)))

print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "Uniquely Stemmed words", words)

training = []
output = []
# create an empty array for output
output_empty = [0] * len(classes)

# creating training set, bag of words for each sentence
for doc in documents:
    # initialize bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stemming each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)   # append(1)  ?

    # output is '1' for current tag and '0' for rest of other tags
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffling features and turning it into np.array
random.shuffle(training)
training = np.array(training) # shape of training data is 16,2
#print("shape of training data", training[:,1].shape)

train_x = list(training[:,0]) # features --> intents # shape is (16,)
train_y = list(training[:,1])  # labels ---> tags # shape is (16,)
print(training,training.shape)

# building ann-->
inputLayer = keras.layers.Dense(16, activation=tf.nn.relu, input_shape=(len(train_x[0]), )) #Shape is Number of Features in your training dat aset
hiddenLayer = keras.layers.Dense(8, activation=tf.nn.relu)
outputLayer = keras.layers.Dense(len(train_y[0]), activation=tf.nn.softmax)

ann = [inputLayer, hiddenLayer, outputLayer]

model = keras.Sequential(ann)
#compiling the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_x, train_y, epochs=800, batch_size=8)
model.save("chatbotModel")
print(">> Model saved!!")

#checking for losses-----> code unsure

import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" )) # dumps data in stream of bytes in a file

data = pickle.load( open( "training_data", "rb")) # loads the data structure fro the file
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']


with open('intents.json') as json_data:
    intents = json.load(json_data)

# load the saved model
model = keras.models.load_model('./chatbotModel')

def tokenize_sentence(sentence):
    # tokenizing the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stemming each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# returning bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenizing the pattern
    sentence_words = tokenize_sentence(sentence)
    # creating bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

ERROR_THRESHOLD = 0.30
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence) # if we have a classification then find the matching intent tag
    if results:
        while results:    # loop as long as there are matches to process
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # a random response from the intent
                    return print(random.choice(i['responses']))

            results.pop(0)


#Adding some context to the conversation i.e. Contexualization for altering question and intents etc.
# create a data structure to hold user context
context = {}

classify('Hi')
response('Hello', show_details=True)

response('what do you do?',show_details=True)