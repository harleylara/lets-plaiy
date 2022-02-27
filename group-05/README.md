# General Info
This project aims to use Sanp! as interface for Object Detection on Jetson Nano.

Flask server running on Jetson Nano for communication under the address:
`http://ip_address:4040/jetson-interface`

# Requirements
 ## Jetson Nano
  - Built in [jetson inference](https://github.com/dusty-nv/jetson-inference) repository on Jetson Nano
    ```bash
    $ sudo apt-get update
    $ sudo apt-get install git cmake libpython3-dev python3-numpy
    $ git clone --recursive https://github.com/dusty-nv/jetson-inference
    $ cd jetson-inference
    $ mkdir build
    $ cd build
    $ cmake ../
    $ make -j$(nproc)
    $ sudo make install
    $ sudo ldconfig
    ```
- Python3 Dependencies

  The server is based on Flask and requires some dependencies to be installed:

  - Flask
  - Flask-Restful
  - Flask-Cors
  - Pillow

  ```bash
  $ pip3 install Flask flask-restful flask-cors Pillow requests
  ```
## Snap!
   It is recommended to use offline version of Snap! for avoiding potential CORS problems
   ```bash
cd ~
git clone https://github.com/jmoenig/Snap
cd Snap
```
# Setup
## Jetson Nano
- Note your IP address. IP address is needed for `Response` block in Snap!. 
Command below will give IP adress of your device
  ```bash
  ifconfig -a
  ```
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
## Snap!
- Open file __Verison.2_01.xml__ with Snap!
- Enable _JavaScript extentions_ from settings
- Edit `Response` block to write your IP address

![Response](/group-05/snap/Screenshots/Response.png)
