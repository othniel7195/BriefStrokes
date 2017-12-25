#-*- encoding:UTF-8 -*-

import argparse
import sys
from PIL import Image


#命令行处理
parse = argparse.ArgumentParser() #type: ArgumentParser
parse.add_argument('--imgname') #输入图片名字
parse.add_argument('--output')  #输出文件名字
parse.add_argument('--w', type=int, default=80) #宽度
parse.add_argument('--h', type=int, default=80) #长

args = parse.parse_args()

IMG = args.imgname
W = args.w
H = args.h
OPUT = args.output
default_path = "{0}/{1}".format(sys.path[0], OPUT)

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#ascii_char = list("zhao.feng@ctrip.com,CTRIP@ShangHai")
length = len(ascii_char)

def get_string_image():
    img = Image.open("{0}/{1}".format(sys.path[0], IMG))
    img = img.convert("L") #转换为黑白图片，参数"L"表示黑白模式

    img = img.resize(size=(W, H), resample=Image.NEAREST)
    txt = ""

    for h in range(H):
        for w in range(W):
            #print img.getpixel((w, h))
            gray = img.getpixel((w, h))
            txt = txt + ascii_char[int(((length-1)*gray)/256)]

        txt = txt + '\r\n'

    print txt
    if OPUT:
        file = open(OPUT, 'w')
        file.write(txt)

get_string_image()

