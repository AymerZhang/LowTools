#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Aymer Zhang'

import os

dirpath = '/Users/zhangzhongwen/CodeStudio/AndroidStudioProjects/trunk/app'
if __name__ == '__main__':
    allLines = 0

    for root, dirs, files in os.walk(dirpath, topdown=False):
        for filename in files:
            if filename.endswith('.java'):
                allLines += len(open(os.path.join(root, filename)).readlines())

    print('长度 %d' % allLines)
