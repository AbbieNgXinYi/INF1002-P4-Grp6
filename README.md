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
upload_image(self)
```
   
- Firstly the module will define the file path of the pictures.
```
file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
```

- The user will be shown which path was chosen (to see if uploaded wrong one)
```
print(f"Image uploaded: {file_path}")
```

- The file path is then referenced by the other modules so they can work with the images.
```
self.file_listbox.insert(tk.END, f"Image: {os.path.basename(file_path)}")
self.preview_image(file_path)
self.add_image_to_timeline(file_path)
```
The modules in order are:
- The listbox module for displaying the images and music
- The module for previewing images on the timeline
- The module that displays the images in the timeline

2. Uploading mp3 module
```
upload_mp3(self)
```
- Firstly the module will define the file path of the pictures.
```
file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
```

- The user will be shown which path was chosen (to see if uploaded wrong one)
```
print(f"MP3 uploaded: {file_path}")
```
- The file path is then referenced by the other modules so they can work with the mp3.
```
self.file_listbox.insert(tk.END, f"MP3: {os.path.basename(file_path)}")
self.preview_mp3(file_path)
```
The modules in order are:
- The listbox module for displaying the images and music
- The module for previewing music on the timeline



### Create UI Features 
**[Back To Top](#back-to-top)**


### Implementing UI features to basic program
**[Back To Top](#back-to-top)**


### Synchronisation of video and images to beat
**[Back To Top](#back-to-top)**


