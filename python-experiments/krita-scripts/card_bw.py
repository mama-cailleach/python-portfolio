from krita import *
import os

# Initialize Krita instance
app = Krita.instance()

# Set input/output folders
input_folder = r"D:\Games\Playdate\mama Games\Wee Tarot\source\images\majorArcana"
output_folder = r"D:\Games\Playdate\mama Games\Wee Tarot\source\images\majorArcana\export"

# Define filter settings
filters = [
    {"name": "desaturate", "params": {"mode": "lightness"}},  # Desaturate using Lightness mode
    {"name": "unsharp_mask", "params": {
        "halfSize": 1.39,
        "amount": 99.99,
        "threshold": 0,
        "lightness_only": True
    }}  # Unsharp Mask with your exact settings
]

# Process all image files
image_files = [f for f in os.listdir(input_folder) if f.endswith((".png"))]

for file_name in image_files:
    # Open the image
    doc = app.openDocument(os.path.join(input_folder, file_name))
    app.setActiveDocument(doc)

    # Apply filters
    for filter_data in filters:
        doc.applyFilter(filter_data["name"], filter_data["params"])

    # Save the processed image with the same name
    output_path = os.path.join(output_folder, file_name)
    doc.saveAs(output_path)

    # Close the document
    doc.close()

print("Batch processing completed!")
