#!/usr/bin/python3
# coding=utf-8
#该实例演示了数字猜迷游戏
number = 7
guess = -1
print("数字猜迷游戏！")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("你猜的数字太小了......")
    elif guess > number:
        print("你猜的数字太大了.....")
