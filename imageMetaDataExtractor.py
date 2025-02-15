from PIL import Image
from PIL.ExifTags import TAGS
import os

def get_image_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image.getexif()
        metadata = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
        return metadata
    except Exception as e:
        print(f"Error reading metadata from {image_path}: {e}")
        return None

def process_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)
            metadata = get_image_metadata(image_path)
            if metadata:
                print(f"Metadata for {filename}:")
                for tag, value in metadata.items():
                    print(f"  {tag}: {value}")
                print("-" * 30)

# Specify the directory containing your images
image_directory = "PATH"

# Process the images in the specified directory
process_images_in_directory(image_directory)
