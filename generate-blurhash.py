# https://github.com/woltapp/blurhash-python/blob/v1.2.0/src/blurhash/__init__.py#L32
# https://github.com/woltapp/blurhash-python/blob/v1.2.0/src/blurhash/__init__.py#L60
# https://gitlab.com/joaommpalmeiro/blurhashify/-/blob/main/blurhashify/cli.py
# https://github.com/woltapp/blurhash-python#usage

from pathlib import Path

import blurhash
from PIL import Image

BASE_FOLDER: Path = Path("bases/")
BASE_IMG: Path = BASE_FOLDER / "135628l.jpg"

OUTPUT_FOLDER: Path = Path("gradients/")

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

    output_prefix = BASE_IMG.stem
    output_path = OUTPUT_FOLDER / f"{output_prefix}-{X_COMPONENTS}x{Y_COMPONENTS}.png"

    output_img.save(output_path, format="PNG")
    print(f"Output: {output_path}", end="\n" * 2)

    print("Done!")
