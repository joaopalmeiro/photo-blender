# https://theorangeduck.com/page/generating-icons-pixel-sorting

from pathlib import Path

import numpy as np
from PIL import Image

OUTPUT_FOLDER: Path = Path("output/")
PHOTO_FOLDER: Path = Path("photos/")
PHOTO_IMG: Path = PHOTO_FOLDER / "IMG_4492.jpg"

if __name__ == "__main__":
    with Image.open(PHOTO_IMG) as photo:
        photo_data = np.array(photo)

    photo_data_0 = np.sort(photo_data, axis=0)
    photo_data_1 = np.sort(photo_data, axis=1)
    photo_data_2 = np.sort(photo_data, axis=2)

    Image.fromarray(photo_data_0.astype(np.uint8)).save(
        OUTPUT_FOLDER / "sorted-output-0.jpg"
    )
    Image.fromarray(photo_data_1.astype(np.uint8)).save(
        OUTPUT_FOLDER / "sorted-output-1.jpg"
    )
    Image.fromarray(photo_data_2.astype(np.uint8)).save(
        OUTPUT_FOLDER / "sorted-output-2.jpg"
    )

    print("Done!")
