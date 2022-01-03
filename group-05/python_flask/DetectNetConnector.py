import jetson.inference
import jetson.utils

class DetectNetConnector:
    

    def __init__(self):
        print("init")
       

    def RunInference(self,img):
        """
            Run ImageNet Inference

            :param img: image to be classified

            :return class_desc: object detected
            :return confidence: classification confidence
        """
        myDetections =[]
        output = jetson.utils.videoOutput('./image.png')
	# load image
        image = jetson.utils.loadImage(img)
	
        # load the recognition network
        net = jetson.inference.detectNet("ssd-mobilenet-v2")


        # classify the image
        detections = net.Detect(image)
        output.Render(image)
        for detection in detections:
                myDetections.append([net.GetClassDesc(detection.ClassID),detection.Confidence])
        
       
        return myDetections
