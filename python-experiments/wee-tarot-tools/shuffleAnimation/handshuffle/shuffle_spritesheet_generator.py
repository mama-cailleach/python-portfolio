from PIL import Image
import numpy as np
import imageio

# Load card images — full layer size (174x300), visually stacked layout
card_files = [
    "Card01.PNG", "Card02.PNG", "Card03.PNG", "Card04.PNG",
    "Card05.PNG", "Card06.PNG", "Card07.PNG", "Card08.PNG"
]
cards = [Image.open(file).convert("RGBA") for file in card_files]
num_cards = len(cards)

# Canvas and frame setup
canvas_width, canvas_height = 300, 360
frames = []
total_frames = 90

# Original positions (fixed, stacked layout)
original_positions = [(0, 60) for _ in range(num_cards)]  # Centered horizontally

# Card dimensions and movement parameters
card_width, card_height = 174, 300
lift_offsets_y = [160, 150, 140]  # Different heights for varied movement
lift_offsets_x = [10, 20, 30]  # Slightly different horizontal offsets
scale_factors = [1, 1, 1]  # Slightly different scaling effects

# Choose three cards to animate
np.random.seed(42)
lift_indices = [2, 4, 7]  # Example: cards shuffled at different times

# Initialize without altering layer order
new_depth_positions = {idx: None for idx in lift_indices}

# Different start delays for staggered movement
start_delays = {2: 0, 4: 0, 7: 0}  # Each card starts at a different frame

for t in range(total_frames):
    new_frame = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

    draw_order = list(range(num_cards))

    for lift_index in lift_indices:
        progress = max(0, (t - start_delays[lift_index]) / (total_frames - 1))

        # Assign a new stack position at the midpoint
        if t == start_delays[lift_index] + (total_frames // 2) and new_depth_positions[lift_index] is None:
            new_depth_positions[lift_index] = lift_index- 2

        # Apply new depth placement *only if* the card has fully lifted
        if new_depth_positions[lift_index] is not None:
            draw_order.remove(lift_index)
            draw_order.insert(new_depth_positions[lift_index], lift_index)

    for i in draw_order:
        x, y = original_positions[i]
        card = cards[i]

        if i in lift_indices and t >= start_delays[i]:
            idx = lift_indices.index(i)
            dx = int(np.interp(progress, [0, 0.5, 1], [0, lift_offsets_x[idx], 0]))
            dy = int(np.interp(progress, [0, 0.5, 1], [0, -lift_offsets_y[idx], 0]))
            scale = np.interp(progress, [0, 0.5, 1], [1.0, scale_factors[idx], 1.0])

            new_size = (int(card_width * scale), int(card_height * scale))
            lifted = card.resize(new_size, resample=Image.LANCZOS)
            offset_x = dx - (new_size[0] - card_width) // 2
            offset_y = dy - (new_size[1] - card_height) // 2
            new_frame.paste(lifted, (x + offset_x, y + offset_y), lifted)
        else:
            new_frame.paste(card, (x, y), card)

    frames.append(new_frame)

# Create an empty spritesheet canvas (horizontal layout)
spritesheet_width = canvas_width * total_frames
spritesheet_height = canvas_height
spritesheet = Image.new("RGBA", (spritesheet_width, spritesheet_height), (255, 255, 255, 0))

# Paste each frame side by side
for idx, frame in enumerate(frames):
    x_offset = idx * canvas_width
    spritesheet.paste(frame, (x_offset, 0), frame)

# Save the spritesheet as a PNG
spritesheet.save("shuffle-table-200-360.png")


# Export to GIF
frames[0].save(
    "shuffle.gif",
    save_all=True,
    append_images=frames[1:],
    duration=30,
    loop=0,
    disposal=2
)