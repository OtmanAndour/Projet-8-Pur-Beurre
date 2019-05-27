#! /usr/bin/env python
# coding: utf-8

"""This file fills the Product model with products retrieved for the OFF API"""

import threading
import requests
import json
from .models import User, Product


def api_request(i):
    """Calls the OFF API and retrieves 1000 products per page"""

    data = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",{
            'action': 'process',
            'tagtype_0': 'categories', #categories selected
            'tag_contains_0': 'contains', #contains or not
            'sort_by': 'unique_scans_n',
            'countries': 'France',
            'json': 1,
            'page': i,
            'page_size' : 1000
            })
    response = json.loads(data.text, encoding='utf-8')
    return response

def product_name(product):
    """Retrieves product name"""
    try:
        name = product["product_name_fr"]
    except KeyError:
        name = product["product_name"]
    return name

def has_nutriscore(product):
    """Returns the nutriscore if the product has one, or return False"""
    try:
        return(product["nutrition_grade_fr"])
    except KeyError:
        try:
            return(product["nutrition_grades"])
        except KeyError:
            return False


def product_nutriments(product):
    """Retrieves product nutriments in a dict"""

    datas = { #An empty dict that will be filled with product nutriments
        'energy_100g' : '',
        'sugars_100g' : '',
        'salt_100g' : '',
        'fat_100g' : '',
        'saturated-fat_100g' : '',
        'sodium_100g' : '',
        'proteins_100g' : '',
        'carbohydrates_100g' : ''
    }
    for key in datas.keys():
        datas[key] = product['nutriments'][key]
    return datas

def product_infos(product):
    """Retrieves product infos, such as category, stores, etc... in a dict"""
    datas = { #An empty dict that will be filled with product infos
        'categories' : '',
        'stores' : '',
        'url' : '',
        'image_url' : '',
        'image_small_url' : '',
    }
    for key in datas.keys():
        datas[key] = product[key]
    return datas

def fill_database():
    """Fills the database with products, excluding those without a nutriscore"""
    for k in range(1500):
        count = 0
        response = api_request(k)
        if len(response) == 0:
            break
        products = response["products"]
        for product in products:
            if has_nutriscore(product):
                name = product_name(product)
                nutriscore = has_nutriscore(product)
                infos = product_infos(product)
                nutriments = product_nutriments(product)
                Product.objects.create(
                    name = name,
                    nutriscore = nutriscore,
                    category = infos.get("categories"),
                    stores = infos.get('stores'),
                    url = infos.get('url'),
                    image_url = infos.get('image_url'),
                    image_small_url = infos.get('image_small_url'),
                    energy = nutriments.get('energy_100g'),
                    sugar = nutriments.get('sugars_100g'),
                    salt = nutriments.get('salt_100g'),
                    fat = nutriments.get('fat_100g'),
                    saturated_fat = nutriments.get('saturated-fat_100g'),
                    sodium = nutriments.get('sodium_100g'),
                    proteins = nutriments.get('proteins_100g'),
                    carbohydrates = nutriments.get('carbohydrates_100g')
                )
            else:
                pass
            count+= 1
            print(count)

def main():
    fill_database()
   
main()
