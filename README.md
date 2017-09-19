# WaterMark

---
<!-- TOC -->

- [WaterMark](#watermark)
    - [安装](#安装)
    - [使用说明](#使用说明)
    - [其他](#其他)
    - [TODO LIST](#todo-list)

<!-- /TOC -->

图片水印生成器，可以给指定图片文件或者目录添加水印，水印支持自定义文本、位置、颜色、大小。

## 安装

```bash
brew tap LiushuiXiaoxia/watermark
brew install watermark
```

执行`watermark -h`，显示帮助信息，说明安装成功。

```bash
$ watermark -h
usage: watermark.py [-h] -f FILE -t TEXT -o OUT [-c COLOR] [-s SIZE]
                    [-p POSITION]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  image path or directory
  -t TEXT, --text TEXT  water mart text
  -o OUT, --out OUT     image output directory
  -c COLOR, --color COLOR
                        text color, red、blue and so on
  -s SIZE, --size SIZE  text size
  -p POSITION, --position POSITION
                        text position, left_top、left_bottom、right_top、ri
                        ght_bottom、center，default is center,
```

## 使用说明

参数说明:

```bash
  -h, --help                    帮助信息
  -f FILE, --file FILE          图片路径或者图片目录
  -t TEXT, --text TEXT          水印文本
  -o OUT, --out OUT             图片输出目录
  -c COLOR, --color COLOR       水印文本颜色，可以是red、blue、white等
  -s SIZE, --size SIZE          文本大小
  -p POSITION, --position       文本位置可以是left_top、left_bottom、right_top、right_botto center，默认是center
```

比如举例一个图片，文件路径是`image/test.png`

![](https://raw.githubusercontent.com/LiushuiXiaoxia/WaterMark/master/doc/test.png)

执行命令如下

```bash
watermark -f image/test.png -t "流水不腐小夏" -o new -c red -s 23 -p left_top
```

则效果如下

![](https://raw.githubusercontent.com/LiushuiXiaoxia/WaterMark/master/doc/1.png)

当然如果你有整个文件夹要处理，可以直接指定一个目录。

```bash
watermark -f image -t "流水不腐小夏" -c black  -o new  -p left_top
```

![](https://raw.githubusercontent.com/LiushuiXiaoxia/WaterMark/master/doc/2.png)

## 其他

如有想法或者意见，欢迎交流。

本程序暂时只支持Mac平台，如果Window平台需要运行，可以直接python代码。

## TODO LIST

* 支持自定义字体

* 支持更多平台
