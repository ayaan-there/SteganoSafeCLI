from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="StegosafeCLI",
    version="0.1.0",
    author="Ayaan Usmani",
    author_email="ayaanusmani2005@gmail.com",
    description="A command-line tool for LSB steganography with encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayaan.there/StegosafeCLI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pillow",
        "pycryptodome",
    ],
    entry_points={
        "console_scripts": [
            "stegosafe=stegosafecli.cli:main",
        ],
    },
)