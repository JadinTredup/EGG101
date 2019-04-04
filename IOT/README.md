# Thingspeak IOT application

## Purpose
The purpose of this code is to create an easy-to-use application which could route sensor data from an Arduino plugged in via a serial port to a Thingspeak IOT cloud server.

## Downloading and Installing the Code
This application does not require any package installation because it has been bundled up into an executable files using pyinstaller. The source code is still provided however so that interested students can see how it functions. These steps assume that you have already created a thingspeak account, a channel, and a single field set up. If this is not the case, please scroll further down for instructions on setting this up.

### Step 1: Download the repository
Download the whole repository from the home page, or just download this individual directory. This repository has multiple modules as part of the EGG101 Freshman Engineering Seminar so if you do not need all of them, this one folder should be enough.

### Step 2: Run the Executable
Open the 'Executables' file and select the file with your operating system in the name. Double click on the executable and the application should run.

### Step 3: The Information Window
The first window requires four pieces of information to start:
1. The Channel ID # which can be found right underneath the channel name.
2. The Write API key.
3. The Read API key.
4. The Com port which the arduino is connected to.

### Step 4: Broadcast Data to Cloud
After hitting "Submit" on the information window, the executable will start broadcasting data to the cloud. It does not display any output, but if you log into Thingspeak and view the channel you can watch it receive data.
