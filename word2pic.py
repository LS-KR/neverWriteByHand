import random
import os
import configparser
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def isAlphaBet(s=''):
    length = len(s)
    if length == 0:
        return False
    for i in range(0, length):
        if s[i] != ' ':
            try:
                s.encode('ascii')
                return True
            except:
                return False
    return True


def word2pic(
        txt_path='./source.txt',
        ttf_path="./src/writeup.ttf",
        save_path="./result/",
        size=4,
        background='./src/backgroundW.png',
        fill=(0, 0, 0, 255),
        lines=28,
        font_size=25,
        xy=(70, 83),
        line_gap=48,
        rx=(995, 13, 22),
        wide_char=''
):
    font = ImageFont.truetype(ttf_path, font_size)  # Setup Font
    f = open(txt_path, 'r', encoding='utf-8')  # Setup Text
    string = f.read()
    f.close()
    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        img = Image.open(background)
        draw = ImageDraw.Draw(img)
        for i in range(lines):
            j = xy[0]
            while j < rx[0]:
                if flag >= lenstr:
                    break
                if string[flag] == '\n':
                    flag += 1
                    break
                draw.text((random.random() * size / 2 + j, xy[1] + random.random() * size + i * line_gap), string[flag], fill, font=font)
                if (not isAlphaBet(string[flag])) or (string[flag] in wide_char):
                    j += rx[2]
                else:
                    j += rx[1]
                flag += 1
            if flag >= lenstr:
                break
        img.save(save_path + str(page) + ".png")
        page += 1


def getConfig(_secret: str, key: str, default: any, ctype: str):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    try:
        secret = config[_secret]
        if ctype == 'int':
            return int(secret[key])
        elif ctype == 'float':
            return float(secret[key])
        elif ctype == 'str':
            return str(secret[key])
        elif ctype == 'bool':
            return bool(secret[key])
        else:
            return secret[key]
    except:
        return default

if __name__ == "__main__":
    size = getConfig('DEFAULT', 'size', 4, 'int')  # Chaos
    txt_path = getConfig('DEFAULT', 'txt_path', './source.txt', 'str')  # Text File
    ttf_path = getConfig('DEFAULT', 'ttf_path', './src/writeup.ttf', 'str')  # Font
    save_path = getConfig('DEFAULT', 'save_path', './result/', 'str')  # storage folder
    white = getConfig('DEFAULT', 'white', 0, 'int')  # If set as 1, a white background is generated
    fill = getConfig('DEFAULT', 'fill', '#000000FF', 'str')  # Color (RGBA)
    background = getConfig('OVERRIDE', 'background', './src/backgroundW.png' if white == 1 else './src/backgroundY.png', 'str')
    lines = getConfig('OVERRIDE', 'lines', 28, 'int')
    font_size = getConfig('OVERRIDE', 'font_size', 25, 'float')
    xy = (getConfig('OVERRIDE', 'startX', 70, 'int'), getConfig('OVERRIDE', 'startY', 83, 'int'))
    line_gap = getConfig('OVERRIDE', 'gap', 48, 'int')
    rx = (getConfig('OVERRIDE', 'length', 925, 'int') + xy[0], getConfig('OVERRIDE', 'sizeEn', int(font_size / 2), 'int'), getConfig('OVERRIDE', 'sizeCn', font_size - 3, 'int'))
    wide_char = getConfig('FORMAT', 'wide_char', '', 'str')
    for root, dirs, files in os.walk(save_path):
        for file in files:
            if file.endswith('.png'):
                os.remove(root + '/' + file)
    word2pic(txt_path, ttf_path, save_path, size, background, fill, lines, font_size, xy, line_gap, rx, wide_char=wide_char)
    print("success!")
