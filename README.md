# INF1002-P4-Grp6
## Project Title : Creating a simple video slideshow with music

## Table of Contents
- **[Project Overview](#project-overview)**
- **[Getting Started](#getting-started)**
  - **[Folder and Images and Music file creation](#folder-and-images-and-music-file-creation)**
  - **[Libraries Installation](#libraries-installation)**
  - **[Executing basic program](#executing-basic-program)**
  - **[Create UI Features](#create-ui-features)**
  - **[Implementing UI features to basic program](#implementing-ui-features-to-basic-program)**
---
## Project Overview
This project is a Python-based application that enables users to create simple video slideshows by combining images and music. The goal of the project is to offer an intuitive and user-friendly interface that mimics key features found in video editing platforms, allowing users to easily organize images and background music into a cohesive video slideshow.

## Getting Started
**[Back To Top](#back-to-top)**

- Creating your folders
- Libraries installation
- Step by step execution guide

### Folder and Images and Music file creation
**[Back To Top](#back-to-top)**


### Libraries Installation
**[Back To Top](#back-to-top)**
#### 1. Moviepy
Description:  Python library used for video editing and manipulation. It allows you to create, modify, and process videos, audio files, and images programmatically. 

Installation: In the terminal, type: 
```bash
pip install moviepy
```

#### 2. Pillow
Description: A powerful imaging library in Python, used for opening, manipulating, and saving many different image file formats. It's the modern fork of the original PIL (Python Imaging Library).

Installation: In the terminal, type:
```bash
pip install pillow
```

#### 3. pydub
Description: A simple and easy-to-use library for manipulating audio files. It allows for tasks like slicing, concatenating, and exporting audio in various formats.

Installation: In the terminal, type:
```bash
pip install pydub
```

#### 4. tkinterdnd2
Description: An extension of Tkinter that adds drag-and-drop functionality, enabling users to drag files directly into the application window.

Installation: In the terminal, type:
```bash
pip install tkinterdnd2
```

#### 5. matplotlib
Description: A comprehensive library for creating static, animated, and interactive visualizations in Python. It's used here for visualizing audio waveforms.

Installation: In the terminal, type:
```bash
pip install matplotlib
```

#### 6. numpy
Description: A fundamental package for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them.

Installation: In the terminal, type:
```bash
pip install numpy
```

#### 7. ffmpeg
Description: While not a Python library, ffmpeg is essential for handling audio and video processing tasks in moviepy and pydub. It needs to be installed separately and should be accessible via your system's PATH.

Installation (Varies for different Operating Systems):

**Windows:**
Step 1: Download the FFmpeg Zip Package
- Go to the FFmpeg official website.
- Scroll down to the Get packages & executable files section.
- Under the Windows tab, click on the link to Windows builds from gyan.dev.
- Download the ffmpeg-release-essentials.zip file from the "Essentials Builds" section.

Step 2: Extract the FFmpeg Files
- Navigate to the folder where the .zip file was downloaded.
- Right-click on the file and select Extract All or use a tool like 7-Zip.
- Choose a location to extract the files. For simplicity, extract it to C:\ffmpeg.

Step 3: Add FFmpeg to the System PATH
This step allows you to use FFmpeg from any folder in the command prompt.
- Open the Start Menu and search for Environment Variables.
- Click on Edit the system environment variables.
- In the System Properties window, click on the Environment Variables button.
- Under the System variables section, find the variable named Path and click Edit.
- Click New and add the path to the bin folder where FFmpeg is extracted (e.g., C:\ffmpeg\bin).
- Click OK to close all windows.

Step 4: Verify the Installation
- Open the Command Prompt by typing cmd in the Start Menu and pressing Enter.
- Type ffmpeg -version and press Enter.
- If FFmpeg is installed correctly, you'll see details about the FFmpeg version.

**MacOC:**
Step 1: Install Homebrew (if not installed)
- Open the Terminal app.
- - Install Homebrew by pasting this command and pressing Enter:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- Follow the on-screen instructions to complete the installation.

Step 2: Install FFmpeg with Homebrew
- Once Homebrew is installed, install FFmpeg by running this command in the terminal:
```bash
brew install ffmpeg
```

Step 3: Verify the Installation
**After the installation completes, check if FFmpeg is installed correctly by running:**
```bash
ffmpeg -version
```
- You should see information about the FFmpeg version, build, and configuration if the installation is successful.

#### Verifying Installations
After installing, you can verify that all libraries are correctly installed by running the following Python script:
```Python
import moviepy
import PIL
import pydub
import tkinterdnd2
import matplotlib
import numpy
print("All libraries are successfully installed!")
```
If no errors are raised, your environment is set up correctly to run the Simple Video Editor UI application.

### Executing basic program
**[Back To Top](#back-to-top)**


### Create UI Features 
**[Back To Top](#back-to-top)**


### Implementing UI features to basic program
**[Back To Top](#back-to-top)**


### Synchronisation of video and images to beat
**[Back To Top](#back-to-top)**


