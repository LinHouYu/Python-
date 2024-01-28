import os
import shutil
from PIL import Image

def classify_images(image_directory, destination_folder_4k, destination_folder_1):
    for filename in os.listdir(image_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = Image.open(os.path.join(image_directory, filename))
            width, height = image.size

            if width > 3000 and height > 2000:
                destination_folder = destination_folder_4k
            else:
                destination_folder = destination_folder_1

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.copy2(os.path.join(image_directory, filename), os.path.join(destination_folder, filename))


classify_images(r"C:\Users\zhish\Downloads", r"C:\Users\zhish\Downloads\4k", r"C:\Users\zhish\Downloads\1")
