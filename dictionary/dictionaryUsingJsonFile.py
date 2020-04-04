import json
import difflib as dl

dataFile = json.load(open("data.json"))
dataFileWords = dataFile.keys()


def translate(userInput):
    userInput = userInput.lower()
    # if dataFileWords.__contains__(userInputWord):
    if userInput in dataFileWords:
        return dataFile.get(userInput)
    elif userInput.title() in dataFileWords:
        return dataFile.get(userInput.title())
    elif userInput.upper() in dataFileWords:
        return dataFile.get(userInput.upper())
    elif len(dl.get_close_matches(userInput, dataFileWords)) > 0:
        suggestion = dl.get_close_matches(userInput, dataFileWords)[0]
        userOption = input("Did you mean %s instead? if yes enter Y else enter N: " % suggestion).lower()
        if userOption == 'y':
            return dataFile.get(suggestion)
        elif userOption == 'n':
            return "The word doesn't exists, Please double check it"
        else:
            return "We don't understand your input"
    else:
        return "The word doesn't exists, Please double check it"


userInputWord = input("Enter a word: ")
output = translate(userInputWord)
if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)
