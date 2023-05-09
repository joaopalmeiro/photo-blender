# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#reading-and-writing-images
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.blend
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize

# from PIL import Image

PHOTO_IMG: str = "photos/"
GRADIENT_FOLDER: str = "gradients/"
OUTPUT_FOLDER: str = "output/"

ALPHA: float = 0.5

if __name__ == "__main__":
    pass
    # with Image.open("output.jpg") as photo, Image.open("output_9x8.png") as gradient:
    #     gradient = gradient.resize((6000, 4000))
    #     print(photo.size)
    #     print(gradient.size)
    #     output = Image.blend(photo, gradient, 0.2)
    #     print(output)
    #     output.save("output-4.jpg")
