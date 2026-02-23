from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="alper",
    version="0.1.3",
    packages=find_packages(),
    install_requires=["yt-dlp"],
    entry_points={
        "console_scripts": [
            "needmusic=alper:needmusic",
            "needvideo=alper:needvideo",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)