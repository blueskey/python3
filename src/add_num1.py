from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

file_name=input("Please input the image name, including file appendix: ")
img = Image.open(file_name)
s = input("Please input the number to display: ")
num = int(s)
img_width,img_height = img.size
font_size = 60 * img_height // 480
font_height = 60
font_width = 40
text_x = img_width - font_width * len(str(num))
text_y = 0
print("font_size=",font_size)
font = ImageFont.truetype("arial.ttf", font_size)

draw = ImageDraw.Draw(img)
draw.text((text_x, text_y), str(num), (255,0,0), font=font)

img.save("new_image.jpg")
print("finished!")