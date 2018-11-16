#!/usr/bin/env python
# coding=utf-8
cities={
    'taizhou':{
        'country':'china',
        'population':'1000 million',
        'fact':'水乡，好吃的多',
    },
    'dongjin':{
        'country':'japan',
        'population':'20000 million',
        'fact':'鬼子多',
    },
    'new york':{
        'country':'america',
        'population':'90000 million',
        'fact':'洋妞多'
    },
}
for city,cities_info in cities.items():
    print("\nCitiesname: "+city)
    print ("\nCountry:"+cities_info['country'].title()+"\nPopulation:"+cities_info['population']+"\nFact:"+cities_info['fact'])
