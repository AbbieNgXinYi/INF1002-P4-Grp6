import os
from moviepy.editor import ImageSequenceClip, AudioFileClip
from PIL import Image

# Function to load images from a folder
def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):  # Sorting ensures the right order
        if filename.endswith(('png', 'jpg', 'jpeg')):
            images.append(os.path.join(folder, filename))
    return images

# Function to resize images to a target resolution
def resize_images(images, target_resolution):
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

# Set the image folder and target resolution (e.g., 1920x1080 for HD video)
image_folder = r'C:\Users\ANG HUI TING\OneDrive\Desktop\Hui Ting\SIT\Year 1 Tri 1\Programming Fundamentals (INF1002)\Project\Images'
images = load_images_from_folder(image_folder)

target_resolution = (1920, 1080)  # Set a fixed resolution for the video (HD)

# Resize all images and get paths of resized images
resized_images = resize_images(images, target_resolution)

# Load background music
music_file = r'C:\Users\ANG HUI TING\OneDrive\Desktop\Hui Ting\SIT\Year 1 Tri 1\Programming Fundamentals (INF1002)\Project\Kevin MacLeod  Sneaky Snitch (1).mp3'
background_music = AudioFileClip(music_file)

# Create the video clip from resized images
clip = ImageSequenceClip(resized_images, fps=0.07)  # 1 frame per second (adjust fps for duration)
final_video = clip.set_audio(background_music)

# Export the final video
output_video_path = r'C:\Users\ANG HUI TING\OneDrive\Desktop\Hui Ting\SIT\Year 1 Tri 1\Programming Fundamentals (INF1002)\Project\output_video.mp4'
final_video.write_videofile(output_video_path, codec='libx264')
