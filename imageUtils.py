from PIL import Image, ImageDraw, ImageFilter

thumbWidth = 150

def thumbnail(image):
    img_width, img_height = image.size
    return image.crop(((img_width - min(image.size)) // 2,
                         (img_height - min(image.size)) // 2,
                         (img_width + min(image.size)) // 2,
                         (img_height + min(image.size)) // 2)).resize((thumbWidth, thumbWidth), Image.LANCZOS)

