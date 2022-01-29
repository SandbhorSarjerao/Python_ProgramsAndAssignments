from PIL import Image

img = Image.open('Google.jpg')

print(img.show())
print(img.format)
print(img.size)
print(img.mode)
print(img.rotate(90))
print(img.resize(400,400))
print(img.thumbnail(300,300))
print(img.crop(250,250,250,250))
print(img.convert('L'))
print(img.ImageFilter.BLUR)

