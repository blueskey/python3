# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。


from PIL import Image, ImageDraw, ImageFont

def add_num_to_img(image_path, sign="ok"):
    im = Image.open(image_path)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", min(width//6, height//6))
    draw.text((width*0.75, height*0.075), sign, font=font, fill=(255,33,33, 255))

    left, right = image_path.rsplit(".", 1)
    new_image_path = left + "_" + sign + "." + right
    im.save(new_image_path)

if __name__ == '__main__':
    # for test
    add_num_to_img("G:/study/python/sample/a.png")
    print("Finished.")