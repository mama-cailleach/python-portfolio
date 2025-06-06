# Krita Scripts – Image Automation for Game Development

This folder contains Python scripts for automating image editing tasks in [Krita](https://krita.org/en/). These were originally created to streamline asset creation for a tarot game project for Playdate, but are designed to be broadly useful for automating repetitive image operations in future game development workflows.

## Overview

- **Purpose:**  
  Automate and batch image/layer operations in Krita to speed up game asset production and reduce manual work.
- **Use Cases:**  
  - Bulk exporting or processing of layers and images  
  - Automated resizing, cropping, and compositing  
  - Applying filters and property-based adjustments
  - Generating consistent assets for game engines or consoles

## Features

- **Flexible Filtering:**  
  Scripts include a `filters_properties` feature that can retrieve and display all available properties you can use for filtering or processing layers/images. This makes it easy to discover and leverage Krita's scripting capabilities for your needs.

- **Batch Processing:**  
  Most scripts are designed to handle multiple files, layers, or images at once—ideal for large-scale asset production.

- **Reusable for Any Game Project:**  
  While inspired by a tarot game, these scripts are generic and adaptable for any game or digital art workflow.

## How to Use

1. Open Krita.
2. Go to `Tools > Scripts > Scripter` to open the Python scripting panel.
3. Load and run the desired script from this folder.
4. Adjust file paths, layer names, and parameters as needed for your project.
5. Use the `filters_properties` feature to list all properties you can filter or modify in your automation.

> **Tip:**  
> Always back up your work before running batch scripts!

## Scripts

- Each script includes comments (in English or Portuguese) explaining its function and usage.
- Example operations:
  - Export all visible layers as PNGs
  - Batch resize/export images to platform specs
  - Filter and process layers by property (using the `filters_properties` tool)
  - Apply automated effects or color adjustments

## Contributions

Feel free to adapt, extend, or contribute new automation scripts!

---

*Created by [mama-cailleach](https://github.com/mama-cailleach) as part of ongoing game dev and digital art workflow automation.*
