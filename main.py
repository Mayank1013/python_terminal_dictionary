import json
import difflib as dl
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(dl.get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Press Y if yes and N is no:" % dl.get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[dl.get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "This word does not exist in this dictionary"
        else:
            return "We did not understand"
    else:
        return "We did not understand the word"


word = input("Enter the word : ")


def printdef():
    if type(output) == list:
        for item in output:
         print(item)
    else:
         print(output)


output = translate(word) 
printdef()