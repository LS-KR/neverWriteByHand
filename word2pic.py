import random
import os
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
                c = s.encode('ascii')
                return True
            except:
                return False
    return True


def word2pic(txt_path='./source.txt', ttf_path="./src/writeup.TTF", save_path="./result/", size=4, white=False):
    font = ImageFont.truetype(ttf_path, 25)  # 设置字体
    f = open(txt_path, 'r', encoding='utf-8')  # 设置文档
    string = f.read()
    f.close()
    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        img = Image.open('./src/backgroundW.png' if white else './src/backgroundY.png')
        draw = ImageDraw.Draw(img)
        for i in range(28):
            j = 70
            while j < 995 :
                if flag >= lenstr:
                    break
                if string[flag] == '\n':
                    flag += 1
                    break
                draw.text((random.random() * size / 2 + j, 83 + random.random() * size + i * 48), string[flag], (0, 0, 0), font=font)
                if isAlphaBet(string[flag]):
                    j += 13
                else:
                    j += 25
                flag += 1
            if flag >= lenstr:
                break
        img.save(save_path + str(page) + ".png")
        page += 1

if __name__ == "__main__":
    for root, dirs, files in os.walk('./result/'):
        for file in files:
            if file.endswith('.png'):
                os.remove(root + '/' + file)
    size = 2  # 混乱度
    txt_path = './source.txt'  # 文档位置
    ttf_path = "src/writeup.TTF"  # 字体位置
    save_path = "./result/"  # 储存文件夹 若没有不会自动生成
    white = False    # 若为 True 则生成白底
    word2pic(txt_path, ttf_path, save_path, size, white)
    print("success!")
