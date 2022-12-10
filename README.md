# Multiple Object Tracker

Multi-object tracker project developed by Juan Porta for the Epic IO challenge.

## Description

This project is a multi-object tracking system that was developed using the OpenCV library tracking tools. It is intended to be run using Docker.

## Usage

The Dockerfile is located in the service folder, along with the requirements file. After building the image, we can run the project from terminal as follows:

```bash
docker run image-name
```

You can set the video input path, the path to the initial bounding boxes, the video output path, and the model to use:

```bash
docker run image-name --pathvideo=/input/video --pathjson=/bboxes/json --output=/output/video --trackmodel='csrt'
```

You can also choose to view the frame processing progress:

```bash
docker run image-name --processframe
```

To consult the help (to see in detail arguments, model options, etc):

```bash
docker run image-name --help
```
