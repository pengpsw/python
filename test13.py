#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(max):
    n, a, b= 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles(lines):
    linelist=[1]
    for line in range(lines):
        columns = line + 1
        tmpList = []

        for column in range(columns):
            start = 0
            if column > 0 :
                start = linelist[column-1]
            #end 0
            if column < len(lineList):

                end = lineList[column]

            tmpList.append(start + end)

        yield tmpList

        lineList = tmpList

def triangles1():
        l=[]

    while True:

        l=[v+l[i-1] if i>0 else 1 for i,v in enumerate(l)]

        l.append(1)

        yield l

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles1():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

