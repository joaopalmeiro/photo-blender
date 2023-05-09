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
pipenv run python generate-blurhash.py
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
