from img_tools import *
from PIL import Image
import requests
import json
import os


def downloadCaptcha():
    """
    从 SJTU-jwc 下载验证码样本
    """
    path = 'ValidationSet'
    for i in range(100):
        print("正在下载第%s张验证码" % str(i))
        file_path = os.path.join(path, str(i), '.jpg')
        r = requests.get('https://jaccount.sjtu.edu.cn/jaccount/captcha?')
        with open(file_path, 'bw') as f:
            f.write(r.content)


def newFolder():
    """
    生成分类文件夹用于前期处理
    """
    if os.path.exists('SingleChars'):
        pass
    else:
        os.mkdir('SingleChars')
    os.chdir('SingleChars')
    for i in 'abcdefghijklmnopqrstuvwxyz1234567890':
        if os.path.exists(i):
            continue
        else:
            os.mkdir(i)
    os.chdir('..')


def getHashFile(resize, filename):
    """
    一个字符选5张图片计算 hash 值
    """
    hashDict = {}
    imgDict = {
        'a': [
            './SingleChars/a/tmp/0.jpg',
            './SingleChars/a/tmp/1.jpg',
            './SingleChars/a/tmp/2.jpg',
            './SingleChars/a/tmp/3.jpg',
            './SingleChars/a/tmp/121.jpg',
        ],
        'b': [
            './SingleChars/b/tmp/2.jpg',
            './SingleChars/b/tmp/1.jpg',
            './SingleChars/b/tmp/11.jpg',
            './SingleChars/b/tmp/22.jpg',
            './SingleChars/b/tmp/54.jpg',
        ],
        'c': [
            './SingleChars/c/tmp/0.jpg',
            './SingleChars/c/tmp/1.jpg',
            './SingleChars/c/tmp/2.jpg',
            './SingleChars/c/tmp/4.jpg',
            './SingleChars/c/tmp/99.jpg',
        ],
        'd': [
            './SingleChars/d/tmp/0.jpg',
            './SingleChars/d/tmp/1.jpg',
            './SingleChars/d/tmp/8.jpg',
            './SingleChars/d/tmp/25.jpg',
            './SingleChars/d/tmp/90.jpg',
        ],
        'e': [
            './SingleChars/e/tmp/4.jpg',
            './SingleChars/e/tmp/3.jpg',
            './SingleChars/e/tmp/33.jpg',
            './SingleChars/e/tmp/39.jpg',
            './SingleChars/e/tmp/53.jpg',
        ],
        'f': [
            './SingleChars/f/tmp/0.jpg',
            './SingleChars/f/tmp/4.jpg',
            './SingleChars/f/tmp/2.jpg',
            './SingleChars/f/tmp/39.jpg',
            './SingleChars/f/tmp/74.jpg',
        ],
        'g': [
            './SingleChars/g/tmp/2.jpg',
            './SingleChars/g/tmp/8.jpg',
            './SingleChars/g/tmp/21.jpg',
            './SingleChars/g/tmp/39.jpg',
            './SingleChars/g/tmp/102.jpg',
        ],
        'h': [
            './SingleChars/h/tmp/0.jpg',
            './SingleChars/h/tmp/1.jpg',
            './SingleChars/h/tmp/9.jpg',
            './SingleChars/h/tmp/12.jpg',
            './SingleChars/h/tmp/75.jpg',
        ],
        'i': [
            './SingleChars/i/tmp/0.jpg',
            './SingleChars/i/tmp/1.jpg',
            './SingleChars/i/tmp/24.jpg',
            './SingleChars/i/tmp/27.jpg',
            './SingleChars/i/tmp/41.jpg',
        ],
        'j': [
            './SingleChars/j/tmp/0.jpg',
            './SingleChars/j/tmp/3.jpg',
            './SingleChars/j/tmp/4.jpg',
            './SingleChars/j/tmp/5.jpg',
            './SingleChars/j/tmp/9.jpg',
        ],
        'k': [
            './SingleChars/k/tmp/0.jpg',
            './SingleChars/k/tmp/1.jpg',
            './SingleChars/k/tmp/2.jpg',
            './SingleChars/k/tmp/3.jpg',
            './SingleChars/k/tmp/4.jpg',
        ],
        'l': [
            './SingleChars/l/tmp/0.jpg',
            './SingleChars/l/tmp/1.jpg',
            './SingleChars/l/tmp/4.jpg',
            './SingleChars/l/tmp/28.jpg',
            './SingleChars/l/tmp/32.jpg',
        ],
        'm': [
            './SingleChars/m/tmp/0.jpg',
            './SingleChars/m/tmp/1.jpg',
            './SingleChars/m/tmp/2.jpg',
            './SingleChars/m/tmp/3.jpg',
            './SingleChars/m/tmp/4.jpg',
        ],
        'n': [
            './SingleChars/n/tmp/0.jpg',
            './SingleChars/n/tmp/3.jpg',
            './SingleChars/n/tmp/4.jpg',
            './SingleChars/n/tmp/5.jpg',
            './SingleChars/n/tmp/7.jpg',
        ],
        'o': [
            './SingleChars/o/tmp/2.jpg',
            './SingleChars/o/tmp/3.jpg',
            './SingleChars/o/tmp/9.jpg',
            './SingleChars/o/tmp/10.jpg',
            './SingleChars/o/tmp/11.jpg',
        ],
        'p': [
            './SingleChars/p/tmp/0.jpg',
            './SingleChars/p/tmp/4.jpg',
            './SingleChars/p/tmp/5.jpg',
            './SingleChars/p/tmp/6.jpg',
            './SingleChars/p/tmp/7.jpg',
        ],
        'q': [
            './SingleChars/q/tmp/0.jpg',
            './SingleChars/q/tmp/9.jpg',
            './SingleChars/q/tmp/26.jpg',
            './SingleChars/q/tmp/20.jpg',
            './SingleChars/q/tmp/57.jpg',
        ],
        'r': [
            './SingleChars/r/tmp/1.jpg',
            './SingleChars/r/tmp/2.jpg',
            './SingleChars/r/tmp/3.jpg',
            './SingleChars/r/tmp/4.jpg',
            './SingleChars/r/tmp/5.jpg',
        ],
        's': [
            './SingleChars/s/tmp/0.jpg',
            './SingleChars/s/tmp/1.jpg',
            './SingleChars/s/tmp/2.jpg',
            './SingleChars/s/tmp/3.jpg',
            './SingleChars/s/tmp/4.jpg',
        ],
        't': [
            './SingleChars/t/tmp/0.jpg',
            './SingleChars/t/tmp/2.jpg',
            './SingleChars/t/tmp/13.jpg',
            './SingleChars/t/tmp/24.jpg',
            './SingleChars/t/tmp/43.jpg',
        ],
        'u': [
            './SingleChars/u/tmp/0.jpg',
            './SingleChars/u/tmp/1.jpg',
            './SingleChars/u/tmp/13.jpg',
            './SingleChars/u/tmp/31.jpg',
            './SingleChars/u/tmp/48.jpg',
        ],
        'v': [
            './SingleChars/v/tmp/2.jpg',
            './SingleChars/v/tmp/8.jpg',
            './SingleChars/v/tmp/16.jpg',
            './SingleChars/v/tmp/20.jpg',
            './SingleChars/v/tmp/65.jpg',
        ],
        'w': [
            './SingleChars/w/tmp/0.jpg',
            './SingleChars/w/tmp/2.jpg',
            './SingleChars/w/tmp/3.jpg',
            './SingleChars/w/tmp/4.jpg',
            './SingleChars/w/tmp/18.jpg',
        ],
        'x': [
            './SingleChars/x/tmp/0.jpg',
            './SingleChars/x/tmp/1.jpg',
            './SingleChars/x/tmp/2.jpg',
            './SingleChars/x/tmp/4.jpg',
            './SingleChars/x/tmp/5.jpg',
        ],
        'y': [
            './SingleChars/y/tmp/0.jpg',
            './SingleChars/y/tmp/3.jpg',
            './SingleChars/y/tmp/4.jpg',
            './SingleChars/y/tmp/7.jpg',
            './SingleChars/y/tmp/9.jpg',
        ],
        'z': [
            './SingleChars/z/tmp/0.jpg',
            './SingleChars/z/tmp/1.jpg',
            './SingleChars/z/tmp/3.jpg',
            './SingleChars/z/tmp/4.jpg',
            './SingleChars/z/tmp/5.jpg',
        ]
    }
    for char in imgDict:
        hashDict[char] = []
        for img in imgDict[char]:
            imgHash = str(hash(Image.open(img), resize))
            hashDict[char].append(imgHash)
    with open(filename, 'w') as fp:
        json.dump(hashDict, fp)
    return hashDict
