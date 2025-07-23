# shuffleAnimation

This directory contains various Python scripts and experiments focused on generating animated card shuffle effects and sprite sheets for my Playdate game, **Wee Tarot**.

## Purpose

All code here was used for **testing and tweaking visual shuffle animations**, mainly by generating `.gif` previews and `.png` spritesheets for use in-game. The scripts let me quickly iterate on card movement, stacking, spreading, scaling, and other effects before exporting assets for Wee Tarot.

## Contents

- **animationtest.py**  
  Circular shuffle animation for a small deck; generates a `.gif` preview showing cards rotating around a central point.

- **handshuffle/scale_spritesheet_gif_generator.py**  
  Animates a single card being scaled and shifted, exporting both a `.gif` animation and a horizontal `.png` spritesheet of the frames.

- **handshuffle/shuffle_gif_generator.py**  
  Simulates hand shuffling by lifting and restacking selected cards with staggered timing; exports a `.gif` preview.

- **handshuffle/shuffle_spritesheet_generator.py**  
  Similar to above but exports a full horizontal spritesheet `.png` for use in Playdate, plus a `.gif` preview.

- **handshuffle/shuffle_spritesheet_generator_16cards.py**  
  Animates one card drifting and spinning out of a 16-card deck, layering it beneath the top cards; outputs a spritesheet and `.gif`.

- **handshuffle/shuffle_spritesheet_generator_spread.py**  
  Simulates a fancy spread/fan and explosive finale with flipping/rotation and random explosion vectors; exports a `.png` spritesheet and `.gif` preview.

## Usage

1. **Install dependencies**  
   Most scripts require:
   - [Pillow](https://python-pillow.org/) (`pip install pillow`)
   - [numpy](https://numpy.org/) (`pip install numpy`)
   - Some use [imageio](https://imageio.github.io/) (`pip install imageio`)

2. **Prepare card images**  
   Place your card images (e.g., `Card01.PNG`, ...) in the same directory as the scripts. File names should match those referenced in the scripts.

3. **Run scripts**  
   Each script can be run independently:
   ```bash
   python animationtest.py
   python handshuffle/scale_spritesheet_gif_generator.py
   # ...etc
   ```

   Outputs are saved as `.gif` previews and/or `.png` spritesheets in the current or `exports/` directory.

4. **View/Use Results**  
   Open the generated `.gif` files to preview the animation. Use the `.png` spritesheets in your Playdate game or wherever needed.

## Note

This folder is **experimental** and contains lots of iterative code for visual prototyping. Expect some hardcoded paths, parameters, and image filenames. It's intended as a working playground for animation ideas rather than polished, general-purpose tools.

---

Made with ♥ by [mama-cailleach](https://github.com/mama-cailleach) for Wee Tarot.
