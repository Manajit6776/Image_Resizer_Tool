# Batch Image Resizer Tool

A Python script for resizing and converting multiple images in bulk while maintaining aspect ratio. Perfect for preparing images for web, mobile apps, or storage optimization.

## Features

- 🖼️ Batch process all images in a folder
- 📏 Resize to exact dimensions or maximum bounds
- 🔄 Convert between formats (JPEG, PNG, WEBP, etc.)
- ⚖️ Maintain original aspect ratio
- 🎚️ Adjustable quality settings
- 🛠️ Comprehensive error handling
- 📁 Automatic output folder creation

## Installation

1. Ensure you have Python 3.6+ installed
2. Install required packages:
```bash
pip install pillow
```

## Download the script:
https://github.com/Manajit6776/Image_Resizer_Tool/blob/main/image_resizer.py
cd image-resizer

## Usage
### Basic Command
```bash
python image_resizer.py input_folder output_folder width height
```
```bash
python image_resizer.py ./photos ./resized 1200 800
```
### Advanced Options
Option	Description	Example
--format	Output format (JPEG, PNG, etc.)	--format PNG
--quality	JPEG quality (1-100)	--quality 90
--help	Show help message	python image_resizer.py -h
### Practical Examples
Resize for web thumbnails:
```bash
python image_resizer.py originals thumbnails 300 300 --format WEBP
Convert entire folder to high-quality JPEGs:
```
```bash
python image_resizer.py raw_images jpegs 1920 1080 --format JPEG --quality 95
Create mobile-optimized versions:
```
```bash
python image_resizer.py full_size mobile 800 1200 --quality 85
```

## Supported Formats
Input: JPG, JPEG, PNG, BMP, GIF, TIFF, WEBP
Output: All input formats plus format conversion

## Author:
Manajit Mondal
