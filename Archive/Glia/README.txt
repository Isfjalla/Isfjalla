Introduction:

API's written explained: 

POST "/jumble_word/{word}"

Takes an input {word} and randomizes it.

GET "/"

Displays the last 10 calls and the payload

Requirements:
Python 3.9.x or above
Uvicorn 0.18.3 or above

Run:

docker build -t fastapi-jumble-audit:0.1 . 

docker run -p 8000:80 --name fast-jump fastapi-jumble-audit:0.1

