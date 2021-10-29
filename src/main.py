from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

import io
import base64
import ast

import PIL.Image as Image

import ImageNetConnector as imgNet

app = Flask(__name__)
CORS(app)
api = Api(app)
connector = imgNet.ImageNetConnector()

class JetsonInterface(Resource):

    ROUTE = '/jetson-interface'

    def __init__(self, host='127.0.0.1', port=4040, debug=True, route='/jetson-interface'):
        """
            class constructor

            :param host: set host ip for Flask server
            :param port: set port
            :param debug: set debug mode True or False
            :param route: set base route for Flask server

        """
        self.HOST = host
        self.PORT = port
        self.DEBUG = debug
        self.ROUTE = route

        app.run(host=self.HOST, port=self.PORT, debug=self.DEBUG)

    @app.route(ROUTE, methods=['GET'])
    def get():
        """
            :return: server status
        """
        return 'running'

    @app.route(ROUTE + '/imagenet', methods=['POST']) 
    def post():

        req = request.get_data() # bytes
        req_s = req.decode('utf-8') # convert to string
        req_d = ast.literal_eval(req_s) # convet to dict
        
        image = req_d["image"]
        _, img_encoded = image.split(',')

        # decode image into bytes
        img_decoded = base64.b64decode(img_encoded)
        
        # convert bytes into image
        img = Image.open(io.BytesIO(img_decoded))
        img.save('./request.png')
        
        class_desc, confidence = connector.RunInference('./request.png')
        
        response = { 'class': class_desc, 'confidence': confidence }
        return response

if __name__ == '__main__':

    api.add_resource(JetsonInterface)
    JetsonInterface(host='0.0.0.0')
