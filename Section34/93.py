# The Python Mega Course: Build 10 Real World Applications
# Chatbot Version 4.0
# Let's now make the chatbot highly intelligent.

# So far the bot only answers if the user question has an exact match in the vocabulary. For example, it answers the question "what is the time", but it doesn't answer if the query is "tell me the time". You need to modify the function so that if the user asks questions such as "tell me the time", the function returns the time even though "tell me the time" was not in the vocabulary.

# So, in other words, you need to implement a function that:

# (1) takes as parameters a query (e.g. "bye bye" ) and the given vocabulary 

# (2) calculates a similarity ratio for each of the vocabulary keys and

# (3) returns the vocabulary value (i.e. "Goodbye") that has the highest ratio.

# import datetime
# import difflib


# vocabulary = {
#     "hello" : "Hi there!",
#     "what's your name" : "My name is Roboto!",
#     "what is your name" : "My name is Roboto!",
#     "bye" : "Goodbye!",
#     "what time is it" : datetime.datetime.now().strftime("%H:%M")
# }

# def foo(query, vocabulary):

import datetime
import difflib


vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

def foo(query, vocabulary):
    new_vocabulary = {key:[value, difflib.SequenceMatcher(None, query, key).ratio()] 
    for (key,value) in vocabulary.items()}
    return new_vocabulary[max(new_vocabulary, key=lambda k: new_vocabulary[k][1])][0]