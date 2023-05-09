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

## Notes

- `export PIPENV_VENV_IN_PROJECT=1 && pipenv --python 3.7`
- `pipenv install Pillow==9.5.0 && pipenv install --dev black==23.1.0 mypy==1.1.1 ruff==0.0.259`
