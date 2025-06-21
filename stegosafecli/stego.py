"""
Steganography functions for LSB encode/decode in PNG/BMP images.
"""
from PIL import Image

DELIMITER = '####'

def _int_to_bin(rgb):
    # Ensure rgb is a tuple of ints
    return tuple(format(int(c), '08b') for c in rgb)

def _bin_to_int(rgb):
    return tuple(int(b, 2) for b in rgb)

def hide_message(input_path, output_path, message):
    img = Image.open(input_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    encoded = img.copy()
    width, height = img.size
    message += DELIMITER
    data = ''.join(format(ord(i), '08b') for i in message)
    data_len = len(data)
    idx = 0
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if not isinstance(pixel, tuple) or len(pixel) != 3:
                pixel = (0, 0, 0)
            pixel = [int(c) for c in pixel]
            for n in range(3):
                if idx < data_len:
                    pixel[n] = pixel[n] & ~1 | int(data[idx])
                    idx += 1
            encoded.putpixel((x, y), tuple(pixel))
            if idx >= data_len:
                break
        if idx >= data_len:
            break
    if idx < data_len:
        raise ValueError('Message too large for image.')
    encoded.save(output_path)

def reveal_message(stego_path):
    img = Image.open(stego_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    width, height = img.size
    bits = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if not isinstance(pixel, tuple) or len(pixel) != 3:
                continue
            for n in range(3):
                bits.append(str(int(pixel[n]) & 1))
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(''.join(byte), 2))
        chars.append(char)
        if ''.join(chars).endswith(DELIMITER):
            break
    message = ''.join(chars).replace(DELIMITER, '')
    return message
