# LSB (Least Significant Bit) steganography


#LSB Encode (Hide Message in Image)

from PIL import Image
import numpy as np

def hide_message_lsb(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = np.array(img)

    # Convert message to binary and add delimiter
    message += '###'  # Delimiter to indicate end of message
    bin_msg = ''.join([format(ord(c), '08b') for c in message])
    
    flat_data = data.flatten()

    if len(bin_msg) > len(flat_data):
        raise ValueError("Message too long to hide in this image.")

    # Modify the LSB of each pixel byte
    for i in range(len(bin_msg)):
        flat_data[i] = (flat_data[i] & ~1) | int(bin_msg[i])

    # Reshape and save stego image
    stego_data = flat_data.reshape(data.shape)
    stego_img = Image.fromarray(stego_data.astype('uint8'), 'RGB')
    stego_img.save(output_path)
    print(f"Message hidden in '{output_path}'.")

# LSB Decode (Extract Message from Image)

def extract_message_lsb(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = np.array(img).flatten()

    bits = [str(pixel & 1) for pixel in data]
    chars = [chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars)

    # Stop at delimiter
    end_index = message.find('###')
    if end_index != -1:
        message = message[:end_index]
    else:
        print("Warning: Delimiter not found.")
    
    print(f"Extracted message: {message}")
    return message


# Hide message
hide_message_lsb('cover.png', 'Hello LSB!', 'stego.png')

# Extract message
extract_message_lsb('stego.png')


