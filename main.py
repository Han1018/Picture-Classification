import cv2 as cv
import os
import shutil
import glob2 as gb


def facedetect(picname):
    # FaceDetect Ref : https://zhuanlan.zhihu.com/p/63154631

    # 加载haar级联分类器
    face_cascade = cv.CascadeClassifier(
        './haarcascade_frontalface_default.xml')

    # 读取进行检测的图像
    img = cv.imread(picname)
    # 将原图像转为灰度图
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 使用级联分类器进行人脸检测 返回值为 人脸的bounding box参数（左上角坐标（x,y），矩形框长和宽）
    # 如果有多张人脸 则返回一个四维数组
    BBox = face_cascade.detectMultiScale(gray, 1.3, 5)
    if BBox == ():
        return False
    return True


def classify(picname, fileFormat):
    # 檔案處裡Ref :
    # https://medium.com/seaniap/python-%E4%BD%BF%E7%94%A8%E6%AA%94%E6%A1%88%E7%B3%BB%E7%B5%B1-eaecbe7001dd
    # https://www.delftstack.com/zh-tw/howto/python/python-file-move/#%25E5%259C%25A8-python-%25E4%25B8%25AD%25E4%25BD%25BF%25E7%2594%25A8-shutil.move-%25E5%2592%258C-listdir-%25E6%2596%25B9%25E6%25B3%2595%25E7%25A7%25BB%25E5%258B%2595%25E5%25A4%259A%25E5%2580%258B%25E6%25AA%2594%25E6%25A1%2588

    tmpPic = 't.'+fileFormat
    dir, name = os.path.split(picname)
    os.rename(picname, tmpPic)
    hasFace = facedetect(tmpPic)
    os.rename(tmpPic, picname)

    if hasFace == True:
        shutil.move(picname, 'Picture/'+name)
        return
    else:
        shutil.move(picname, 'Other/'+name)
    return


def getFiles(format):
    target = 'Site Files/'
    return gb.glob(target+'*.'+format)


def main():
    types = ['png', 'jpg']  # HEIC not supported
    for type in types:
        files = getFiles(type)
        for pic in files:
            classify(pic, 'jpg')


main()
