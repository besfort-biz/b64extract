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
