

# 使用PIL读取和显示图像
from PIL import Image

path = "origin.jpg"

img1 = Image.open(path)

print(img1.format)
print(img1.size)     # 注意，省略了通道 (w，h)
print(img1.mode)     # L为灰度图，RGB为真彩色,RGBA为加了透明通道
img1.show()


a = 1






