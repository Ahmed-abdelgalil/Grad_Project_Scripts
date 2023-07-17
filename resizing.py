from PIL import Image
import os
import multiprocessing
import fnmatch

""" Resize all images to specific size in order to train using YOLOV8"""

# Set directory path
directory = " "
#define image extensions in dataset
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.PNG', '*.JPEG']  

# Set maximum allowed width and height
max_size = 640

# Iterate through files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if any(fnmatch.fnmatch(filename, ext) for ext in image_extensions):
        # Open the image file using PIL
        image_path = os.path.join(directory, filename)
        with Image.open(image_path) as img:
            # Get the size of the image
            width, height = img.size
            # Check if the image is larger than the maximum allowed size
            if width > max_size or height > max_size:
                # Calculate the new size based on the maximum allowed size
                new_width = max_size
                new_height = int(height * max_size / width) if width > height else max_size
                # Resize the image
                img = img.resize((new_width, new_height))
                # Save the resized image
                img.save(image_path)



