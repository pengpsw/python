#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 22:43
# @Author  : Adong_Chen
 
from xml import sax
 
 
class TestHandler(sax.ContentHandler):                # 定义自己的handler类，继承sax.ContentHandler
    def __init__(self):
        sax.ContentHandler.__init__(self)     # 弗父类和子类都需要初始化（做一些变量的赋值操作等）
        self._content = ""
        self._tag = ""
 
    def startElement(self, name, attrs):           # 遇到<tag>标签时候会执行的方法，这里的name，attrs不用自己传值的（这里其实是重写）
        self._tag = name
        if name == "bookstore":
            print "=========BOOKSTORE========="
        if self._tag == "book":
            print "BOOK: " + attrs["category"]
            print "--------------------------"
 
    def endElement(self, name):　　　　　　　　　　　　　　# 遇到</tag>执行的方法，name不用自己传值（重写）
        # print "endElement"
        if name == "bookstore":
            print "=========BOOKSTORE========="
        elif name == "title":
            print "Title: " + self._content
        elif name == "author":
            print "Author: " + self._content
        elif name == "year":
            print "Year: " + self._content
        elif name == "price":
            print "Price: " + self._content
        else:
            pass
 
    def characters(self, content):                      # 获取标签内容
        self._content = content
 
 
if __name__ == "__main__":
    handler = TestHandler()         # 自定义类实例化成对象
    sax.parse("Test2.xml", handler)  # 解析xml文件