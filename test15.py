#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen(object):

    def __init__(self):#初始化屏幕参数
        self.__width = None
        self.__height = None
        self.__resolution = None

    @property  # 相当于get_width
    def width(self):
        return self.__width

    @property  # 相当于get_height
    def height(self):
        return self.__height

    @width.setter  # 相当于set_width
    def width(self, width):
        self.__width = width

    @height.setter  # 相当于set_height
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        if (not self.width is None) and (not self.height is None):  # 如果宽高都不为空时返回分辨率
            return self.width * self.height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')