from PIL import Image
import numpy as np
import shutil

src_path = r'C:/Users/sireen.khemesh/.gemini/antigravity/brain/6bc0ebe0-bf6e-4d46-9ff9-4b695826a984/.user_uploaded/media_1794665990726_62de17ae.png'

# 1. Copy raw image
shutil.copy(src_path, "heritage_logo_raw.png")

# 2. Make high-quality transparent PNG
im = Image.open(src_path).convert("RGBA")
data = np.array(im)

# The background color is approximately R:18, G:25, B:18 (luminance < 35)
# Letters are white (luminance > 150) with anti-aliasing in between (35 - 150)
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
# Compute brightness / distance from dark bg
bg_r, bg_g, bg_b = 18, 25, 18
diff = np.maximum.reduce([
    np.maximum(0, r.astype(int) - bg_r),
    np.maximum(0, g.astype(int) - bg_g),
    np.maximum(0, b.astype(int) - bg_b)
])

# Alpha formula: if diff <= 8 -> alpha 0; if diff >= 70 -> alpha 255; linear ramp
alpha = np.clip((diff - 8) / 60.0 * 255, 0, 255).astype(np.uint8)

# To keep the white text bright and clean on any background, we can whiten anti-aliased pixels
new_r = np.clip(r.astype(float) * 255.0 / np.maximum(diff, 1), 0, 255).astype(np.uint8)
new_g = np.clip(g.astype(float) * 255.0 / np.maximum(diff, 1), 0, 255).astype(np.uint8)
new_b = np.clip(b.astype(float) * 255.0 / np.maximum(diff, 1), 0, 255).astype(np.uint8)

new_data = np.dstack((new_r, new_g, new_b, alpha))
trans_im = Image.fromarray(new_data, "RGBA")
trans_im.save("heritage_brand_logo.png", "PNG")

print("Created heritage_brand_logo.png (Transparent) successfully!")
print("Size:", trans_im.size)
