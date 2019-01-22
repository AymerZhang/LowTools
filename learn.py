#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 一笔画完工具 """  # 任何模块的第一个字符串会被当做是注释

__author__ = 'Aymer Zhang'  # 模块作者 当公开代码的时候别人就会看到了作者的大名了
import tkinter as tk
import tkinter.messagebox as messagebox

# 源数据
data = []
# 0表示起点，1表示可以走的路径，2表示不可以走的路径

# 所有按钮
buttons = []

# 存储答案路线
ways = []


# 自定义button实现点击同步数据和视图
class MyButton(tk.Button):
    def __init__(self, master=None):
        tk.Button.__init__(self, master, command=self.count)
        self.val = -1
        self['text'] = str(self.val)

    def count(self):
        if self.val < 2:
            self.val += 1
        else:
            self.val = 0
        self['text'] = str(self.val)


# 计算答案核心方法
def dfs(data, row, i, ways):
    #     a=[1,-1]
    data[row][i] = 3  # 这里置为3表示已经这个点已经走过

    if row + 1 < len(data) and data[row + 1][i] == 1:
        if not dfs(data, row + 1, i, ways):
            data[row + 1][i] = 1

    if row - 1 > -1 and data[row - 1][i] == 1:
        if not dfs(data, row - 1, i, ways):
            data[row - 1][i] = 1

    if i + 1 < len(data[0]) and data[row][i + 1] == 1:
        if not dfs(data, row, i + 1, ways):
            data[row][i + 1] = 1

    if i - 1 > -1 and data[row][i - 1] == 1:
        if not dfs(data, row, i - 1, ways):
            data[row][i - 1] = 1
    for row1 in data:
        for i1 in row1:
            if (i1 == 1):
                return False
    ways.append((row, i))
    return True


# 开始计算
def go():
    # 根据视图更新数据
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(buttons[i][j]['text'])

    # 检测未初始化的值
    for row in data:
        for i in row:
            if i == -1:
                messagebox.showerror('警告', '有值为-1的方格')
                return

    # 遍历找出起点，从起点开始计算
    for row in data:
        for i in row:
            if i == 0:
                dfs(data, data.index(row), row.index(i), ways)

    if ways:
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                buttons[i][j]['text'] = '*'
        for index, val in enumerate(ways):  # i[0]是行  i[1]是列
            data[val[0]][val[1]] = '步骤:' + str(len(ways) - index)
            buttons[val[0]][val[1]]['text'] = str(len(ways) - index)
            buttons[val[0]][val[1]]['bg'] = 'black'  # 更改途中经过按钮的背景颜色 但是api不好使
    else:
        messagebox.showinfo('致歉', '我不会')

    print(data)


# 宽高信息输入完后
def input_over():
    nums_width = entry_width.get()
    nums_height = entry_height.get()
    if nums_width.isdigit() and nums_height.isdigit():
        global data
        data = [([-1] * int(nums_width)) for i in range(int(nums_height))]
        global buttons
        buttons = [([tk.Button()] * int(nums_width)) for i in range(int(nums_height))]
        window2 = tk.Tk()
        window2.title('键入信息')
        window2.geometry('900x600')
        tk.Label(window2, text='0表示起点，1表示可以走的路径，2表示不可以走的路径   点击切换数字').grid(
            row=600,
            column=600,
            columnspan=5
        )
        for i in range(int(len(data))):
            for j in range(int(len(data[i]))):
                buttons[i][j] = MyButton(master=window2)
                buttons[i][j].grid(row=i + 1,
                                   column=j + 1,
                                   padx=10,
                                   pady=10,
                                   ipadx=5,
                                   ipady=5)
        tk.Button(window2, text='开始计算路线', command=go).grid(row=0, column=0)
        window2.mainloop()
    else:
        messagebox.showerror(title='警告', message='非法长宽')


window = tk.Tk()
window.title('一笔画完工具')
window.geometry('500x500')

text_width = tk.Label(text='宽:')
entry_width = tk.Entry()
text_height = tk.Label(text='高:')
entry_height = tk.Entry()
text_width.pack()
entry_width.pack()
text_height.pack()
entry_height.pack()

bt1 = tk.Button(text='宽高输入完成', command=input_over)
bt1.pack()

window.mainloop()
