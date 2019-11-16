from flask import Flask
from flask_ask import Ask, statement, question, session
import traceback
import random
import os
import requests
import logging
import time
import json
import subprocess
import face_recognition

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

app = Flask(__name__)
ask = Ask(app, '/')

""" These functions handle what are essentially the beginning and end of the main use case of the skill."""
@ask.launch
def start_session():
    return question("Please Wait. Processing...")


@ask.intent('DescribeWorldIntent')
def speaknext():
    choice = [
        "There's",
        "Okay. Lets see what can I see for you now. I see ",
        "I see in front of you",
        "Now I can see "
    ]
    result = subprocess.getoutput(
        'curl -F "image=@imgcptn/png/example.jpeg" -X POST http://localhost:5000/model/predict')
    result = result.split('{', 1)[1]
    result = "{" + result
    res = json.loads(result)
    speechstring = res["predictions"][0]["caption"]
    return question(speechstring)


@ask.intent('WantPersonNames')
def speakpersonname():
    picture_of_me = face_recognition.load_image_file("me.jpeg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
    unknown_picture = face_recognition.load_image_file("unknown.jpeg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    # Now we can see the two face encodings are of the same person with `compare_faces`!
    results = face_recognition.compare_faces(
        [my_face_encoding], unknown_face_encoding)
    if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")
    return question("Please Wait. Processing...")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
