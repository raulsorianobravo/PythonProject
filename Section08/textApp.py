# Text parser

def maker(phrase):
    
    quest = ("how", "what", "why")
    
    cap = phrase.capitalize()
    if phrase.startswith(quest):
        return "{}?".format(cap)
    else:
        return "{}.".format(cap)
    
print(maker("how are you"))
print(maker("you are good"))

phraseList = []

while True:
    userInput = input("Enter: ")
    if(userInput == "\end"):
        break
    else:
        phraseList.append(maker(userInput))

print(phraseList)
print(" ".join(phraseList))