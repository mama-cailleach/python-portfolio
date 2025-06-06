from krita import Krita
import os

# Initialize the Krita instance
app = Krita.instance()

# Set input and output folder paths (use raw strings for Windows paths)
input_folder = r"D:\Games\Playdate\mama Games\Wee Tarot\source\images\majorArcana"
output_folder = r"D:\Games\Playdate\mama Games\Wee Tarot\processed_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Gather image files with supported extensions
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".png", ".jpg"))]

for filename in image_files:
    file_path = os.path.join(input_folder, filename)
    
    # Open the document and set it active
    doc = app.openDocument(file_path)
    app.setActiveDocument(doc)
    
    # Retrieve the active layer; if none, use the first top-level node
    layer = doc.activeNode()
    if layer is None:
        nodes = doc.topLevelNodes()
        if nodes:
            layer = nodes[0]
        else:
            print(f"Skipping {filename}: no valid layer found.")
            doc.close()
            continue

    # -----------------------
    # Apply Desaturate Filter
    # -----------------------
    desatFilter = app.filter('desaturate')
    desatConfig = desatFilter.configuration()
    
    # Set the filter to use the "lightness" method for conversion
    desatConfig.setProperty('mode', 'lightness')
    desatFilter.setConfiguration(desatConfig)
    
    # Apply the desaturation filter to the entire layer
    desatFilter.apply(layer, 0, 0, doc.width(), doc.height())
    doc.refreshProjection()

    # -----------------------
    # Apply Unsharp Filter
    # -----------------------
    unsharpFilter = app.filter('unsharp')
    unsharpConfig = unsharpFilter.configuration()
    
    # Set your desired properties for unsharp filtering
    unsharpConfig.setProperty('amount', 99.99)
    unsharpConfig.setProperty('halfSize', 1.39)
    unsharpConfig.setProperty('lightnessOnly', True)
    unsharpConfig.setProperty('threshold', 0)
    unsharpFilter.setConfiguration(unsharpConfig)
    
    # Apply the unsharp filter to the same layer
    unsharpFilter.apply(layer, 0, 0, doc.width(), doc.height())
    doc.refreshProjection()

    # -----------------------
    # Save and Close the Document
    # -----------------------
    output_path = os.path.join(output_folder, filename)
    doc.saveAs(output_path)
    doc.close()

print("Batch processing (desaturation and unsharp mask) completed!")
