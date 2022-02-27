# General Info
This project aims to use Sanp! as interface for Object Detection on Jetson Nano.

Flask server running on Jetson Nano for communication.

# Setup
## Jetson Nano
- Use Command Line to clone the directory on Jetson Nano
  ```bash
  git clone https://github.com/harleylara/lets-plaiy
  ```
- Navigate to python folder
   ```bash
  cd ~/lets-plaiy/group-05/python_flask
  ```
- Use command below to run flask server on Jetson Nano
    ```bash
    sudo python3 APP.py
  ```
- Note your IP address. IP address is needed for `Response` block in Snap!
## Snap!
- Open file __Verison.2_01.xml__ with Snap!
- Enable _JavaScript extentions_ from settings
- Edit `Response` block to write your IP address

![Response](/group-05/snap/Screenshots/Response.png)
