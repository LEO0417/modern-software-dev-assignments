import fitz  # PyMuPDF
import os

def split_pdf_to_images(pdf_path, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Iterate through pages
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) # Zoom x2 for better quality
        output_file = os.path.join(output_folder, f"page{i+1}.png")
        pix.save(output_file)
        print(f"Saved {output_file}")
    
    print(f"Successfully converted {len(doc)} pages to images in {output_folder}")

if __name__ == "__main__":
    pdf_path = "Antigravity_First_Flight_Guide.pdf"
    output_folder = "Antigravity_Images"
    split_pdf_to_images(pdf_path, output_folder)
