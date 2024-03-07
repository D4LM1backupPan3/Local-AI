import random
import json

#Name
BotName = "Cortona"
BotNameColon = "Cortona: "

#Info
Version = 0.001
LastDateUpdated = "3/6/2024"
Dev = "D4LM"
GithubLink = "https://github.com/D4LM1backupPan3/Local-AI"

#Greetings and goodbyes
greetings=["Hello!", "What's up!", "Howdy!", "Greetings!"]
goodbyes=["Bye!","Goodbye!","See you later!","See you soon!"]

responseData = json.load(open("response.json")) 
dictionaryResponseData = json.load(open("dictionary.json", "r"))

print(BotNameColon + random.choice(greetings) + " My name is Cortona!")


while True :
   
    userinp = input("").lower()
    
    if userinp == "hi" :
        print(BotNameColon + random.choice(greetings))
        continue

    if userinp == "bye":
        print(BotNameColon + random.choice(goodbyes))
        break
    
    if userinp == "botInfo":
        print(BotNameColon + "Version: " + Version)
        print(BotNameColon + "The last date I updated this bot: " + LastDateUpdated)
        print(BotNameColon + "The developer is " + Dev)
        print(BotNameColon + "Link to the Github: " + GithubLink)
    
    #Systeminfo module
        

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
    
    if not userinp in responseData:
        response = input(BotNameColon + "I've never seen this command, how should I respond? ")
        responseData[userinp] = response
        f = open("response.json", "w")
        json.dump(responseData, f)