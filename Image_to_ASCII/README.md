## Image to ASCII ##
一个将图片按灰度转换为字符画的小工具
***
灰度的计算公式为：

    gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
***
用到的库有：pillow(PIL)、argparse

**argparse**是Python标准库中推荐使用的命令行解析模块。可以用于命令行调用.py时传递参数的交互。
参考：
* [Argparse简易教程](https://blog.ixxoo.me/argparse.html)
* [官方文档](https://docs.python.org/2/library/argparse.html)

**Python Imaging Library**，或者叫PIL，是Python图像操作的核心库（据说早已停止开发）。**Pillow**是一个对 PIL 友好的一个分支，其中的Image类，被用于从文件中读取图片。
参考：
* [Python图像处理库：Pillow 初级教程](http://www.cnblogs.com/wbin91/p/3971079.html)
* [Pillow 中文文档](http://pillow-cn.readthedocs.io/zh_CN/latest/)
* [安装参考](http://pythonguidecn.readthedocs.io/zh/latest/scenarios/imaging.html)

***


这个小程序的教程来自：https://www.shiyanlou.com/courses/370/labs/1191/document
