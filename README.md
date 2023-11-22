# Parking AI

We're making an AI model that can recognize how many cars are on the parking at VIVES Brugge.


## Table of Contents
- [The plan](#the-plan)
- [Model](model)
- [How to Use](#how-to-use)

## The plan

The plan is to use a Raspberry Pi 4 together with a Raspberry Pi High Quality Camera. 

We will use this camera to take a picture every 30 seconds and count how many cars are in the picture.

Since the camera will not be moving we know how many parking spots are in frame.

After counting the cars we subtract the amount of parking spots by how many cars we counted to get a result of how many spots are still open.

## Model

We are going to retrain the pretrained YOLO-model to focus on cars in a parking lot.

YOLO (You Only Look Once) is an advanced Object Detection model that, hence the name, only looks at the picture once and then goes through the network once and detects objects.

## How to Use

TODO
