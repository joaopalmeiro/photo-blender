# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
# https://www.geeksforgeeks.org/python-pil-gaussianblur-method/

from pathlib import Path

from PIL import Image, ImageFilter

PHOTO_FOLDER: Path = Path("photos/")
PHOTO_IMG: Path = PHOTO_FOLDER / "IMG_4492.jpg"

OUTPUT_FOLDER: Path = Path("output/")

if __name__ == "__main__":
    with Image.open(PHOTO_IMG) as photo:
        blur_photo = photo.filter(ImageFilter.GaussianBlur(radius=10))

    output_path = OUTPUT_FOLDER / "blur-output.jpg"
    blur_photo.save(output_path)
    print(f"Output: {output_path}")

    print("Done!")
