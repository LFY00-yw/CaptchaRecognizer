from img_tools import *
from recognize import *


class Test:
    def test_recognize(self):
        img = Image.open('ValidationSet/aasd.jpg')
        assert(recognize(img) == "aasd")

    def test_calcRatio(self):
        assert(type(calcRatio((24, 24)) == str))
