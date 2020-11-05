#!/usr/bin/env python3
# -*- coding: utf-8 -*-

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s,%s' % (std['name'],std['score']))
print_score(std1)
print_score(std2)

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s,%s' % (self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<= score <= 100:
            self.__score=score
        else:
            raise ValueError('bad score')

bart = Student('Bart s',50)
lisa = Student('lisa s',90)
bart.print_score()
lisa.print_score()
print(lisa.get_name(),lisa.get_score(),lisa.get_grade())
print(bart.get_name(),lisa.get_score(),bart.get_grade())
lisa.set_score(92)
lisa.print_score()
print(bart.get_name(),lisa.get_score(),bart.get_grade())

lisa.set_score(102)
lisa.print_score()
print(bart.get_name(),lisa.get_score(),bart.get_grade())

