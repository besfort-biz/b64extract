# Base64 Asset Extractor (B64Extract)

## Overview

**Base64 Asset Extractor** is a Python-based tool designed to scan HTML files for base64-encoded assets such as images and fonts, extract them, and save them as individual files. It then replaces the base64 strings in the HTML with file references, making the code cleaner and easier to manage.

## Features

- Extracts base64-encoded images (PNG, JPEG, JPG, GIF, SVG, WebP) and fonts (WOFF, WOFF2, TTF, OTF) from HTML.
- Automatically saves the assets in a designated folder.
- Updates the original HTML file with correct file paths instead of base64 data.
- Supports a wide range of file formats including image/webp.
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/besfort-biz/b64extract.git
   cd b64extract
2.Rename the html file with base64 data as index.html and run the app.
    ```bash
    python3 app.py

3.Data are scrapped and put in a folder assets in current dir, while on cleaned_index.html the data are now written as filenames, put the cleaned html file inside asset folder and all in one folder.
