from matplotlib import pyplot as plt
from img_tools import *
import numpy as np
from util import getHashFile
import json
import os
import csv


def recognize(img, resize=(24, 24)):
    """
    识别字符，拼成字符串即为验证码的值
    """
    # 先更新 hash
    hashfile = 'HashFiles/hash_%sx%s.json' % resize
    if os.path.exists(hashfile):
        with open(hashfile, 'r') as fp:
            hashDict = json.load(fp)
    else:
        hashDict = getHashFile(resize, hashfile)

    img = img.convert('L')
    img = binaryImg(img)
    captcha = ''
    nearness = {}
    verticalSegImgs = verticalCut(img)
    for im in verticalSegImgs:
        charImg = horizontalCut(im)
        hashVal = str(hash(charImg, resize))
        for char in hashDict:
            nearness[char] = np.sum(hammingDistance(hashVal, el) for el in hashDict[char])
        captcha += sorted(nearness.items(), key=lambda d: d[1])[0][0]

    return captcha


def calcRatio(resize):
    """
    计算正确率
    """
    total = os.listdir('ValidationSet')
    corrent = 0

    for imgName in total:
        img = Image.open(os.path.join('ValidationSet', imgName))
        try:
            captcha = recognize(img, resize)
            if captcha == imgName[:-4]:
                corrent += 1
        except Exception as e:
            print('Recognize failed at {0}. Error: {1}'.format(imgName, e))

    ratio = '%.2f' % (corrent / len(total) * 100)
    return ratio


def plotRatio():
    """
    每次计算完后保存数据
    """
    if os.path.exists('ratios.csv'):
        print('Warning:')
        print('Ratios exists and will be plotted directly.')
        print('If you want the new data, delete ratios.csv file and run the script again.')
        with open('ratios.csv', 'r') as f:
            reader = csv.reader(f)
            resizes, ratioVals = list(zip(*reader))
    else:
        resizes = np.arange(8, 80, 2)
        ratioVals = []
        for val in resizes:
            ratio = calcRatio(resize=(val, val))
            print(val, ratio)
            ratioVals.append(ratio)
        # 保存数据
        ratios = zip(resizes, ratioVals)
        with open('ratios.csv', 'w') as f:
            writer = csv.writer(f)
            for row in ratios:
                writer.writerow(row)

    # 画图
    ratioVals = np.float64(ratioVals)
    plt.plot(resizes, ratioVals)
    plt.title('Determine the best resize value to calculate image hash')
    plt.ylim(40, 60)
    plt.xlabel('Resize value (pixel)')
    plt.ylabel('Ratios (%)')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # img = Image.open('ValidationSet/aiwhj.jpg')
    # print(recognize(img, (24, 24)))
    print(calcRatio((24, 24)))
    # plotRatio()
