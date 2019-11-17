#Open Innovation
#IDEA
Conversion of what we see into an audio-only environment for Blind and visually impaired that will actually allow them to interact as if they had eyes.

##WORKING
Our AI based System built with the aim of completely revolutionizing the lifestyle of the visually impaired will consist of a wearable with a camera attached to it. 
The Pi will send this real-time data frame by frame to our web application. The web application will do basically three things, all at the same time.
Firstly, it utilizes neural networks to generate captions for the frames obtained. 
It is done by first encoding the image into a fixed-length vector representation and then decoding the representation into natural language description. 
The image encoder is a deep convolutional neural network and is used for object recognition and detection. 
The decoder is a long short-term memory (LSTM) network trained as a language model conditioned on the image encoding.
Words in the captions generated above are represented with an embedding model. 
Each word in the vocabulary is associated with a fixed-length vector representation that is learned during training. We will implement the state of the art Show and Tell Model.


Thirdly, it will do a face analysis on the picture to find familiar faces in the surroundings using a Deep learning algorithm which will use pictures of known people scraped from the user's Twitter/Facebook account. 
Thus, there will not only be information like - "There is a man in front of you"; but it will also have information on who the person is.
Now, as the server will use Flask-ASK, the data obtained from the step above will be converted to speech output using Amazon Alexa. For any object that the user can interact with, Alexa will ask the user if he/she wants to interact with it or not. 
The user's answer will then be analyzed and depending on the answer required information will then be provided to the user through speech.
