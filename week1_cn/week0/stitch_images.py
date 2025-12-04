import os
from PIL import Image

def stitch_images_vertically(image_paths, output_path):
    if not image_paths:
        print("No images to stitch.")
        return

    images = [Image.open(path) for path in image_paths]
    
    # Calculate dimensions
    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)
    
    # Create new blank image
    combined_image = Image.new('RGB', (max_width, total_height), (255, 255, 255))
    
    current_y = 0
    for img in images:
        # Center the image if it's smaller than max_width (optional, but looks better)
        x_offset = (max_width - img.width) // 2
        combined_image.paste(img, (x_offset, current_y))
        current_y += img.height
        
    combined_image.save(output_path)
    print(f"Saved {output_path}")

def main():
    base_dir = "/Users/leowang/github/modern-software-dev-assignments/week1_cn/week0"
    images_dir = os.path.join(base_dir, "slides_images")
    
    # Define groups by page numbers
    # Group 1: 1-5
    # Group 2: 6-9
    # Group 3: 10-13
    groups = [
        range(1, 6),
        range(6, 10),
        range(10, 14)
    ]
    
    for i, page_range in enumerate(groups):
        image_paths = []
        for page_num in page_range:
            filename = f"page{page_num}.png"
            path = os.path.join(images_dir, filename)
            if os.path.exists(path):
                image_paths.append(path)
            else:
                print(f"Warning: {path} not found.")
        
        if image_paths:
            output_filename = f"long_image_{i+1}.png"
            output_path = os.path.join(base_dir, output_filename)
            stitch_images_vertically(image_paths, output_path)

if __name__ == "__main__":
    main()
