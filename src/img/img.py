import cv2

# imread读到的颜色空间是BGR
imge = cv2.imread(r'C:\Users\Administrator\Desktop\goods_imgs\1.jpg')

hlsImg = cv2.cvtColor(imge, cv2.COLOR_BGR2HLS)

for i in range(len(hlsImg)):
    for j in range(len(hlsImg[0])):
        hlsImg[i][j][2] *= 3
        # 饱和度值域 [0,100]
        if hlsImg[i][j][2] > 100:
            hlsImg[i][j][2] = 100

# 保存图片需要采用BGR
dsImg = cv2.cvtColor(hlsImg, cv2.COLOR_HLS2BGR)
cv2.imwrite(r'C:\Users\Administrator\Desktop\goods_imgs\1_new.jpg', dsImg)

