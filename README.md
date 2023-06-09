# photo-blender

Photo editing experiments with code.

## Development

VS Code profile: [Python](https://github.com/joaopalmeiro/vscode-profiles/tree/main/Python)

```bash
export PIPENV_VENV_IN_PROJECT=1 && pipenv install --dev
```

```bash
pipenv run python blend-gradients.py
```

```bash
pipenv run python blend-multiple-gradients.py
```

```bash
pipenv run python blend-photo-gradation.py
```

```bash
pipenv run python blurify.py
```

```bash
pipenv run python generate-blurhash.py
```

```bash
pipenv run python pixelify.py
```

```bash
pipenv run python sort-pixels.py
```

```bash
pipenv run mypy .
```

## Notes

- `export PIPENV_VENV_IN_PROJECT=1 && pipenv --python 3.7`
- `pipenv install Pillow==9.5.0 && pipenv install --dev black==23.1.0 mypy==1.1.1 ruff==0.0.259`
- `pipenv --rm`
- https://global.canon/en/c-museum/product/ef410.html
- https://github.com/samuelcolvin/python-devtools
- https://github.com/woltapp/blurhash-python
- https://dubblefilm.com/blogs/noticias/the-queen-of-film-soups
- `pipenv install blurhash-python==1.2.0`
- https://github.com/TotallyNotChase/glitch-this:
  - https://github.com/TotallyNotChase/glitch-this/wiki/Documentation:-The-commandline-script
  - `pipx run glitch_this -h`
  - `pipx run glitch_this -s output/output.jpg 2`
  - `pipx run glitch_this -c output/output.jpg 2` or `pipx run glitch_this -c output/output.jpg 2 -f`
- https://github.com/delivrance/glitchart
- https://github.com/satyarth/pixelsort:
  - https://pypi.org/project/pixelsort/
  - `pipenv install pixelsort==1.0.1`
  - https://github.com/satyarth/pixelsort#parameters
  - `pipenv run python -m pixelsort output/output-121027l-6x6.jpg -o output/pixelsort_output-121027l-6x6.png -i random -c 20`
  - `pipenv run python -m pixelsort output/output-121027l-6x6.jpg -o output/pixelsort_output-121027l-6x6.png -i edges -t .5`
  - `pipenv run python -m pixelsort output/output-121027l-6x6.jpg -o output/pixelsort_output-121027l-6x6.png -i edges -t .4`
  - `pipenv run python -m pixelsort output/output-121027l-6x6.jpg -o output/pixelsort_output-121027l-6x6.png -i edges -s saturation`
- https://ffglitch.org/
- https://github.com/rkargon/pixelsorter
- https://github.com/osromusic/Glitch-Arts-Resources
- `pipenv install numpy==1.21.6`
- https://scikit-image.org/docs/stable/auto_examples/edges/plot_canny.html
- https://docs.opencv.org/4.7.0/da/d22/tutorial_py_canny.html
- https://github.com/noelleleigh/glitch_me
- https://www.pyinvoke.org/
- https://github.com/daneah/pixelize
- https://moviebarcode.tumblr.com/
- `IMG_4492.jpg`:
  - First layer (Lightroom):
    - `Light` > `Exposure` > `− 3,00`
    - `Optics` > Enable `Remove Chromatic Aberration`
    - `Geometry` > `Upright` > `Auto`
  - Third layer (Lightroom):
    - B&W
    - `Effects` > `Texture` > `50`
- https://github.com/jkenlooper/pixsaw
- https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/Pillow.md + https://pypi.org/project/types-Pillow/
- `pipenv install --dev types-Pillow==9.5.0.4`
