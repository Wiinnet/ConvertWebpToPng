from PIL import Image

webp_image = "image.webp"
png_image = "image.png"

img = Image.open(webp_image)
img.save(png_image, "PNG")
