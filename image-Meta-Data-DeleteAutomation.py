import os
from PIL import Image

def delete_metadata(image_path):
    with Image.open(image_path) as img:
        data = list(img.getdata())
        img_without_metadata = Image.new(img.mode, img.size)
        img_without_metadata.putdata(data)
        img_without_metadata.save(image_path)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(folder_path, filename)
            delete_metadata(file_path)
            print(f"Processed: {filename}")

folder_path = 'PATH'  # Change this to your folder path
process_folder(folder_path)
