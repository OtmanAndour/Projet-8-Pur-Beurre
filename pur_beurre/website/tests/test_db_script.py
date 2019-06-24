""" File testing database script """

from website.db_script import api_request
import requests
import json
import codecs

from django.test import TestCase

class TestDbScript(TestCase):
    """Database tests class"""
    
#   Trying to mock, but not working
#   def test_api_request(self, monkeypatch):
#       """ Testing the OFF API request """
#       search_request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",{
#               'action': 'process',
#               'tagtype_0': 'categories', #categories selected
#               'tag_contains_0': 'contains', #contains or not
#               'sort_by': 'unique_scans_n',
#               'countries': 'France',
#               'json': 1,
#               'page': 1,
#               'page_size' : 1000
#               })
#       with codecs.open("test_off_api_request.json","w", "utf-8-sig") as f:
#           f.write(search_request.text)
#           f.close()
#       with codecs.open("test_off_api_request.json","r", "utf-8-sig") as f:
#           results = json.loads(f.read())
#
#       class MockRequestsGet:
#           def __init__(self, url, params=None):
#               pass
#           def json(self):
#               return results
#
#       monkeypatch.setattr('requests.get', MockRequestsGet)
#
#       self.assertEquals(api_request(1), results)


