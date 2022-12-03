from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI() 
 
word = {
}

class NewWord(BaseModel):
    API: str
    Jumbled: str

@app.post("/jumble_word/{word}")
def new_word(words : str, aWord : NewWord):
    seq = len(word)
    inputWord = words
    api = "/jumble_word/" + inputWord
    letters = list(inputWord)
    output = ""
    for num in range(len(letters)): #randomize the input word
        jumbler = random.randrange(0, len(letters))
        temp = letters[num]
        letters[num] = letters[jumbler]
        letters[jumbler] = temp
        output = ''.join(letters).lower()
    word[seq] = api, output
    return output

@app.get("/")
def audit_words():
    ten_items = list(word.items())[-10:]#returns the last 10
    return ten_items
