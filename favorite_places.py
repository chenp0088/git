#!/usr/bin/env python
# coding=utf-8
favorite_places={
    'chenhua':['taizhou','shanghai','nanjin'],
    'wangda':['xian','changsha','beijin'],
    'xiaoyan':['henan','aiji','xinjiang'],
}
for name,place in favorite_places.items():
    for di in place:
        print name,("is like to go to "),di
