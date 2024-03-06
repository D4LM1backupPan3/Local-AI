import random
import json

#Variables
BotName = "Cortona"
BotNameColon = "Cortona: "

#Greetings and goodbyes
greetings=["Hello!", "What's up!", "Howdy!", "Greetings!"]
goodbyes=["Bye!","Goodbye!","See you later!","See you soon!"]

responseData = json.load(open("response.json")) 
dictionaryResponseData = json.load(open("dictionary.json", "r"))
chessOpeningDictionaryResponseData = json.load(open("chessOpeningsEco.json", "r"))

print(BotNameColon + random.choice(greetings) + " My name is Cortona!")


while True :
   
    userinp = input("").lower()
    
    if userinp == "hi" :
        print(BotNameColon + random.choice(greetings))
        continue

    if userinp == "bye":
        print(BotNameColon + random.choice(goodbyes))
        break
    
    #Dictionary module

    if userinp == "dictionary":
        Word = input(BotNameColon +"Put Word here (Undercase only for now):")
        if Word in dictionaryResponseData:
            print(BotNameColon + dictionaryResponseData[Word])
            continue
        else:
            print(BotNameColon + "Can't find word definition(If you need to add it, go to the end of the .json and add it)")
            continue

    if userinp == "dictionary.dump":
        print(dictionaryResponseData)
        continue

    #Chess dictionary module
    if userinp == "chess":
        openingName = input(BotNameColon + "Put Word here (Undercase only for now):")
        if openingName in chessOpeningDictionaryResponseData:
            print(BotNameColon + chessOpeningDictionaryResponseData[openingName])
            continue
        else:
            print(BotNameColon + "Can't find opening (If you need to add it, go to the end of the .json and add it)")
            continue

    

    if not userinp in responseData:
        response = input(BotNameColon + "I've never seen this command, how should I respond? ")
        responseData[userinp] = response
        f = open("response.json", "w")
        json.dump(responseData, f)