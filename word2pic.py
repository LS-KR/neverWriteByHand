import os
import configparser
from PIL import ImageFont
from PIL import Image
from handright import Template
from handright import handwrite


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
        fill=0,
        lines=28,
        font_size=25,
        xy=(70, 83),
        line_gap=48,
        rx=(995, 13, 22),
        wide_char='',
        sigma=20
):
    f = open(txt_path, 'r', encoding='utf-8')  # Setup Text
    string = f.read()
    f.close()
    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        img = Image.open(background)
        font = ImageFont.truetype(font=ttf_path, size=font_size)
        template = Template(
            background=img,
            font=font,
            font_size_sigma=sigma * 0.1 + size * 0.25,
            fill=fill,
            left_margin=xy[0],
            top_margin=xy[1],
            bottom_margin=img.height - xy[1] - lines * line_gap,
            right_margin=img.width - xy[0] - rx[0],
            word_spacing=5,
            word_spacing_sigma=size,
            start_chars="“（[<",  # 特定字符提前换行，防止出现在行尾
            end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
            perturb_x_sigma=size,  # 笔画横向偏移随机扰动
            perturb_y_sigma=size,  # 笔画纵向偏移随机扰动
            line_spacing_sigma=size * 1.5,  # 行间距随机扰动
        )
        imgs = handwrite(string, template)
        for i, im in enumerate(imgs):
            assert isinstance(im, Image.Image)
            im.save(save_path + str(page) + '.png')
        page += 1


def getConfig(_secret: str, key: str, default: any, ctype: str):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    try:
        secret = config[_secret]
        match ctype:
            case 'int':
                return int(secret[key])
            case 'float':
                return float(secret[key])
            case 'bool':
                return bool(secret[key])
            case 'str':
                return str(secret[key])
    except:
        return default


if __name__ == "__main__":
    size = getConfig('DEFAULT', 'size', 4, 'int')  # Chaos
    txt_path = getConfig('DEFAULT', 'txt_path', './source.txt', 'str')  # Text File
    ttf_path = getConfig('DEFAULT', 'ttf_path', './src/writeup.ttf', 'str')  # Font
    save_path = getConfig('DEFAULT', 'save_path', './result/', 'str')  # storage folder
    white = getConfig('DEFAULT', 'white', 0, 'int')  # If set as 1, a white background is generated
    fill = getConfig('DEFAULT', 'fill', '#000000FF', 'str')  # Color (RGBA)
    background = getConfig('OVERRIDE', 'background', './src/backgroundW.png' if white == 1 else './src/backgroundY.png',
                           'str')
    lines = getConfig('OVERRIDE', 'lines', 28, 'int')
    font_size = getConfig('OVERRIDE', 'font_size', 25, 'int')
    xy = (getConfig('OVERRIDE', 'startX', 70, 'int'), getConfig('OVERRIDE', 'startY', 83, 'int'))
    line_gap = getConfig('OVERRIDE', 'gap', 48, 'int')
    rx = (
    getConfig('OVERRIDE', 'length', 925, 'int') + xy[0], getConfig('OVERRIDE', 'sizeEn', int(font_size / 2), 'int'),
    getConfig('OVERRIDE', 'sizeCn', font_size - 3, 'int'))
    wide_char = getConfig('FORMAT', 'wide_char', '', 'str')
    sigma = getConfig('FORMAT', 'sigma', 20, 'int')
    for root, dirs, files in os.walk(save_path):
        for file in files:
            if file.endswith('.png'):
                os.remove(root + '/' + file)
    word2pic(
        txt_path=txt_path,
        ttf_path=ttf_path,
        size=size,
        save_path=save_path,
        background=background,
        fill=int(format(int(fill.strip('#'), 16), 'd')),
        lines=lines,
        font_size=font_size,
        xy=xy,
        line_gap=line_gap,
        rx=rx,
        wide_char=wide_char,
        sigma=sigma
    )
    print("success!")
