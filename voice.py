from flask import Flask
from flask_ask import Ask, statement, question, session
import traceback
import random
import os
import requests
import logging
import time
import json

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

app = Flask(__name__)
ask = Ask(app, '/')

""" These functions handle what are essentially the beginning and end of the main use case of the skill."""
@ask.launch
def start_session():
    while 1:
        if (alexaready.fetchStatus('/captionready') == 1):
            caption = fetchcaption.fetchCaption()
            choice = [
                "I'm glad that I can help you. I see",
                "Glad to be of some help. There's",
                "I see in front of you"
            ]
            alexaready.setStatus('captionready', 0)
            return question(random.choice(choice)+' '+caption+' Is there anything else I can do for you?')
        else:
            return question("Please Wait. Processing...")


@ask.intent('DescribeWorldIntent')
def speaknext():
    choice = [
        "There's",
        "Okay. Lets see what can I see for you now. I see ",
        "I see in front of you",
        "Now I can see "
    ]
    files = {
        'image': ('imgcptn/png/example.jpeg', open('imgcptn/png/example.jpeg', 'rb')),
    }
    response = requests.post(
        'http://localhost:5000/model/predict', files=files)
    json_data = json.loads(response.text)
    print(json_data)
    return question("Hello")


@ask.intent('WantPersonNames')
def speakpersonname():
    if (alexaready.fetchStatus('/peopleready') == 1):
        personnames = fetchperson.fetchCaption()

        print(personnames)
        if(personnames != '0'):
            choice = [
                "I see "
            ]
            print(personnames)
            alexaready.setStatus('peopleready', 0)
            return question(random.choice(choice)+' '+personnames+' You might want to say hi to them.')
        else:
            alexaready.setStatus('peopleready', 0)
            return question("I am sorry but I believe that I do not recognize anyone here")
    else:
        return question("Please Wait. Processing...")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
