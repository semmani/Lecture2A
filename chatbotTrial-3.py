
"""
Retrieval based chatbots--->
         Pre defined Responses ---> intents.json file
         context based answers

         KNOWLEDGE <-------  CHAT SOURCES
          RULES
        MACHINE LEARNING
1. SCIKIT LEARN                     NLTK---> classification , tokenization(sentence, words), stemming(lemmatizing the words), parsing
2. BAG OF WORDS or VETCTORIZATION
       OR
 TF-IDF FORMULA----> term frequency - inverse document frequency
TF-->  term frequency -->NO OF TIMES A TERM APPEARS / NO OF TOTAL TERMS IN DOCUMENT
IDF --> 1 + LOG(X/Y)
Eg.  in 500 words call appears 10 times---> term freq = 10/500 = 0.02



"""

import nltk
from nltk import RegexpTokenizer
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout,Flatten
from keras.optimizers import SGD   # importing stochastic gradient descent
import pandas as pd
import pickle
import random
import numpy as np


import json
with open('intents.json') as json_data:
    intents = json.load(json_data)

print()

#for intent in intents['intents']:
    #print(intent) # this basically prints all the intents we created i.e tags,patterns, responses and contexts evrythings
   # print(intent['tag']) # prints all the tags we made i.e greeting,cattle_disease

#preprocessing involves ccreatign bag of words
word_tokens = []
tags = []
doc = []   #bag of words model
ignore_words = ['?']
# loop through each sentence in the intent's patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        word_tokens.extend(w)
        doc.append((w, intent['tag']))
        # add tags to our classes list
        if intent['tag'] not in tags:
            tags.append(intent['tag'])

print(doc)  # 'hi' ,'greeting'
# print()
print(word_tokens)
# print()
print(tags)
st = nltk.stem.PorterStemmer()
# words = [st.stem(w.lower()) for w in word_tokens if w not in ignore_words] # stemming and lowercasing each word and removing duplicates
# words = sorted(list(set(words)))
#sorting the tags
# tags = sorted(list(set(tags)))
# print(len(bagOfWords), "bagOfWords", bagOfWords)  # bagofwords = combination between patterns and intents
#tags = intents
# print(len(tags), "tags", tags)
# vocabulary
# print(len(words), "unique stemmed words", words)
# from nltk.stem import WordNetLemmatizer
#
# def lemmatizing(tokens):
#     lemmer = WordNetLemmatizer()
#     lem_words=  [lemmer.lemmatize(w) for w in tokens]
#     print("lemmatized words", sorted(list(set(lem_words))))





#lemmatizing(word_tokens)


# creating vectors of bag of words
training_data = []
output = np.zeros(len(tags), dtype=int)  # len of tags is 8 so output is array containing 8 zeroes i.e [0, 0, 0, 0, 0, 0, 0, 0]  ` ONHOTENCODING
for bg in doc:
    bag = []
    pattern_words = bg[0]  # contains ['hi', greeting ]
    pattern_words = [st.stem(word.lower())for word in pattern_words]
    print(pattern_words)     # this contains all the patterns related to one tag
    for w in word_tokens:
        bag.append(1) if w in pattern_words else bag.append(0)    # 0 for each tag and 1 for current tag  ~ one hot encoding technique

    print("bag",bag)
    output_row = list(output)
    print("output row:", output_row)
    output_row[tags.index(bg[1])] = 1
    print(output_row)
    training_data.append([bag, output_row])
random.shuffle(training_data) # length of training data
training_data = np.array(training_data)  #shuffling and creating array of training_data
print(len(training_data), "data", training_data, training_data.shape)    #vectors for all the vocabulary
"""
# creating training data
train_x = training_data[:,0] # shape is (25,)  len of trainx[0] = 40  len of train_x is 25   40 features to predict
train_y = training_data[:, 1]    # train_y[0] is 8  len = 25  output length, 8 is the output
  # 25 length  shape = 25, 2   25
print("\n")
print("Training data of X(train_x):",train_x, len(train_x), train_x.shape)
print("Training data of Y(train_y):", train_y, len(train_y), train_y.shape)
print(len(train_x[0]),"data", train_x[0],np.shape(train_x[0]))
print(len(train_y[0]),"data", train_y[0], np.shape(train_y[0]))


model = Sequential()
model.add(Dense(32, input_shape=(len(train_x[0]), ), activation='relu')) # input layer shud be fed with features1
model.add(Dropout(0.3))   # dropout is used to reduce the overfitting of the input given thru input variables 50% inputs set to zero
model.add(Dense(8, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(8, activation='softmax'))   # output neurons will be equal to no of intents i.e 8 or we cn replace it with number

# using different optimisers--> SGD AND ADAM
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)   #LEARNING RATE For SGD=0.01 i.e is generally called step_size which is amountof weights changed in network, DECAY
history = model.compile(loss='sparse_categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit the model
model.fit(train_x, train_y, epochs=500, batch_size=5, verbose=1)

# use fit_generator instead of fit  -> if we have used ImageDataGenerator for our Image Data Set Creation
#history = model.fit_generator(tra, epochs=5, validation_data=testing_images)

print(">> STEP#4 VISUALIZING ACCURACY AND LOSS")
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

# from sklearn.feature_extraction.text import TfidfVectorizer
# vect = TfidfVectorizer(train_x[0])

# dumping file usng pickle

pickle.dump(model, open("cattle-model.pkl", "wb"))
# save all of our data structures
pickle.dump({'words': words, 'tags': tags, 'train_x': train_x, 'train_y': train_y}, open("cattle-data.pkl", "wb"))

# save in different file
with open('cattle-data.pkl') as cat_data:
    model = pickle.load(cat_data)

def classify(sentence):

    # Add these two lines for workaround error _thread._local' object has no attribute 'value'
     # generate probabilities from the model
    ERROR_THRESHOLD = 0.25
    input_data = pd.DataFrame([bow(sentence, words)], index=['input'])
    results = model.predict([input_data], workers=1, verbose=1)[0]

    # filter out predictions below a threshold, and provide intent index
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((tags[r[0]], str(r[1])))
    # return tuple of intent and probability
    return return_list

def clean_up_sentence(user_response):
    # tokenizing the pattern
    sentence_words = nltk.word_tokenize(user_response)
    # stemming each word
    sentence_words = [st.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    # tokenizing the pattern
    sentence_words = clean_up_sentence(sentence)
    # generating bag of words
    bag = np.zeros(len(tags), dtype=int)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)

    return(np.array(bag))

flag=True
print("chatbot initiated!\n")
while flag:
    user_response = input()
    user_response = user_response.lower()
    def botResponse(user_response, userID):
        import random
        tagResult = classify(user_response)
        if not tagResult:
            return "Sorry, I do not understand"
        else:
            flag= False
            print("CHATBOT BYE BYE!")
        responseList = list(filter(lambda x: x['tag'] == tagResult[0][0], intents['intents']))
        return random.choice(responseList[0]['responses'])
 
# tag = ints[0]['intent']
#     list_of_intents = intents_json['intents']
#     for i in list_of_intents:
#         if(i['tag']== tag):
#             result = random.choice(i['responses'])
#             break
#     return result
# """