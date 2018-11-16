#!/usr/bin/env python
# coding=utf-8
cities={
    '泰州':{
        '所属国家':'中国',
        '人口':'1000万',
        '简介':'水乡，好吃的多',
    },
    '东京':{
        '所属国家':'日本',
        '人口':'20000万',
        '简介':'鬼子多',
    },
    '纽约':{
        '所属国家':'美国',
        '人口':'90000万',
        '简介':'洋妞多'
    },
}
for city,cities_info in cities.items():
    print ("\n城市名称："+city+"\n所属国家:"+cities_info['所属国家']+"\n人口:"+cities_info['人口']+"\n简介:"+cities_info['简介'])
