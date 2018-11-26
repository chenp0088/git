#!/usr/bin/env python
# coding=utf-8
prompt = "\n请输入比萨的配料:"
prompt += "\nEnter 'quit' to end."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
