## What is it ?

PixelescoPy is an application for Concept Designers and Artists in line with the concept of '30 seconds draw'. Most Concept Artists have a treasure of references, master study or model pose 
libraries on their desktops. Point this application to the folder and set a timer - it would display pictures from the folder (and its subfolders) one after the other at random for <timer> seeconds
. An image  can be skipped if needed. The images displayed would not repeat until all images are exhausted.
    

## Use cases

- Display images from picture library (folders) for study
- Tuneable display duration
- Images displayed  at random
- Images do not repeat
- An image can be skipped
- UI

## Limitations

- No executable package at the moment (Need to follow all the steps in [To run](#to-run) section)
- No UI to enter the folder path and timer (Input section in the code at the moment)
- No back button
- No pause button
- Additional bugs here : https://gitlab.com/ananya26nov/PixelescoPy/-/issues 

## Requirements
- python3
- python3-pip
- ```pip install -r requirements.txt```

## To run
- Open an IDE and clone the project. (I am going with PyCharm here)
    * Download Pycharm : https://www.jetbrains.com/pycharm/download/ 
    * Download Git : https://git-scm.com/downloads
    * Download Python 3.6 : https://www.python.org/downloads/
    * Open PyCharm , Go to VCS > Git > Clone
    * Enter the URL https://gitlab.com/ananya26nov/PixelescoPy.git and local path. Clone.
    * Go to Settings/Preference (Windows/Mac). Select project interpreter  as python (from the  earlier step)
    * In the Terminal type  ```pip install -r requirements.txt```
- In 'base.py'  under the Input section set the folder path and timer
- Run initialize_db.py (one time)
- Run base.py (to run application everytime) 
