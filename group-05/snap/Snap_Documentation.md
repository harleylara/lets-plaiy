(VideoCapturePicture)
Set Video Capture asks for Permission from the User to access a Video Device.
Set Video Transparancy is set to 0, to correctly display the Video on the Stage.

(SpaceAndForLoop)
When Pressing the "Space"-Key we execute a for-Loop to delete all old Bounding Boxes from previous Detections. After that we switch the Costume to the Stage to see our Camera.

(KeyEnter)
We are waiting for the Enter Key to be pressed.
After that we take a snapshot of the stage and set it to the variable "picture".
Switch to Costume changes the Costume display the "picture"-variable on the Stage.
Set "response" to the JSON-Response of the Server after processing the picture.
Set "objects" the filtered "response"-Variable that contains a List of detected Objects.
Create Bounding Boxes creates new Sprites and inside those, it creates Costumes as Bounding Boxes.

#Custom Blocks

delete Bounding Boxes:
  iterate every Sprite and delete every Sprite which contains "Object" in their name.

response:
  Converting image to Base64
  Sending a POST request to the Flask Server with the Base64 image in a JSON-Format.
  Report Block waits for response.

objects from Jetson:
  Setting Objects to the {'detections' : **detections** }
  
create Bounding Boxes
  Setting x and y to 0
  Looping though all Objects in "objects" we create a new Sprite with the name "Object (i)".
  Draw Box draws the Bouding Box for every Sprite created.
 
new Sprite
  Adds a new Sprite, and renames it afterwards hence naming isnt available in the creation of the sprite.
  Selected Sprite will switch back to the original sprite (sprite[0]) to keep the Scripts Window opened.
  
Draw Box
  Setting Locations for the Bounding Box from the Object. 
  Converting the Locations from Jetson Format (Origin Top Left Corner) to Snap! Format (Origin Middle)
  
  Tell the Sprite to start drawing and set the pen Location to the top Left Corner of the Bounding Box.
   1 = X-Coordinate from Top-Left-Corner
   2 = Y-Coordinate from Top-Left-Corner
   3 = width of the Bounding Box
   4 = Height of the Bounding Box
  The For-Loop draws the box, then we move the pen inside the box by 3 pixel and fill the Box with Transparency 70%.
  After fill we move the pen to the location where we want to write the Name and Confidence.
  Then we write the Name and Round the Number of the Confidence.
  add pentrails to my costume saves the Bounding Box as the Costume
  Switch to costume displays the Bounding Box on top of the picture.
  
