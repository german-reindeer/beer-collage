import os
import glob
from PIL import Image

resize_size = 128
row_count = 32
collage_size = resize_size * row_count

def resize_image(file_name):
    im = Image.open(file_name)
    width, height = im.size
    crop_size = height if width > height else width
    left = (width - crop_size)/2
    top = (height - crop_size)/2
    right = (width + crop_size)/2
    bottom = (height + crop_size)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    return im.resize((resize_size, resize_size))

def get_all_files():
    return glob.glob("./picture/*.jpg")

def main():
    files = get_all_files()
    resized_files = list(map(resize_image, files))
    new = Image.new("RGBA", (collage_size,collage_size))
    
    for x in range(row_count):
        for y in range(row_count):
            new.paste(resized_files[(x * row_count + y) % 119], (x * resize_size,y * resize_size))

    new.show()

main()
