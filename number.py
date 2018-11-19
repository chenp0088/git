#!/usr/bin/env python
# coding=utf-8
number = input("If you input a number ,I will tell you if the number is multiplier of ten! Please input the number: ")
number = int(number)
if number%10 == 0:
    print("It`s the multiplier of ten!")
else:
    print("It`s not the multiplier of ten!")
