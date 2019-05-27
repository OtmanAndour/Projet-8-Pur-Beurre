#! /usr/bin/env python
# coding: utf-8

import requests
import json
import codecs

data = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",{
            'action': 'process',
            'tagtype_0': 'categories', #categories selected
            'tag_contains_0': 'contains', #contains or not
            'sort_by': 'unique_scans_n',
            'countries': 'France',
            'json': 1,
            'page': 1,
            'page_size' : 100,
})

response = json.loads(data.text, encoding='utf-8')

products = response["products"]

def has_nutriscore(product):
    try:
        return(product["nutrition_grade_fr"])
    except KeyError:
        try:
            return(product["nutrition_grades"])
        except KeyError:
            return False


for product in products:
    if has_nutriscore(product):
        nutriscore = has_nutriscore(product)
        print(nutriscore)
    else:
        print("Ce produit n'a pas de nutriscore")

#with codecs.open('api_test.json', 'w', encoding='utf-8') as f:
#    json.dump(data.text, f, ensure_ascii=False)