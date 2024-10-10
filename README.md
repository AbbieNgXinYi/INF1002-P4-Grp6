# INF1002-P4-Grp6
## Project Title : Creating a simple video slideshow with music

## Table of Contents
- **[Project Overview](#project-overview)**
- **[Getting Started](#getting-started)**
  - **[Folder and Images and Music file creation](#folder-and-images-and-music-file-creation)**
  - **[Libraries Installation](#libraries-installation)**
  - **[Executing basic program](#executing-basic-program)**
  - **[Choosing your own images and music](#choosing-your-own-images-and-music)**
  - **[Create UI Features](#create-ui-features)**
  - **[Implementing UI features to basic program](#implementing-ui-features-to-basic-program)**
  - **[Synchronisation of video and images](#synchronisation-of-video-and-images)**
  - **[Features](#Features)**
  - **[Enhancements](#Enhancements)**
  - **[Code Overview](#code-overview)**
  - **[To run the application](#to-run-the-application)**
  - **[Demo Video](#demo-video)**
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

Before coding, you must store the images and music you wish to upload into the same folder as the Python code.
Additionally, you will have to create a folder to store a set of images for **Choosing your own images and music**

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
1. Firstly, import the libraries to be used. In our case, we will be using the os, moviepy and PIL libraries.
```import os
from moviepy.editor import ImageSequenceClip, AudioFileClip
from PIL import Image
```

2. Now moving on to retrieving images from a specified folder and filtering them by file types.
```def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):  # Sorting ensures the right order
        if filename.endswith(('png', 'jpg', 'jpeg')):
            images.append(os.path.join(folder, filename))
    return images
```
- sorted(os.listdir(folder)):
  This ensures the images are processed in alphabetical order, which is important for keeping the correct sequence.
  
- filename.endswith(('png', 'jpg', 'jpeg')):
  It filters the files to include only image formats (png, jpg, jpeg).

  3.Next, we resize the images to a defined target resolution (e.g., 1920x1080) to ensure consistent video quality and maintain a uniform aspect ratio across all frames.
```def resize_images(images, target_resolution):
    resized_image_paths = []
    
    for image_path in images:
        img = Image.open(image_path)
        
        # Resize image to the target resolution using the LANCZOS filter
        img = img.resize(target_resolution, Image.Resampling.LANCZOS)
        
        # Save resized image to a new path (or overwrite original if you prefer)
        resized_path = image_path.replace('.jpg', '_resized.jpg').replace('.jpeg', '_resized.jpeg').replace('.png', '_resized.png')
        img.save(resized_path)
        resized_image_paths.append(resized_path)  # Collect the resized images' paths
    
    return resized_image_paths
```
- Image Resizing: 
  For each image, it opens the image file using PIL.Image.open(), resizes it to the target resolution using the LANCZOS filter (which provides high-quality resizing), and saves it with a new filename.

- Image.Resampling.LANCZOS:
  A filter used for downscaling or resizing images with good quality.

- The resized image's path is saved with _resized added to the original filename.

4. Next, create a variable for your image folder and define the path to the folder containing images. 
```image_folder = r'C:\path\to\images\folder'
   images = load_images_from_folder(image_folder)
```
- The load_images_from_folder() function is used to retrieve a list of images.

5. Defining the target resolution
```
target_resolution = (1920, 1080)  # Set a fixed resolution for the video (HD)
```

6. Resizing all images
```
resized_images = resize_images(images, target_resolution)
```
- The list of original image paths is passed to the resize_images() function to resize them to the target resolution.
- The function returns a list of resized image paths, which will be used to create the video.

7. Next, create a variable for your music folder and define the path to the folder containing the audio files. 
```
music_file = r'C:\path\to\audio\file.mp3'
background_music = AudioFileClip(music_file)
```
8. Creating the slideshow video clip
```
clip = ImageSequenceClip(resized_images, fps=0.07)  # 1 frame per second (adjust fps for duration)
```
- The ImageSequenceClip() function from MoviePy creates a video clip from the resized images.
- set the frames per second (FPS) to control how long each image stays on screen. You can adjust the FPS to control the image display duration.

9. Create a variable to load both images and audio file into video clip
```
final_video = clip.set_audio(background_music)
```
- set_audio() is used to add the loaded background music to the video clip.

10. Defining the path to export your video
```
output_video_path = r'C:\path\to\output\output_video.mp4'
final_video.write_videofile(output_video_path, codec='libx264')
```
- The video is exported to an MP4 file using write_videofile().
- Remeber to specify the codec to use for video compression. In this code, we are using 'libx264' as it is widely used for high-quality MP4 videos.

### Choosing your own images and music
**[Back To Top](#back-to-top)**

1. Uploading images module
```
    image_folder = filedialog.askdirectory(title="Select Image Folder")
    if not image_folder:
        return
```

- This defines the file directory of the user which has the images. The user is prompted to enter the directory.
- There is also a return function if the user enters not a folder.

```
    images = load_images_from_folder(image_folder)
    resized_images = resize_images(images, target_resolution)
```

- After the user has defined the file path, the images are resized.

### ------------------------------------------------------------------------------------------------------------------------

2. Uploading mp3 module
```
    music_file = filedialog.askopenfilename(title="Select Music File", filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
    if not music_file:
        return
```

- This defines the file directory of the user which has the mp3. The user is prompted to enter the directory.
- There is also a return function if the user enters not a folder.

```
    background_music = AudioFileClip(music_file)
```
- The user's mp3 is now set as the music for the video 

### Create UI Features 
In this section, we describe the user interface (UI) components developed for the Simple Video Editor application. The UI features aim to enhance user interaction and streamline the video editing process. Key components include:

File Manager Section:
Allows users to upload images and MP3 files.
- Displays lists of uploaded images and audio files for easy management.

Preview Area:
- Displays a preview of the selected image, providing immediate visual feedback.
- Updates automatically when a new image is selected or uploaded.
  
Timeline Visualization:
- Provides a timeline at the bottom of the application showing the sequence of images added for video generation.
- Each image in the timeline is represented visually for quick reference.
  
Audio Waveform Display:
- Visual representation of the audio file's waveform, enhancing user understanding of the audio content.
- Allows users to trim the audio by setting start and end times, with the waveform updating dynamically.
  
Control Buttons:
- Upload Image/MP3: Buttons for uploading media files.
- Delete: Removes selected images or audio files from the lists.
- Clear: Resets all inputs and clears uploaded files.
- Trim Audio: Facilitates trimming of audio segments based on user input.
- Generate MP4: Compiles the uploaded images and audio into a final video output.

**[Back To Top](#back-to-top)**


### Implementing UI features to basic program
This section outlines how the UI features were integrated into the underlying functionality of the Simple Video Editor application.

1. File Upload Functionality:
- Implemented upload_image and upload_mp3 methods to handle file selection via dialogs.
- Used Tkinter's Listbox widget to display and manage uploaded files, ensuring users can easily select and delete items.
  
2. Image Preview:
- Leveraged the PIL library to load and display images in a preview area.
- Implemented thumbnail resizing for optimal display within the UI.
  
3. Audio Waveform Visualization:
- Integrated librosa for audio analysis, allowing for real-time waveform generation based on the uploaded MP3.
- Utilized Matplotlib to plot the waveform and display it within the application.
  
4. Timeline Management:
- Developed a timeline feature that visually represents the sequence of images added to the project.
- Images are added as small thumbnails to a Canvas widget for easy viewing and rearrangement.
  
5. Audio Trimming:
- Implemented functionality to allow users to input start and end times for audio trimming.
- Used the pydub library for audio manipulation, enabling users to save trimmed audio segments.
  
6. Video Generation:
- Utilized the moviepy library to compile images and audio into a single MP4 file.
- Managed synchronization between image duration and audio beats to ensure a cohesive video output.

This documentation provides an overview of the UI components and their integration with the core functionality of the Simple Video Editor application. Users can easily navigate the application and leverage its features for efficient video editing.

**[Back To Top](#back-to-top)**


### Synchronisation of video and images
This project enables the synchronization of images with audio beats, creating engaging video presentations. The application, built using Tkinter, allows users to upload images and MP3 audio files, trim audio segments, and generate a MP4 video that aligns the visual content with the rhythm of the music.

### Features
- **User-Friendly Interface**: Designed with a clean and intuitive layout using Tkinter, making it easy to upload and manage images and audio files.
- **Image and Audio Upload**: Users can upload multiple images and an MP3 file through buttons or drag-and-drop functionality.
- **Audio Trimming**: Users can trim the audio to select specific segments for synchronization.
- **Real-Time Waveform Visualization**: The application displays the audio waveform for better visual reference while editing.
- **Beat Detection**: Utilizing of `librosa` helps to detect beats in the audio track, ensuring that the images displayed are in sync with the music.
- **MP4 Video Generation**: Combines the uploaded images and audio into a final MP4 video that matches the beats.

### Enhancements
- **Video Transitions**: Included fade in and out transitions for the generated mp4 video
- **Scroll bar**: This allows for a more responsive UI design
- **Progress and loading bar**: To show and inform users about the progress of the downloading progress of their mp4 file
- **Saving trimmed mp3 file**: This feature allows users to save their trimmed MP3 file, enabling them to reuse it without needing to trim the original file again.

### Code Overview
The core functionality is implemented in the `FileEditorApp` class, which includes methods for:
- **Uploading Files**: Methods like `upload_image()` and `upload_mp3()` allow users to load their media files into the application.
- **Previewing Media**: Users can preview images and audio waveforms to make informed editing decisions.
- **Trimming Audio**: The `trim_audio()` method allows for specifying start and end times, facilitating precise control over the audio segment used.
- **Beat Tracking**: The `generate_mp4()` method detects beats in the audio file and calculates the duration for which each image should be displayed based on these beats.
- **Generating the Final Video**: After synchronization, the application generates and saves the output video as an MP4 file.

The core functionality is implemented in the `ProgressBarHandler` class, which includes methods for:
- **Progress and loading bar**: the class inlcudes functions like 'emit()' to help ensure progress bar updates

### To run the application
1. Run the application:
``
python your_script.py  # Replace with your actual script name
``
2. Upload images and an MP3 file.
3. Use the trimming feature to specify which part of the audio you want to include.
4. Click "Generate MP4" to create the synchronized video.

**To Note**
Please download these libraries before starting on the code:
- Python 3.x
- Required Libraries:
  - `moviepy`
  - `pydub`
  - `librosa`
  - `matplotlib`
  - `Pillow`
  - `tkinterdnd2`

**[Back To Top](#back-to-top)**

## Demo Video




