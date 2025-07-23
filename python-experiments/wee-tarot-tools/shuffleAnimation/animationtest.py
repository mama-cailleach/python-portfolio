from PIL import Image
import numpy as np
import imageio
import math

# Load card images
card_files = ["card1.png", "card2.png", "card3.png", "card4.png"]
cards = [Image.open(file) for file in card_files]

frames = []
deck_center_x, deck_center_y = 150, 225  # Central point for rotation
radius = 40  # Adjusted for more subtle shuffle motion

# Adjust positioning based on card size
card_width, card_height = 79, 134
initial_offsets = [(i * 8, i * 4) for i in range(len(cards))]  # Based on card size

for t in range(20):  # More frames for smoother movement
    new_frame = Image.new("RGBA", (300, 450), (255, 255, 255, 0))

    for i, card in enumerate(cards):
        angle = (i * 30 + t * 10) % 360  # Dynamic rotation per frame
        x = int(deck_center_x + radius * math.cos(math.radians(angle))) - card_width // 2 + initial_offsets[i][0]
        y = int(deck_center_y + radius * math.sin(math.radians(angle))) - card_height // 2 + initial_offsets[i][1]

        # Rotate naturally, ensuring pivot movement
        rotated_card = card.rotate(angle - 90, expand=True)
        new_frame.paste(rotated_card, (x, y), rotated_card.convert("RGBA"))

    frames.append(new_frame)

# Save as an animated GIF
frames[0].save("circular_shuffle.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)