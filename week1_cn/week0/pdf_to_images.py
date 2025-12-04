import os
import fitz  # PyMuPDF

def convert_pdf_to_images(pdf_path, output_folder):
    # Check if PDF exists
    if not os.path.exists(pdf_path):
        print(f"Error: File {pdf_path} not found.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    # Open the PDF
    doc = fitz.open(pdf_path)
    print(f"Opened {pdf_path}, found {len(doc)} pages.")

    for i, page in enumerate(doc):
        # Render page to an image (pixmap)
        # zoom_x and zoom_y set the resolution. 2.0 is usually good quality (approx 144 dpi if base is 72)
        zoom = 2.0 
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        # Define output filename
        # Page numbers start at 1 as per user request "page1"
        output_filename = f"page{i+1}.png"
        output_path = os.path.join(output_folder, output_filename)
        
        # Save image
        pix.save(output_path)
        print(f"Saved {output_path}")

    print("Conversion complete.")

if __name__ == "__main__":
    base_dir = "/Users/leowang/github/modern-software-dev-assignments"
    pdf_file = os.path.join(base_dir, "week1_cn/week0/AI编程工坊_Python核心工具入门.pdf")
    output_dir = os.path.join(base_dir, "week1_cn/week0/slides_images")
    convert_pdf_to_images(pdf_file, output_dir)
