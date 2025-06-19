from PIL import Image, ImageDraw
import math

def create_frame(radius):
    # Create an image with a transparent background
    frame = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)

    radius = int(radius)
    
    # Draw a white circle with a white outline
    left_up_point = (50 - radius, 50 - radius)
    right_down_point = (50 + radius, 50 + radius)
    draw.ellipse([left_up_point, right_down_point], fill='white', outline='white')
    
    return frame

# Total frames for 3 seconds at 24 FPS
total_frames = 3 * 24
frames = []

# Generate frames for one cycle of the animation
for t in range(total_frames):
    phase = math.sin(4 * math.pi * t / total_frames)
    radius = 25 + 15 * phase**2 * (phase / abs(phase + 1e-10))
    frame = create_frame(radius)
    frames.append(frame)

# Save frames as a GIF
frames[0].save("CreateAnimation/standard.gif", save_all=True, append_images=frames,duration=3,transparency=0,loop=0,disposal=2)
