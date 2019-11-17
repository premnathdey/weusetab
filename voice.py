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
    result = subprocess.getoutput(
        'curl -F "image=@imgcptn/png/example.jpeg" -X POST http://localhost:5000/model/predict')
    result = result.split('{', 1)[1]
    result = "{" + result
    res = json.loads(result)
    speechstring = res["predictions"][0]["caption"]
    return question(speechstring)


@ask.intent('WantPersonNames')
def speakpersonname():
    directory = os.fsencode("knownpeople")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpeg"):
            picture_of_me = face_recognition.load_image_file(
                "knownpeople/"+filename)
            my_face_encoding = face_recognition.face_encodings(picture_of_me)[
                0]
            unknown_picture = face_recognition.load_image_file(
                "imgcptn/png/example.jpeg")
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[
                0]
            # Now we can see the two face encodings are of the same person with `compare_faces`!
            results = face_recognition.compare_faces(
                [my_face_encoding], unknown_face_encoding)
            if results[0] == True:
                sentence = "I can see " + os.path.splitext(filename)[0]
                print(sentence)
                return question(sentence)
        else:
            return question("Nobody known was found")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
