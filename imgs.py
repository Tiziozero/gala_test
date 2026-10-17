
#!/usr/bin/env python3
from PIL import Image
import random

WIDTH = 512
HEIGHT = 512

def generate_image():
    pixels = [
        (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        for _ in range(WIDTH * HEIGHT)
    ]

    image = Image.new("RGB", (WIDTH, HEIGHT))
    image.putdata(pixels)
    return image

img1 = generate_image()
img2 = generate_image()

img1.save("image1.png")
img2.save("image2.png")

print(f"Generated image1.png and image2.png ({WIDTH}x{HEIGHT})")

