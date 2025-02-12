
# Chatbot Version 3.0
# Complete the talk function so that it behaves like its previous 2.0 version if we were to call it:

# print(talk("hello", vocabulary)) -> Hi there!
# print(talk("what's your name", vocabulary)) -> My name is Roboto!
# print(talk("how old are you", vocabulary)) -> I don't understand that!
# In addition to version 2.0, this time the chatbot should know how to answer the "what time is it" query:

# print(talk("what time is it", vocabulary)) -> 11:26
# So, the last output is the current time in HH:MM format.

# vocabulary = {
#     "hello" : "Hi there!",
#     "what's your name" : "My name is Roboto!",
#     "what is your name" : "My name is Roboto!",
#     "bye" : "Goodbye!"
# }

# def talk(query, vocabulary):

import datetime

vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

def foo(query, vocabulary):
    if query in vocabulary:
        return vocabulary[query]
    else:
        return "I don't understand that!"