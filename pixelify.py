# https://pythonprogramming.altervista.org/pixelize-an-image-with-pil-and-python/
# https://towardsdatascience.com/convert-photo-into-pixel-art-using-python-d0b9bd235797

from pathlib import Path

from PIL import Image

OUTPUT_FOLDER: Path = Path("output/")
PHOTO_FOLDER: Path = Path("photos/")
PHOTO_IMG: Path = PHOTO_FOLDER / "IMG_4492.jpg"

if __name__ == "__main__":
    with Image.open(PHOTO_IMG) as photo:
        # small_photo = photo.resize((128, 128), resample=Image.BILINEAR)
        # small_photo = photo.resize((8, 8), Image.BILINEAR)
        # small_photo = photo.resize((8, 8))
        # small_photo = photo.resize((256, 256))

        resize_size = (int(photo.width / 40), int(photo.height / 40))
        print(f"Photo resize size: {resize_size}")

        small_photo = photo.resize(resize_size, Image.BILINEAR)

        output = small_photo.resize(photo.size, Image.NEAREST)

    output.save(OUTPUT_FOLDER / f"pixel-output-{resize_size[0]}x{resize_size[1]}.jpg")

    print("Done!")
