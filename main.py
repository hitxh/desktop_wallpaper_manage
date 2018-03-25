# -*- coding: UTF-8 -*-

from __future__ import unicode_literals


import image
import datetime
import win32gui, win32con, win32api

import re
# from HttpWrapper import SendRequest
#import SendRequest    # 目前python3.5不能很好的支持

StoreFolder = "c:\\dayImage"


def setWallpaperFromBMP(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)


def setWallPaper(imagePath):
    """
    Given a path to an image, convert it to bmp and set it as wallpaper
    """

    bmpImage = image.open(imagePath)
    newPath = StoreFolder + '\\mywallpaper.bmp'
    bmpImage.save(newPath, "BMP")
    setWallpaperFromBMP(newPath)


def getPicture():
    url = "http://photography.nationalgeographic.com/photography/photo-of-the-day/"
    h = SendRequest(url)
    if h.GetSource():
        r = re.findall('<div class="download_link"><a href="(.*?)">Download', h.GetSource())
        if r:
            return SendRequest(r[0]).GetSource()
        else:
            print("解析图片地址出错，请检查正则表达式是否正确")
            return None


def setWallpaperOfToday():
    # img = getPicture()
   # path = "C:\Users\Administrator\Pictures\main_image\ceshi.jpeg"
    # if img:
    #     path = StoreFolder + "\\%s.jpg" % datetime.date.today()
    #     f = open(path, "wb")
    #     f.write(img)
    #     f.close()

    setWallPaper(path)

# setWallpaperOfToday()

path = "C:\\Users\\Administrator\\Pictures\\main_image\\ceshi.jpeg"
setWallPaper(path)

print('Wallpaper set ok!')
