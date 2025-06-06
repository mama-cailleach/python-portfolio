from krita import Krita
import os

# Initialize the Krita instance
app = Krita.instance()

# Define input and output folders (use raw strings for Windows paths)
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

    # Retrieve the active layer; if missing, use the first top-level node.
    layer = doc.activeNode()
    if layer is None:
        nodes = doc.topLevelNodes()
        if nodes:
            layer = nodes[0]
        else:
            print(f"Skipping {filename}: no valid layer found.")
            doc.close()
            continue

    # Create and configure the desaturate filter:
    # (This follows the documentation example using application.filter instead of creating a filter layer.)
    desatFilter = app.filter('desaturate')
    desatConfig = desatFilter.configuration()

    # (Optional) Print available properties:
    # print(desatConfig.properties())

    # Configure the filter to use "lightness" mode.
    desatConfig.setProperty('mode', 'lightness')
    desatFilter.setConfiguration(desatConfig)

    # Apply the filter to the entire layer
    desatFilter.apply(layer, 0, 0, doc.width(), doc.height())
    # Refresh to ensure changes are rendered
    doc.refreshProjection()

    # Save the processed image in the output folder with the same filename.
    output_path = os.path.join(output_folder, filename)
    doc.saveAs(output_path)

    # Close the document to free resources
    doc.close()

print("Batch desaturation completed!")
