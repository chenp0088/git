#!/usr/bin/env python
# coding=utf-8
age = ("请问你的年龄多大: ")
while True:
    inputage = input(age)
    if 'quit' in inputage:
        print("程序结束")
        break
    elif int(inputage)<3:
        print("您的票价免费！")
    elif 3<=int(inputage)<=12:
        print("您的票价10美元")
    elif int(inputage)>12:
        print("您的票价15美元")
