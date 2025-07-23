from PIL import Image
import numpy as np
import os

# === Constants ===
canvas_width, canvas_height = 400, 240
card_width, card_height = 174, 300
total_frames = 60
max_scale = 1.6

# === Load one card ===
card = Image.open("Card07.PNG").convert("RGBA")

# === Easing function ===
def ease_in_out_quad(t):
    return 2 * t * t if t < 0.5 else -1 + (4 - 2 * t) * t

# === Generate frames ===
frames = []
for t in range(total_frames):
    progress = t / (total_frames - 1)
    eased = ease_in_out_quad(progress)

    # Scale and shift slightly upward/right
    scale = np.interp(eased, [0, 1], [0.1, max_scale])
    new_size = (int(card_width * scale), int(card_height * scale))
    scaled_card = card.resize(new_size, resample=Image.LANCZOS)

    dx = int(np.interp(eased, [0, 1], [0, 10]))  # small horizontal shift
    dy = int(np.interp(eased, [0, 1], [0, -70])) # upward lift
    offset_x = - (new_size[0] - card_width) // 2
    offset_y = - (new_size[1] - card_height) // 2

    # Create frame
    frame = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))
    px = (canvas_width - card_width) // 2 + dx + offset_x
    py = (canvas_height - card_height) // 2 + dy + offset_y
    frame.paste(scaled_card, (px, py), scaled_card)
    frames.append(frame)

# === Export spritesheet ===
os.makedirs("exports", exist_ok=True)
sheet = Image.new("RGBA", (canvas_width * total_frames, canvas_height), (255, 255, 255, 0))
for i, frame in enumerate(frames):
    sheet.paste(frame, (i * canvas_width, 0), frame)

sheet.save("exports/scaled_card_spritesheet.png")

# === Optional GIF export ===
frames[0].save(
    "exports/scaled_card.gif",
    save_all=True,
    append_images=frames[1:],
    duration=30,
    loop=0,
    disposal=2
)