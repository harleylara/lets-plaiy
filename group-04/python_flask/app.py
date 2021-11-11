########  imports  ##########
from flask import Flask, jsonify, request, render_template
import base64
from flask_restful import Api, Resource

import ImageNetConnector as imgNet

import ast
import io
import PIL.Image as Image

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api=Api(app)

connector=imgNet.ImageNetConnector()

class JetsonInterface(Resource):
	ROUTE='/jetson-interface'
	def __init__(self,host='0.0.0.0',port=80, debug=True,route='jetson-interface'):
		self.HOST=host
		self.PORT=port
		self.DEBUG=debug
		self.ROUTE=route
		
		app.run(host=self.HOST, port=self.PORT,debug=self.DEBUG)

	@app.route(ROUTE, methods=['GET'])
	def get():
		return 'running'

	@app.route(ROUTE+'/imagenet',methods=['POST'])
	def post():
		req=request.get_data()
		req_s=req.decode('utf-8')
		req_d=ast.literal_eval(req_s)
		image=req_d["image"]
		_, img_encoded=image.split(',')
		img_decoded=base64.b64decode(img_encoded)
		
		img=Image.open(io.BytesIO(img_decoded))
		img.save('./request.png')
		
		class_desc,confidence=connector.RunInference('./request.png')
		response={ 'class':class_desc, 'confidence':confidence }
		return response
if __name__=='__main__':
	api.add_resource(JetsonInterface)
	JetsonInterface(host='0.0.0.0', port=80)

