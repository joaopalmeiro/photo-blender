# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#reading-and-writing-images
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.blend
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize
# https://stackoverflow.com/a/50557495
# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html:
# - FIND_EDGES for edge detection
# https://docs.python.org/3.7/library/pathlib.html#pathlib.Path.glob

from pathlib import Path

from PIL import Image

PHOTO_FOLDER: Path = Path("photos/")
PHOTO_IMG: Path = PHOTO_FOLDER / "IMG_4492-4.jpg"
GRADIENT_FOLDER: Path = Path("gradients/")
OUTPUT_FOLDER: Path = Path("output/")

ALPHA: float = 0.3

if __name__ == "__main__":
    with Image.open(PHOTO_IMG) as photo:
        # for f in glob.iglob(f"{GRADIENT_FOLDER}/*.png"):
        for gradient_path in GRADIENT_FOLDER.glob("*.png"):
            print(f"Gradient: {gradient_path}")
            with Image.open(gradient_path) as gradient:
                output = Image.blend(photo, gradient, ALPHA)

                output_suffix = gradient_path.stem
                output_path = OUTPUT_FOLDER / f"output-{output_suffix}.jpg"

                output.save(output_path)

                print(f"Output: {output_path}", end="\n" * 2)

    print("Done!")
