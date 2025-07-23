from PIL import Image
import numpy as np
import os

# === Constants ===
canvas_width, canvas_height = 400, 240
card_width, card_height = 174, 300
num_cards = 16
total_frames = 60
drift_index = 7  # Card that spins and slides
x_drift = 120
y_drift = 20
rotation_amount = 360  # degrees of spin
depth_buffer = 3  # How many cards should stay on top of the drifting card

# === Load deck ===
card_files = [f"Card{str(i).zfill(2)}.PNG" for i in range(1, num_cards + 1)]
cards = [Image.open(f).convert("RGBA") for f in card_files]

# === Position deck at center ===
stack_x = (canvas_width - card_width) // 2
stack_y = canvas_height - card_height - 5
positions = [(stack_x, stack_y) for _ in range(num_cards)]

# === Easing ===
def ease_out_quad(t):
    return t * (2 - t)

# === Animation Frames ===
frames = []
for t in range(total_frames):
    frame = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))
    progress = t / (total_frames - 1)
    eased = ease_out_quad(progress)

    # Compute drift transform for the selected card
    dx = int(x_drift * eased)
    dy = int(y_drift * eased)
    angle = rotation_amount * eased

    # Split deck: below drifting card, drifting card, and above
    draw_order = list(range(num_cards))
    draw_below = [i for i in draw_order if i < drift_index - depth_buffer]
    draw_above = [i for i in draw_order if i >= drift_index - depth_buffer and i != drift_index]

    # Draw bottom of deck
    for i in draw_below:
        px, py = positions[i]
        frame.paste(cards[i], (px, py), cards[i])

    # Draw drifting card (beneath top few cards)
    rotated = cards[drift_index].rotate(angle, resample=Image.BICUBIC, expand=True)
    rx, ry = rotated.size
    px = stack_x + dx - (rx - card_width) // 2
    py = stack_y + dy - (ry - card_height) // 2
    frame.paste(rotated, (px, py), rotated)

    # Draw top of deck
    for i in draw_above:
        px, py = positions[i]
        frame.paste(cards[i], (px, py), cards[i])

    frames.append(frame)

# === Export Spritesheet and Preview ===
os.makedirs("exports", exist_ok=True)
sheet = Image.new("RGBA", (canvas_width * total_frames, canvas_height), (255, 255, 255, 0))
for i, f in enumerate(frames):
    sheet.paste(f, (i * canvas_width, 0), f)

sheet.save("exports/card_spin_slide_spritesheet.png")

frames[0].save(
    "exports/card_spin_slide_preview.gif",
    save_all=True,
    append_images=frames[1:],
    duration=30,
    loop=0,
    disposal=2
)