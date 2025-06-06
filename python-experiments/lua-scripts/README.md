# Lua Scripts – Text-to-Lua Dictionary Automation

This folder contains helper scripts related to Lua scripting for game development workflows.

## Overview

The current script in this folder is designed to automate the conversion of text data—typically exported or organized from Excel—into a Lua dictionary (table) format. This makes it easier to integrate game data (such as localization strings, configuration, or game content) directly into your Lua-based games or tools.

### Key Features

- **Excel/Text to Lua Table:**  
  Converts structured text files (e.g., CSV or tab-separated values from Excel) into properly formatted Lua dictionary scripts.
- **Game-Ready Output:**  
  Ensures output is ready to be included as a Lua module or data file for use in your game code.

## How to Use

1. Prepare your text file (CSV, TSV, or similar) with the data you want to convert.
2. Run the provided script, specifying your input file.
3. The script will output a `.lua` file containing the equivalent Lua dictionary/table.
4. Import this generated file into your Lua project as needed.

> **Tip:**  
> Adjust the script as necessary to match your specific text file formatting and the structure required by your game.

## Example Use Case

- Quickly convert dialogue, localization, or configuration data from Excel sheets into Lua tables for use in games.

---

*Created by [mama-cailleach](https://github.com/mama-cailleach) to streamline data integration for game projects.*
