# https://stackoverflow.com/questions/35374333/create-a-steganographically-hidden-image-with-pillow
# https://note.nkmk.me/en/python-opencv-numpy-alpha-blend-mask/
# https://note.nkmk.me/en/python-numpy-generate-gradation-image/
# https://mdigi.tools/gradient-generator/

from pathlib import Path

import numpy as np
from PIL import Image

PHOTO_FOLDER: Path = Path("photos/")
PHOTO_IMG: Path = PHOTO_FOLDER / "IMG_4492.jpg"
GRADIENT_FOLDER: Path = Path("gradients/")
GRADIENT_IMG: Path = GRADIENT_FOLDER / "135099l-6x6.png"
BASE_FOLDER: Path = Path("bases/")
GRADATION_IMG: Path = BASE_FOLDER / "gradient.jpeg"
OUTPUT_FOLDER: Path = Path("output/")

if __name__ == "__main__":
    with Image.open(PHOTO_IMG) as photo, Image.open(
        GRADIENT_IMG
    ) as gradient, Image.open(GRADATION_IMG) as gradation:
        photo_data = np.array(photo)
        gradient_data = np.array(gradient)

        gradation_mask = np.array(gradation)
        gradation_mask = gradation_mask / 255

        gradation_180_mask = np.array(gradation.transpose(Image.ROTATE_180))
        gradation_180_mask = gradation_180_mask / 255

    output_data = photo_data * gradation_mask + gradient_data * (1 - gradation_mask)
    Image.fromarray(output_data.astype(np.uint8)).save(OUTPUT_FOLDER / "output.jpg")

    output_data = photo_data * gradation_180_mask + gradient_data * (
        1 - gradation_180_mask
    )
    Image.fromarray(output_data.astype(np.uint8)).save(OUTPUT_FOLDER / "output-180.jpg")

    print("Done!")
