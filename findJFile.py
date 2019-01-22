#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Aymer Zhang'

import os

# 项目文件夹路径
dirPath = 'project/projectName'
keyEnd = '.java'
if __name__ == '__main__':
    allLines = 0

    for root, dirs, files in os.walk(dirPath, topdown=False):
        for filename in files:
            if filename.endswith(keyEnd):
                allLines += len(open(os.path.join(root, filename)).readlines())

    print('%s文件有 %d 行' % (keyEnd.strip('.'), allLines))
