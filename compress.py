import os
import glob2 as gb
import requests
import tinify
from PIL import Image
tinify.key = "xspvWq8m7gyrZ4dNxRnlyt8mYNFgvyC0"


# def compressAPI(picPath):
#     path, format = os.path.splitext(picPath)
#     source = tinify.from_file(picPath)
#     source.to_file(path+'_compressed'+format)


def getNeedCompressedFiles(path, format):
    target = path+'/'
    res = []
    for picPath in gb.glob(target+'*.'+format):
        # img = Image.open(picPath)
        # imgSize = img.size  # 檔案大小

        imgSize = os.path.getsize(picPath)/1024/1024  # 單位:Mb
        if(imgSize > 1):
            res.append(picPath)
    return res


files = getNeedCompressedFiles('Picture', 'jpg')
print(len(files))
# compressAPI('./Picture/1.簡暉恩.jpg')
