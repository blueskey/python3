# -*- coding: utf-8 -*-
# 生成图片验证码

__author__ = 'Administrator'

from PIL import Image, ImageDraw, ImageFont,ImageFilter
import random
if __name__=="__main__":
    strs="ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789"

    # img=Image.open("G:/study/python/sample/captcha.png","r")
    width=150
    height=60
    img=Image.new("RGB",(width,height),color=(255,255,255))
    margin=10
    xx=(150-2*margin)//4

    #多生成一些干扰项
    for i in range(1,5):
        draw = ImageDraw.Draw(img)
        for j in range(1,1500):
            draw.point((random.randrange(i*55),random.randrange(height)),(random.randrange(255),random.randrange(255),random.randrange(255), 255))

        for k in range(1,4):
            draw.line([(random.randrange(width),random.randrange(height)),(random.randrange(width),random.randrange(height))],(random.randrange(255),random.randrange(255),random.randrange(255), 255),1)

    #模糊滤镜下
    img.filter(ImageFilter.BLUR)

    for i in range(1,5):
        font = ImageFont.truetype("arial.ttf", width//3)
        text=strs[random.randint(0,len(strs)-1)]
        # text=strs[random.randrange(len(strs))]
        # text=random.choice(strs)
        print(text)
        draw.text((margin+(i-1)*xx, height*0.075), text, font=font, fill=(random.randrange(255),random.randrange(255),random.randrange(255), 255))

    img.save("ncaptcha.png")
    print("finished")