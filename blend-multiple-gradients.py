# https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html
# https://stackoverflow.com/questions/339007/how-do-i-pad-a-string-with-zeroes

from pathlib import Path

import numpy as np
from PIL import Image

PHOTO_FOLDER: Path = Path("photos/")
PHOTO_IMG: Path = PHOTO_FOLDER / "IMG_4492.jpg"

GRADIENT_FOLDER: Path = Path("gradients/")

OUTPUT_FOLDER: Path = Path("output/")

# ALPHA: float = 0.3
N_RUNS: int = 10

if __name__ == "__main__":
    for n_run in range(1, N_RUNS + 1):
        print(f"Run #{n_run:02}")
        with Image.open(PHOTO_IMG) as photo:
            for gradient_path in GRADIENT_FOLDER.glob("*.png"):
                with Image.open(gradient_path) as gradient:
                    alpha = np.random.random_sample()
                    photo = Image.blend(photo, gradient, alpha)

                    print(f"Gradient: {gradient_path} ({alpha})")

            output_path = OUTPUT_FOLDER / f"gradients-output-run{n_run:02}.jpg"
            photo.save(output_path)

            print(f"Output: {output_path}", end="\n" * 2)

    print("Done!")
