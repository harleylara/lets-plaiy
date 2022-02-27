import jetson.inference
import jetson.utils

#load the recognition network
net = jetson.inference.detectNet("ssd-mobilenet-v2")

class DetectNetConnector:
    

    def __init__(self):
        print("init")

    def RunInference(self,img):
        """
            Run detectNet 

            :param img: image to be detected

            :return myDetections : list of detected objects
        """

	# load image
        image = jetson.utils.loadImage(img)


        # classify the image
        myDetections =[]
        detections = net.Detect(image)
        

        for detection in detections:
                myDetections.append([net.GetClassDesc(detection.ClassID),detection.Confidence,round(detection.Top),round(detection.Bottom),round(detection.Left),round(detection.Right)])
        
       
        return myDetections
