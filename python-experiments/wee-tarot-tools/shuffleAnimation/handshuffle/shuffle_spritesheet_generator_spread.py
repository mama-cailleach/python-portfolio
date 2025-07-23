from PIL import Image
import numpy as np
import math
import random
import os

# === Constants ===
canvas_width, canvas_height = 400, 240
card_width, card_height = 174, 300
total_frames = 100
fan_radius = 90
angle_start, angle_end = -40, 40
flip_duration = 20
explode_duration = 20
explode_start = total_frames - explode_duration
num_cards = 16

# === Setup ===
frames = []
cards = [
    Image.open(f"Card{str(i).zfill(2)}.PNG").convert("RGBA")
    for i in range(1, num_cards + 1)
]
center_x = (canvas_width - card_width) // 2
center_y = canvas_height - card_height + 20

# Assign random explosion vectors
np.random.seed(42)
explode_vectors = {
    i: (
        random.randint(-50, 200),  # dx
        random.randint(-200, -120)  # dy
    ) for i in range(num_cards)
}

# === Easing ===
def ease_in_out(t): return 2*t*t if t < 0.5 else -1 + (4 - 2*t)*t
def flip_ease(t): return math.sin(math.pi * t)
#def explode_ease(t): return t**0.5  # fast push then glide
def explode_ease(t):
    return t ** 0.8  # slightly more sustained thrust



# === Frames ===
for t in range(total_frames):
    frame = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))
    progress = t / (total_frames - 1)
    fan_progress = ease_in_out(min(progress * 2, 1))

    for i, card in enumerate(cards):
        base_angle = np.interp(i, [0, num_cards - 1], [angle_start, angle_end])
        angle_deg = -base_angle * fan_progress
        theta = np.deg2rad(base_angle * fan_progress)
        x_offset = int(fan_radius * math.sin(theta))
        y_offset = int(fan_radius * (1 - math.cos(theta)))

        # Flip effect
        flip_phase = max(0, min(1, (t - total_frames//2 - i*2)/flip_duration))
        flip_scale = 1.0 - 2.0 * flip_ease(flip_phase)
        if flip_scale < 0:
            flipped = card.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            flipped = card

        rotated = flipped.rotate(angle_deg, resample=Image.BICUBIC, expand=True)

        # Explode phase
        if t >= explode_start:
            ep = (t - explode_start) / explode_duration
            dx, dy = explode_vectors[i]
            x_offset += int(dx * explode_ease(ep))
            y_offset += int(dy * explode_ease(ep))


        rx, ry = rotated.size
        px = center_x + x_offset - (rx - card_width) // 2
        py = center_y + y_offset - (ry - card_height) // 2
        frame.paste(rotated, (px, py), rotated)

    frames.append(frame)

# === Export Spritesheet and Preview ===
os.makedirs("exports", exist_ok=True)
sheet = Image.new("RGBA", (canvas_width * total_frames, canvas_height))
for i, f in enumerate(frames):
    sheet.paste(f, (i * canvas_width, 0), f)
sheet.save("exports/explode_finale_spritesheet.png")

frames[0].save(
    "exports/explode_finale_preview.gif",
    save_all=True,
    append_images=frames[1:],
    duration=30,
    loop=0,
    disposal=2
)