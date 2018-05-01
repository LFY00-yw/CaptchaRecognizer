from PIL import Image
import numpy as np


# threshold 210 最佳，请勿随意改动
def binaryImg(img, threshold=210):
    """
    二值化
    """
    img = img.convert('L')
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    binImg = img.point(table, '1')
    return binImg


def hash(img, resize):
    img = img.resize(resize, Image.LANCZOS).convert("L")
    pixels = np.array(img).flatten()
    hs = (pixels > pixels.mean()).astype(int)
    hs = ''.join(str(e) for e in hs)
    return hs


def hammingDistance(hash1, hash2):
    """
    计算汉明距离
    """
    if len(hash1) != len(hash2):
        print('hash1', hash1)
        print('hash2', hash2)
        raise ValueError("Undefined for sequences of unequal length")

    return sum(i != j for i, j in zip(hash1, hash2))


def verticalCut(img):
    """
    纵向切割
    """
    _, height = img.size
    pix = list(np.sum(np.array(img) == 0, axis=0))
    # 列表保存像素累加值大于0的列
    x0 = []
    for x in range(len(pix)):
        if pix[x] > 1:
            x0.append(x)

    # 找出边界
    segList = []
    segList.append(x0[0])
    for i in range(1, len(x0)):
        if abs(x0[i] - x0[i - 1]) > 1:
            segList.extend([x0[i - 1], x0[i]])
    segList.append(x0[-1])

    imgList = []
    # 切割顺利的话应该是整对
    for i in range(len(segList) // 2):
        segImg = img.crop([segList[i * 2], 0, segList[i * 2 + 1], height])
        imgList.append(segImg)
    return imgList


def horizontalCut(img):
    """
    横向切割
    """
    width, _ = img.size
    pix = list(np.sum(np.array(img) == 0, axis=1))
    y0 = []
    for y in range(len(pix)):
        if pix[y] >= 1:
            y0.append(y)
    # 找出边界
    segImg = img.crop([0, y0[0], width, y0[-1]])
    return segImg
