# alper

YouTube audio/video downloader using yt-dlp.

## Install

```bash
pip install alper
```


## Usage

### CLI

```bash
needmusic https://www.youtube.com/watch?v=JWViInkIAuk
needvideo https://www.youtube.com/watch?v=JWViInkIAuk
```

### Python

```python
pip install alper
from alper import needmusic, needvideo

needmusic("https://www.youtube.com/watch?v=JWViInkIAuk")
needvideo("https://www.youtube.com/watch?v=JWViInkIAuk")
```


## Upload

# python setup.py sdist bdist_wheel
# pip install .whl file ( e.g. "pip install alper-0.1.0-py3-none-any.whl" )
# twine upload dist/*