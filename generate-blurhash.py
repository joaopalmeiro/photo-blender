# https://github.com/woltapp/blurhash-python/blob/v1.2.0/src/blurhash/__init__.py#L32
# https://github.com/woltapp/blurhash-python/blob/v1.2.0/src/blurhash/__init__.py#L60
# https://gitlab.com/joaommpalmeiro/blurhashify/-/blob/main/blurhashify/cli.py
# https://github.com/woltapp/blurhash-python#usage

import blurhash
from PIL import Image

BASE_IMG: str = "bases/135099l.jpg"
OUTPUT_FOLDER: str = "gradients"

X_COMPONENTS: int = 6
Y_COMPONENTS: int = 6
WIDTH: int = 6000
HEIGHT: int = 4000

if __name__ == "__main__":
    with Image.open(BASE_IMG) as base:
        hash = blurhash.encode(
            base, x_components=X_COMPONENTS, y_components=Y_COMPONENTS
        )
        print(f"BlurHash string: {hash}")

    output_img = blurhash.decode(hash, width=WIDTH, height=HEIGHT, punch=1)
    output_img.save(
        f"{OUTPUT_FOLDER}/135099l-{X_COMPONENTS}x{Y_COMPONENTS}.png", format="PNG"
    )

    print("Done!")
