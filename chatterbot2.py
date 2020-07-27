# model training


import pickle
import numpy as np
import random
import json
import nltk
from nltk import RegexpTokenizer
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout,Flatten
from keras.optimizers import SGD   # importing stochastic gradient descent
import matplotlib.pyplot as plt

from chatterbotBot import bag_of_words, tokenizing, stemming

import json
with open('intents.json') as json_data:
    intents = json.load(json_data)


sent_tokens = []
word_tokens = []
tags = []
doc = []
resp = []
for intent in intents['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        s = nltk.sent_tokenize(pattern.lower())
        w = nltk.word_tokenize(pattern.lower())
        sent_tokens.append(s)
        word_tokens.extend(w)    # all words
        doc.append((w, tag))    # pair pattern
        # add tags to our classes list
        if intent['tag'] not in tags:
            tags.append(intent['tag'])   # all tags
    # for response in intent['response']:
    #     resp.append(intent['response'])  # all responses
    #     s = nltk.sent_tokenize(response.lower())
    #     w = nltk.word_tokenize(response.lower())
    #     word_tokens.extend(w)
    #     sent_tokens.append(s)
    #     doc.append(w)

print(len(sent_tokens), "sentence tokens",  sent_tokens)
print("\n")
print(len(word_tokens), "words",  word_tokens)   # ..... words including punctuations
print("\n")
print(len(tags), "all tags",  tags)
print("\n")
print(len(resp), "responses", resp)
print("\n")
print(len(doc), "pattern", doc, type(doc))


ignore_words = ['?', '.', '!']
word_tokens = [stemming(w) for w in word_tokens if w not in ignore_words]
# remove duplicates and sort
# cleaned_tokens = sorted(set(word_tokens))
# tags = sorted(set(tags))



# now finally creating training data
X_train = []
Y_train = []

for sent_pattern, tag in doc:
    bag = bag_of_words(sent_pattern, word_tokens)   # bag of words is taking all sentences and tags, will tokenize the sentence
    X_train.append(bag)
    label = tags.index(tag)    #FOR CROSSENTROPY LOSS...WE NEED LABELS ONLY
    Y_train.append(label)

X_train = np.array(X_train)
Y_train = np.array(Y_train)

print("X_TRAINING:",X_train.dtype, X_train)
print("Y_TRAINING:",Y_train.dtype, Y_train)


#Hyper-parameters
# num_epochs = 1000/800
# batch_size = 8
# learning_rate = 0.001/0.01
input_size = len(X_train[0])
# hidden_size = 8
output_size = len(tags)
print("input:", input_size, np.shape(input_size), type(input_size))
print("output", output_size, np.shape(output_size))

inputLayer = keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(input_size, ))
hiddenLayer = keras.layers.Dense(32, activation=tf.nn.relu)
outputLayer = keras.layers.Dense(output_size, activation=tf.nn.softmax)

ann = [inputLayer, hiddenLayer, outputLayer]

model = keras.Sequential(ann)
sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)   #LEARNING RATE For SGD=0.01 i.e is generally called step_size which is amountof weights changed in network, DECAY
model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Training the Model
# We are training in 3 iterations. Every iteration will have some results.
history = model.fit(X_train, Y_train, epochs=800, batch_size=8)

# history will contain information about loss and accuracy details over each epoch
print("===HISTORY===")
print(history.history.keys())
print(history.history)

epochs_range = 800


print(">>  VISUALIZING ACCURACY AND LOSS")
acc = history.history['accuracy']
#val_acc = history.history['val_accuracy']

loss = history.history['loss']
#val_loss = history.history['val_loss']


# overall metrics
loss, accuracy = model.evaluate(X_train, Y_train)
print(">> Loss:", loss)
#print(">> Validation Loss:", val_loss)
print(">> Accuracy:", accuracy)
#print(">> Validation Accuracy:", val_acc)


# plt.plot(epochs_range, acc, label='Training Accuracy')
# #plt.plot(epochs_range, val_acc, label='Validation Accuracy')
# plt.legend(loc='lower right')
# plt.title('ACCURACY')

#plt.plot(epochs_range, loss, label='Training Loss')
#plt.plot(epochs_range, val_loss, label='Validation Loss')
#plt.legend(loc='upper left')
#plt.title('LOSS')

#plt.show()


#heyypickle.dump(model, open("final_model.pkl", 'wb'))


import torch

import webbrowser

# url = 'http://google.com'
#
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

# writing chatting module

bot_name = "Anveg"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    user_response = input("You: ")
    # if user_response == "google" or "open google":
    #     webbrowser.get(chrome_path).open(url)
    if user_response == '[0-9]':
        print("oops! you typed numeric key")
    elif user_response == "quit":
        break

    sentence_token = tokenizing(user_response)
    X = bag_of_words(sentence_token, word_tokens)
    X = X.reshape(1, X.shape[0])
    X = np.array(X)

    probabilityModel = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    predictions = probabilityModel.predict(X)
    predicted = np.argmax(predictions[0])
    #print(predicted)   # generates the
    tag = tags[predicted.item()]
    # print(tag)   # correct predictions of the tags till now

    # probs = torch.softmax(output, dim=1)
    prob = predictions[0][predicted.item()]
    #print(prob)
    if prob.item() > 0.10:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['response'])}")
    else:
        print(bot_name + ":" + "I do not understand...")










