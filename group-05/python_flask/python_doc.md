# APP.py 

__init__()      : Initializing the Flask-Server \
get()           : returns the server status \
post()          : recieve data in bytes -> converting it to string in utf-8 format -> converting in into dictionary format 
                -> get encoded base64 image data -> decode the image -> open and save the image as **request.png**
                 -> calling RunInference('./request.png') from DetectNetConnector class -> returning the response of RunInference as a dictionary

# DetectNetConnector.py

__init__()      : Initializing the constructor of the DetectNetConnector Class \
RunInference(self, img)  : img parameter is the image to be analysed
                          myDetections is a two-Dimensional Array to store the relevant Information about the detected Objects
                          jetson.utils.videoOutput stores the Output. 
                          jetson.utils.loadImage(img) converts the img to a CUDA-image
                          jetson.inference.detectNet('ssd-mobile-v2') loads the Model for the Detection Network
                          
