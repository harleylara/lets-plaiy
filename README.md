# Let's Plaiy

**⚠ REPOSITORY UNDER DEVELOPMENT ⚠**

Let's Pl**ai**y, is a project being developed at **[Rhein-Waal University of Applied Sciences](https://www.hochschule-rhein-waal.de/en)** in the interdisciplinary project (IP 17, WS 2021). The aim of the project is to develop, design and implement teaching materials on _artificial intelligence_ (AI) for schools.

It is intended to use deep learning models powered by [NVIDIA Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit) computers and [Snap!](https://snap.berkeley.edu/), a programming environment to facilitate interaction with the deep learning models.

More information on the [project wiki](https://wiki.eolab.de/doku.php?id=ip:ws2021:lets_plaiy:start).

## Implementation

At the moment the implementation is intended for a single image sent from Snap! to the Jetson Nano using a Restful API.

So far only the image classifier **ImageNet** from the [Jetson inference] repository (https://github.com/dusty-nv/jetson-inference) has been implemented.

## Usage

On the Jetson Nano a server is running using Flask, which has as input path to the API `http://ip_address:4040/jetson-interface`.

If the service is running it responds `running`.

To use the **ImageNet** model the image must be encoded in Base64 format, the request must be in `JSON` format and the path `http://ip_address:4040/jetson-interface/imagenet`.

Format of the request:

```json
{
	¨image¨: "data:image/png;base64,iVBORw0KGgoAAAAN..."
}
```

In the `src` folder you will find the application code, and in the `snap-projects` folder you will find an example project called `hello-ai-world.xml` and a simple custom block `get-stage-base64` to get the Stage of Snap! encoded in base64.

## Setup Jetson Nano

To use the NVIDIA models, the [jetson inference](https://github.com/dusty-nv/jetson-inference) repository must be build from the source.

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

## Python3 Dependencies

The server is based on Flask and requires some dependencies to be installed:

- Flask
- Flask-Restful
- Flask-Cors
- Pillow

```bash
$ pip3 install Flask flask-restful flask-cors Pillow requests
```

## Get Snap!

Usually if you use Snap! from the official website CORS problems arise, so for the moment it is recommended to use a local version of Snap!

```bash
cd ~
git clone https://github.com/jmoenig/Snap
cd Snap
```

To use Snap! with an http server you can use the following command.

```bash
python3 -m http.server
```
