message = ""


def sentenceMaker(inputStr):
    # firstChar = inputStr[0]
    # inp = inputStr.lstrip(firstChar)
    # return firstChar.upper()+inp

    return inputStr.capitalize()

def isQuestion(inputStr):
    # isQuestion = False
    # for que in ("how", "what", "why", "where", "which", "when"):
    #     if inp.lower().__contains__(que):
    #         isQuestion = True
    #         break
    # return isQuestion

    return inputStr.startswith(("how", "what", "why", "where", "which", "when"))

def formatString(inputStr):
    if isQuestion(inputStr) == True:
        inp = inputStr + "?"
    else:
        inp = inputStr + "."

    return sentenceMaker(inp)


results = []
while True:
    inp = input("Say something: ")
    if inp == "\end":
        break
    else:
        results.append(formatString(inp))



print(" ".join(results))