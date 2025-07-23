# Lua Script – Text-to-Lua Dictionary Automation

This folder contains helper scripts related to Lua scripting for game development workflows.

## Overview

The main script in this folder, `generate_card_data.py`, demonstrates how to automate the conversion of structured card data from a CSV file (such as one exported from Excel) into a Lua dictionary (table) format. This workflow showcases the structure and base of how Python was used to transform CSV files into Lua-ready scripts for my game Wee Tarto.

> **Note:**  
> The files here are not the full production files used in the game. They were adapted and changed during testing to illustrate the workflow and underlying approach. They are provided as reference for structure and automation methods.

## Directory Structure

```
python-experiments/lua-scripts/generate_card_data/
├── README.md
├── generate_card_data.py
├── textfiles_19_06.xlsx
├── pentacles_data.csv (...)
├── export/
│   └── cardDescriptionsPentacles.lua (...)
```

## How It Works

- **Input:**  
  The script expects a CSV file (e.g., `pentacles_data.csv`) containing card data. Each row should include the following columns:
  - `Card Name`
  - `Upright Fortune`
  - `Reversed Fortune`
  - `Upright Keywords`
  - `Reversed Keywords`
  - `Correspondence`

- **Transformation:**  
  The script parses each row, handling multiple lines and keywords (split by delimiters like `|` and `;`). It builds a structured Python dictionary for each card, then generates a Lua table string.

- **Output:**  
  The resulting Lua script (e.g., `cardDescriptionsPentacles.lua`) is written to the `export/` directory. The Lua file is ready to be imported into your Lua-based game project.

## How to Use

1. Prepare your CSV file (`pentacles_data.csv`) with the required columns listed above.
2. Run the Python script:
    ```bash
    python generate_card_data.py
    ```
3. The script will create an `export/` directory (if it doesn't exist) and output `cardDescriptionsPentacles.lua` containing the Lua dictionary/table.
4. Import or require the generated Lua file in your Lua project as needed.

> **Tip:**  
> You can adjust the input CSV file name and the output path in the script to match your needs. The script is modular, allowing adaptation for other card sets or data formats.

## Example Use Case

- Quickly convert card descriptions, keywords, and correspondences from Excel or Sheets into Lua tables for use in games.
- Use as a template for building your own automation workflows for data integration in Lua projects.

---

*Created by [mama-cailleach](https://github.com/mama-cailleach) to streamline data integration for game projects.  
Wee Tarot repository link coming soon.*
