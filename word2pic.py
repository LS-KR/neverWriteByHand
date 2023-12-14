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


if __name__ == "__main__":
    size = 4  # Chaos
    txt_path = './source.txt'  # Text File
    ttf_path = "./src/writeup.TTF"  # Font
    save_path = "./result/"  # storage folder
    white = 0  # If set as 1, a white background is generated
    fill = "#000060FF"  # Color (RGBA)
    try:
        config = configparser.ConfigParser()
        config.read('./config.ini')
        secret = config['DEFAULT']
        size = int(secret['size'])
        white = int(secret['white'])
        txt_path = secret['txt_path']
        ttf_path = secret['ttf_path']
        save_path = secret['save_path']
        fill = secret['fill']
    except:
        print('invalid config')
        print('using default settings')
        size = 4
        txt_path = './source.txt'
        ttf_path = "./src/writeup.TTF"
        save_path = "./result/"
        white = 0
        fill = "#000060FF"
    for root, dirs, files in os.walk(save_path):
        for file in files:
            if file.endswith('.png'):
                os.remove(root + '/' + file)
    word2pic(txt_path, ttf_path, save_path, size, white, fill)
    print("success!")
