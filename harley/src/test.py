import requests

"""
Test file:
    Send base64 encoded image
"""

URL = 'http://0.0.0.0:4040/jetson-interface/imagenet'

image_encoded = open('orange_encoded.txt', 'r')
img = image_encoded.read()
req = {'image': img}

resp = requests.post(URL, json=req)

print(resp.text)
