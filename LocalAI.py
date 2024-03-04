import random
import json

#Variables
BotName = "Cortona"
BotNameColon = "Cortona: "

#Greetings and goodbyes
greetings=["Hello!", "What's up!", "Howdy!", "Greetings!"]
goodbyes=["Bye!","Goodbye!","See you later!","See you soon!"]

responseData = json.load(open("response.json", "r"))
dictionaryResponseData = json.load(open("dictionary.json", "r"))

print(BotNameColon + random.choice(greetings) + " My name is Cortona!")


while True :
   
    userinp = input("").lower()
    
    if userinp == "hi" :
        print(BotNameColon + random.choice(greetings))
        continue

    if userinp == "bye" :
        print(BotNameColon + random.choice(goodbyes))
        break
    
    if userinp == "dictionary":
        print(BotNameColon + "Dictionary mode activated, type the word you want to find in english dictionary")
        print(BotNameColon + "Printing whole dictionary")
        print(dictionaryResponseData)
        #while True:
            #if userinp in responseData:
                #print(BotNameColon + dictionaryResponseData[userinp])


    if userinp in responseData :
        print(BotNameColon + responseData[userinp])
        continue
    
    if not userinp in BotNameColon :
        response = input(BotNameColon + "I've never seen this command, how should I respond? ")

    responseData[userinp] = response
    
    f = open("response.json", "w")
    json.dump(responseData, f)


