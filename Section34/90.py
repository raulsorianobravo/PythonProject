
# Chatbot Version 1.0
# Complete the talk function so that it behaves like below if we were to call it:

# print(talk("hello", vocabulary))
# The output of that would be:

# Hi there!
# Here's some more examples of how the function should behave:

# print(talk("what's your name", vocabulary)) -> My name is Roboto!
# print(talk("what is your name", vocabulary)) -> My name is Roboto!
# print(talk("bye", vocabulary)) -> Goodbye!
# print(talk("what time is it")) -> None



vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!"
}

def foo(query, vocabulary):
    if query in vocabulary:
        return vocabulary[query]