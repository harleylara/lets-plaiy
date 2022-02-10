# APP.py

Function | Description
--- | ---
__init__() | Initializing the Flask-Server
get() | Returns the server status
post() | Receive data in bytes 
->  | Converting it to a string in UTF-8 format
->  | Converting in into dictionary format
->  | Get encoded base64 image data
->  | Decode the image
->  | Open and save the image as **request.png**
->  | Calling RunInference('./request.png') from DetectNetConnector class
->  | Returning the response of RunInference as a dictionary

# DetectNetConnector.py

Function | Description
--- | ---
__init__() | Initializing the constructor of the DetectNetConnector Class 
RunInference(self, img) | "img" parameter is the image to be analysed
-> | "myDetections" is a two-dimensional array to store the relevant information about the detected objects 
-> | "jetson.utils.videoOutput" stores the output. 
-> | "jetson.utils.loadImage(img)" converts the img to a CUDA-image (jetson-Format).
-> | "inference.detectNet('ssd-mobile-v2')" loads the model for the detection-network and creates a list of detected objects from "net.Detect(image)"
-> | Loop through all detections in the list and filter the Information into a new custom list with only the necessary information (ClassDescription, Confidence, Top, Bottom, Left, Right) and returning the custom detection list
