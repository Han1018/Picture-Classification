import os
import glob2 as gb
import requests
import tinify
from PIL import Image
tinify.key = "xspvWq8m7gyrZ4dNxRnlyt8mYNFgvyC0"


def compressAPI(picPath, fileFormat):
    # path, format = os.path.splitext(picPath)
    tmpPic = 't.'+fileFormat
    os.rename(picPath, tmpPic)
    source = tinify.from_file(tmpPic)
    source.to_file(picPath)
    os.remove(tmpPic)


def getNeedCompressedFiles(path, format):
    # 檔案處裡 Ref : https://medium.com/seaniap/python-%E4%BD%BF%E7%94%A8%E6%AA%94%E6%A1%88%E7%B3%BB%E7%B5%B1-eaecbe7001dd
    target = path+'/'
    res = []
    allFiles = gb.glob(target+'*.'+format)
    for picPath in allFiles:
        imgSize = os.path.getsize(picPath)/1024/1024  # 單位:Mb
        if(imgSize > 1):
            res.append(picPath)
    return res


def main():
    paths = ['Picture', 'Other']
    types = ['png', 'jpg']  # HEIC not supported
    for path in paths:
        for type in types:
            print(path+'/'+type+":")
            files = getNeedCompressedFiles(path, type)

            for picPath in files:
                print(picPath)
                compressAPI(picPath, type)


# compressAPI('./Picture/1.簡暉恩.jpg')
main()
