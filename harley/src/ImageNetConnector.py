import jetson.inference
import jetson.utils

class ImageNetConnector:

    def __init__(self):
        print("init")

    def RunInference(self,img):
        """
            Run ImageNet Inference

            :param img: image to be classified

            :return class_desc: object detected
            :return confidence: classification confidence
        """

	# load image
        image = jetson.utils.loadImage(img)
	
        # load the recognition network
        net = jetson.inference.imageNet("googlenet")

        # classify the image
        class_idx, confidence = net.Classify(image)

        # find the object description
        class_desc = net.GetClassDesc(class_idx)

        return class_desc, confidence
