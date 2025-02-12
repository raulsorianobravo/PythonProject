
# Chatbot Version 2.0
# Complete the talk function so that it behaves like its previous 1.0 version if we were to call it:

# print(talk("hello", vocabulary)) -> Hi there!
# print(talk("what's your name", vocabulary)) -> My name is Roboto!
# In addition to version 1.0, if an unknown query is passed, the chatbot should return I don't understand that!

# print(talk("what time is it", vocabulary)) -> I don't understand that!
# print(talk("how old are you", vocabulary)) -> I don't understand that!
# Make sure you return exactly "I don't understand that!" including the exclamation mark to make sure your solution is marked as correct.

# vocabulary = {
#     "hello" : "Hi there!",
#     "what's your name" : "My name is Roboto!",
#     "what is your name" : "My name is Roboto!",
#     "bye" : "Goodbye!"
# }

# def talk(query, vocabulary):



vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!"
}

def foo(query, vocabulary):
    if query in vocabulary:
        return vocabulary[query]
    else:
        return "I don't understand that!"