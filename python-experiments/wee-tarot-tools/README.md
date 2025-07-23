# Lua Script – Text-to-Lua Dictionary Automation

This folder contains helper scripts related to Lua scripting for game development workflows.

## Overview

The scripts in this folder demonstrate how to automate the conversion of structured text data (typically exported or organized from Excel) into Lua dictionary (table) format. These scripts showcase the structure and base of how I used Python to transform CSV files into Lua-ready scripts for my game Wee Tarto.

> **Note:**  
> The files here are not the full production files used in the game. They were adapted and changed during testing to illustrate the workflow and underlying approach. They are provided as reference for structure and automation methods.

### Key Features

- **Excel/Text to Lua Table:**  
  Converts structured text files (e.g., CSV or tab-separated values from Excel) into properly formatted Lua dictionary scripts.
- **Game-Ready Output:**  
  Ensures output is ready to be included as a Lua module or data file for use in your game code.
- **Modular Structure:**  
  Scripts are organized to facilitate easy adaptation for different data formats and game requirements.

## How to Use

1. Prepare your text file (CSV, TSV, or similar) with the data you want to convert.
2. Run the appropriate Python script in this folder, specifying your input file.
3. The script will output a `.lua` file containing the equivalent Lua dictionary/table.
4. Import this generated file into your Lua project as needed.

> **Tip:**  
> Adjust the script as necessary to match your specific text file formatting and the structure required by your game.

## Example Use Case

- Quickly convert dialogue, localization, or configuration data from Excel sheets into Lua tables for use in games.
- Use as a template for building your own automation workflows for data integration in Lua projects.

---

*Created by [mama-cailleach](https://github.com/mama-cailleach) to streamline data integration for game projects.  
Wee Tarot repository link coming soon.*
