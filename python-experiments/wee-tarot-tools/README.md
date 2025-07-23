# Wee Tarot Tools

This directory contains helper scripts and experimental tools used for **asset generation** and **data automation** for my Playdate game, **Wee Tarot**.

It is a development playground for visual prototyping, spritesheet creation, and automating the conversion of card data into Lua tables, so I can quickly test, tweak, and integrate new tarot deck content and shuffle animations.

---

## Contents

### 1. **shuffleAnimation/**
> Python scripts for visual prototyping and asset generation of tarot card shuffle animations.

- **Purpose:**  
  Test and tweak shuffle effects, export animated `.gif` previews, and generate `.png` spritesheets for use in the game.
- **Highlights:**  
  - Circular shuffling, hand shuffling, card scaling, fan spreads, and explosive finales.
  - All scripts are iterative and experimental—expect hardcoded parameters and image filenames.
- **See:** [`shuffleAnimation/README.md`](./shuffleAnimation/README.md) for a breakdown of each script and usage instructions.

### 2. **generate_card_data/**
> Python script for automating the conversion of structured tarot card data (from CSV/Excel) into Lua tables.

- **Purpose:**  
  Streamline the process of turning Excel/CSV card descriptions, keywords, and correspondences into Lua dictionaries ready for import in Wee Tarot.
- **Highlights:**  
  - Parses card data from CSV files
  - Outputs Lua script files (tables) for direct use in Playdate/Lua projects
  - Easily adaptable for other card sets or formats
- **See:** [`generate_card_data/README.md`](./generate_card_data/README.md) for step-by-step instructions and details.

---

## How to Use

1. **Install Dependencies**
   - Most scripts require:
     - [Pillow](https://python-pillow.org/) (`pip install pillow`)
     - [numpy](https://numpy.org/) (`pip install numpy`)
     - [imageio](https://imageio.github.io/) (`pip install imageio`)
   - For data scripts, standard Python CSV handling (no extra packages needed).

2. **Prepare Assets**
   - For **shuffleAnimation**: Place card images (e.g., `Card01.PNG`, ...) in the script directory.
   - For **generate_card_data**: Prepare your CSV file with the required columns (see subdirectory README).

3. **Run Scripts**
   - Each script is independent; see the subdirectory README for usage and details.

4. **View Results**
   - Preview `.gif` animations, use `.png` spritesheets in your game, and import generated Lua table files.

---

## Why These Tools?

- Rapid prototyping for game feel and tarot deck visuals
- Quick conversion of design data into code-ready formats
- Streamlined asset creation for Playdate game development
- All code is **experimental** and subject to change, meant for creative iteration!

---

Made with ♥ by [mama-cailleach](https://github.com/mama-cailleach) for Wee Tarot.
