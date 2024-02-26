#Import random module
import random
import time
import random as rand
import random

#Greetings and goodbyes
greetings=["Hello!", "What's up!", "Howdy!", "Greetings!"]
goodbyes=["Bye!","Goodbye!","See you later!","See you soon!"]

#Function
def RandomGreeting(list):
    list[rand.randint(0, len(list))-1]
    return
    

#Keywords and responses that AI chatbot will know
keywords = ["music", "pet", "book", "game", "minecraft", "Hi"]
responses=["Music is so relaxing!", "Dogs are man's best friend!", "I know a lot of books.", "I like to play video games.","Minecraft is a great game!","Please continue, you did not enter anything", RandomGreeting(greetings)]

#Info about bot
BotName = "Cortona"

print(random.choice(greetings) + " My name is " + BotName + ".")

user = input("Say something or type bye to quit: ")
user = user.lower()

while (user !="bye"):
    keyword_found = False

    for index in range(len(keywords)):
        if (keywords[index] in user):
            print(BotName + ": " + responses[index])
            keyword_found = True
    
    if (keyword_found == False):
        new_keyword = input("I'm not sure how to respond. What keyword should I respond to?")
        keywords.append(new_keyword)
        new_response = input("How should I respond to" + new_keyword + "?")
        responses.append(new_response)

    user = input("Say something or type bye to quit: ")
    user = user.lower()

print(random.choice(goodbyes))