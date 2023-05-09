# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#reading-and-writing-images
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.blend
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize
# https://stackoverflow.com/a/50557495
# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html:
# - FIND_EDGES for edge detection

import glob

from PIL import Image

PHOTO_IMG: str = "photos/IMG_4492-4.jpg"
GRADIENT_FOLDER: str = "gradients/"
OUTPUT_FOLDER: str = "output"

ALPHA: float = 0.3

if __name__ == "__main__":
    with Image.open(PHOTO_IMG) as photo:
        for f in glob.iglob(f"{GRADIENT_FOLDER}/*.png"):
            print(f)
            with Image.open(f) as gradient:
                output = Image.blend(photo, gradient, ALPHA)
                output.save(f"{OUTPUT_FOLDER}/output.jpg")

    print("Done!")
