#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageFont


def text2img(text, font_color, font_size=25):
    """生成内容为 TEXT 的水印"""

    font = ImageFont.truetype("/Library/Fonts/SimSun.ttf", font_size)
    # font = ImageFont.load_default()
    # 多行文字处理
    text = text.split('\n')
    mark_width = 0
    height = 0
    for i in range(len(text)):
        (w, h) = font.getsize(text[i])
        height = h
        if mark_width < w:
            mark_width = w
    mark_height = height * len(text)

    # 生成水印图片
    mark = Image.new('RGBA', (mark_width, mark_height))
    draw = ImageDraw.ImageDraw(mark, "RGBA")
    draw.font = font
    for i in range(len(text)):
        (w, h) = font.getsize(text[i])
        draw.text((0, i * h), text[i], fill=font_color)
    return mark


def set_opacity(im, opacity):
    """设置透明度"""

    assert opacity >= 0 and opacity < 1
    if im.mode != "RGBA":
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def watermark(im, mark, position, opacity=1.0):
    """添加水印"""

    try:
        if opacity < 1:
            mark = set_opacity(mark, opacity)
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        if im.size[0] < mark.size[0] or im.size[1] < mark.size[1]:
            print "The mark image size is larger size than original image file."
            return False

        # 设置水印位置
        if position == 'left_top':
            x = 0
            y = 0
        elif position == 'left_bottom':
            x = 0
            y = im.size[1] - mark.size[1]
        elif position == 'right_top':
            x = im.size[0] - mark.size[0]
            y = 0
        elif position == 'right_bottom':
            x = im.size[0] - mark.size[0]
            y = im.size[1] - mark.size[1]
        else:
            x = (im.size[0] - mark.size[0]) / 2
            y = (im.size[1] - mark.size[1]) / 2

        layer = Image.new('RGBA', im.size, )
        layer.paste(mark, (x, y))
        return Image.composite(layer, im, layer)
    except Exception as e:
        print "Sorry, Exception: " + str(e)
        return False


def add_mark(image_file, args, color, text):
    im = Image.open(image_file)
    mark = text2img(text, color)
    image = watermark(im, mark, args.position, 1.0)
    if image:
        name = os.path.basename(image_file)
        if not os.path.exists(args.out):
            os.mkdir(args.out)

        new_name = os.path.join(args.out, name)
        image.save(new_name)
        image.show()

        print "Success add `" + text + "` on " + image_file + " to " + os.path.abspath(new_name)
    else:
        print "Sorry, Failed."


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-f", "--file", required=True, help="image path or directory")
    parse.add_argument("-t", "--text", required=True, help="water mart text")
    parse.add_argument("-o", "--out", required=True, help="image output directory")
    parse.add_argument("-c", "--color", type=str, help="text color, red、blue and so on")
    parse.add_argument("-s", "--size", type=float, help="text size")
    parse.add_argument("-p", "--position",
                       help="text position, left_top、left_bottom、right_top、right_bottom、center，default is center,")

    args = parse.parse_args()
    print args

    text = unicode(args.text, 'utf-8')
    color = args.color or 'red'

    if os.path.isdir(args.file):
        names = os.listdir(args.file)
        for name in names:
            image_file = os.path.join(args.file, name)
            add_mark(image_file, args, color, text)
    else:
        add_mark(args.file, args, color, text)


if __name__ == '__main__':
    main()
