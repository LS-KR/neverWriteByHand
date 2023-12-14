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


def word2pic(txt_path='./source.txt', ttf_path="./src/writeup.TTF", save_path="./result/", size=4, white=0,
             fill=(0, 0, 0, 255)):
    font = ImageFont.truetype(ttf_path, 25)  # Setup Font
    f = open(txt_path, 'r', encoding='utf-8')  # Setup Text
    string = f.read()
    f.close()
    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        img = Image.open('./src/backgroundW.png' if white == 1 else './src/backgroundY.png')
        draw = ImageDraw.Draw(img)
        for i in range(28):
            j = 70
            while j < 995:
                if flag >= lenstr:
                    break
                if string[flag] == '\n':
                    flag += 1
                    break
                draw.text((random.random() * size / 2 + j, 83 + random.random() * size + i * 48), string[flag], fill,
                          font=font)
                if isAlphaBet(string[flag]):
                    j += 13
                else:
                    j += 22
                flag += 1
            if flag >= lenstr:
                break
        img.save(save_path + str(page) + ".png")
        page += 1


def getConfig(key: str, default: any, ctype: str):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    secret = config['DEFAULT']
    try:
        if ctype.__eq__('int'):
            return int(secret[key])
        elif ctype.__eq__('float'):
            return float(secret[key])
        elif ctype.__eq__('bool'):
            return bool(secret[key])
        elif ctype.__eq__('str'):
            return str(secret[key])
        else:
            return secret[key]
    except:
        return default


if __name__ == "__main__":
    size = getConfig('size', 4, 'int')  # Chaos
    txt_path = getConfig('txt_path', './source.txt', 'str')  # Text File
    ttf_path = getConfig('ttf_path', './src/writeup.TTF', 'str')  # Font
    save_path = getConfig('save_path', './result/', 'str')  # storage folder
    white = getConfig('white', 0, 'int')  # If set as 1, a white background is generated
    fill = getConfig('fill', '#000060FF', 'str')  # Color (RGBA)
    for root, dirs, files in os.walk(save_path):
        for file in files:
            if file.endswith('.png'):
                os.remove(root + '/' + file)
    word2pic(txt_path, ttf_path, save_path, size, white, fill)
    print("success!")
