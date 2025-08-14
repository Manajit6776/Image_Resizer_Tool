import os
from PIL import Image
import argparse

def resize_images(input_folder, output_folder, width, height, output_format=None, quality=85):
    """
    Resizes all images in the input folder and saves them to the output folder.
    
    Args:
        input_folder (str): Path to folder containing original images
        output_folder (str): Path to save resized images
        width (int): Target width in pixels
        height (int): Target height in pixels
        output_format (str, optional): Desired output format (e.g., 'JPEG', 'PNG')
        quality (int): Quality for JPEG images (1-100)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
    
    for filename in os.listdir(input_folder):
        try:
            filepath = os.path.join(input_folder, filename)

            if not (os.path.isfile(filepath) and filename.lower().endswith(valid_extensions)):
                continue

            with Image.open(filepath) as img:
                print(f"Processing: {filename} ({img.size[0]}x{img.size[1]})")
                
                img.thumbnail((width, height))

                base_name = os.path.splitext(filename)[0]
                if output_format:
                    output_ext = output_format.lower()
                else:
                    output_ext = os.path.splitext(filename)[1][1:]  # Keep original extension
                
                output_filename = f"{base_name}_resized.{output_ext}"
                output_path = os.path.join(output_folder, output_filename)

                save_params = {}
                if output_ext in ['jpg', 'jpeg']:
                    save_params['quality'] = quality
                if output_ext == 'png':
                    save_params['compress_level'] = 6

                img.save(output_path, format=output_format, **save_params)
                print(f"Saved as: {output_filename} ({img.size[0]}x{img.size[1]})\n")
                
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}\n")

def main():
    parser = argparse.ArgumentParser(description='Batch Image Resizer Tool')
    parser.add_argument('input_folder', help='Folder containing images to resize')
    parser.add_argument('output_folder', help='Folder to save resized images')
    parser.add_argument('width', type=int, help='Target width in pixels')
    parser.add_argument('height', type=int, help='Target height in pixels')
    parser.add_argument('--format', help='Output format (e.g., JPEG, PNG)', default=None)
    parser.add_argument('--quality', type=int, help='Quality for JPEG (1-100)', default=85)
    
    args = parser.parse_args()
    
    resize_images(
        args.input_folder,
        args.output_folder,
        args.width,
        args.height,
        args.format,
        args.quality
    )

if __name__ == "__main__":
    main()
