#!/usr/bin/env python
# coding=utf-8
favorite_names = {
    'chenhua':[2,5,6],
    'wangfang':[1,33,4,55],
    'lijun':[88,100,110],
}
for name,points in favorite_names.items():
    print ("\n"+name.title()+"`s favorite points is :")
    for point in points:
        print("\t"+str(point))
