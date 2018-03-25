

# 使用PIL读取和显示图像
from PIL import Image

path = "origin.jpg"
path1 = "origin1.png"

img1 = Image.open(path1)

print(img1.format)
print(img1.size)     # 注意，省略了通道 (w，h)
print(img1.mode)     # L为灰度图，RGB为真彩色,RGBA为加了透明通道
img1.thumbnail((128, 128))                   # 生成缩略图
img1.save('qq_image_thumb.png', 'PNG')       # 保存图片
img1.show()


a = 1






