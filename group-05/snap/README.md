# Verison.2_01.xml
![VideoCapture](/group-05/snap/Screenshots/VideoCapture.png)  \
***Set Video Capture*** asks for permission from the user to access a video device. \
***Set Video Transparancy*** is set to "0" to correctly display the video on the stage.
___
![Full](/group-05/snap/Screenshots/Full.png) \
We will break down this codeblock into sections below. 
___
![SpaceAndForLoop](/group-05/snap/Screenshots/SpaceAndForLoop.png) \
Press the "Space"-key to execute a for-loop to delete all old bounding boxes from previous detections. \
Switch the costume to the stage to see the camera.
___
![EnterPressed](/group-05/snap/Screenshots/EnterPressed.png) \
Press the "Enter"-key to continue. \
Take a snapshot of the stage and set it to the variable "picture" \
Switch to costume changes the costume to display the "picture"-variable on the stage \
Set "response" to the JSON-response of the server after processing the picture. \
Set "objects" to the filtered "response"-variable that contains a list of detected objects \
Create bounding boxes creates new sprites and inside those, it creates costumes as bounding boxes

https://user-images.githubusercontent.com/39634776/155811691-c4b5f971-dbdb-47cf-9349-b31a84b3dbc3.mp4


# Custom Blocks
## Delete Bounding Boxes
![DeleteBoundingBoxes](/group-05/snap/Screenshots/DeleteBoundingBoxes.png) \
Iterate every sprite and delete each sprite that contains "Object" in their name

## Response
![Response](/group-05/snap/Screenshots/Response.png) \
Converting image to base64 \
Send a POST-request to the Flask-server with the base64 image in a JSON-format \
Report block waits for response
  
## Objects From Jetson
![ObjectsFromJetson](/group-05/snap/Screenshots/ObjectsFromJetson.png) \
Setting objects to the detections part of {'detections' : ***detections***}

## Create Bounding Boxes
![CreateBoundingBoxes](/group-05/snap/Screenshots/CreateBoundingBoxes.png) \
Setting "x"- and "y"-coordinates to "0" \
Looping though all objects in "objects" to create a new sprite with the name "Object (i)".
Draw Box draws the bounding box for every sprite created.
  
## New Sprite
![NewSprite](/group-05/snap/Screenshots/NewSprite.png) \
Adds a new sprite and renames it afterwards, because naming isnt possible in the creation of the sprite \
Selected sprite will switch back to the original sprite (sprite[0]) to keep the scripts window opened \
  
## Draw Box
![DrawBox](/group-05/snap/Screenshots/DrawBox.png) \
Setting locations for the bounding box from the object \
Converting the locations from Jetson-format (origin: top-left-corner) to Snap!-format (origin: center) \
  
Tell the sprite to start drawing and set the pen location to the top-Left-corner of the bounding box \
1 = "X"-coordinate from top-left-corner \
2 = "Y"-coordinate from top-left-corner \
3 = width of the bounding box \
4 = height of the bounding box \
The for-loop draws the box, then the pen moves inside the box by 3 pixels and fills the box with a transparency of 70% \
The pen moves to the another location to write the name and confidence \
Confidence is rounded before writing \
Add pentrails to my costume saves the bounding box as the costume \
Switch to costume displays the bounding box on top of the picture
  
