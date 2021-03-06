# Face detection using OpenCV and precompiled dataset

# Requirements
- Webcam or a videofeed (testvideo included in repo)
- Python3
- OpenCV (developed using v4.0.0)
- pip
- virtualenv


## Setup virtual environment
Use your prefered virtual environment, this will set it up with virtualvenv and pip.

Install **pip** and **virtualvenv** for Arch Linux:
```bash
sudo pacman -S python-pip python-virtualenv
```

Initialize environment:
```bash
python3 -m venv /path-to-directory
```

Change directory into environment and activate it
```bash
cd /path-to-directory
source bin/activate
pip install -r requirements.txt
```

Exit virtualvenv
```bash
deactivate
```

## Ressouces
* Test video [david.webm](media/david.webm) can be found [here](https://github.com/opencv/opencv_extra/blob/master/testdata/cv/tracking/david/data/david.webm)

* Cascades training data used: [haarcascade_profileface.xml from OpenCV](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_profileface.xml)

* [Tutorial on face reconization](https://docs.opencv.org/4.0.1/db/d28/tutorial_cascade_classifier.html)

* [Vehicle detection with Haar Cascades](https://github.com/andrewssobral/vehicle_detection_haarcascades)

* [Video capture tutorial](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html)

## What I learned

* Its pretty easy to create a face reconition software. I found a pre-made public dataset which made it quite easy to set the whole thing up.
* The better quality the dataset is, the better recognition the program will have
