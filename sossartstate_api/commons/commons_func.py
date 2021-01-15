"""Libreries and imports"""
from decouple import config
from pathlib import Path
import urllib.parse as encoder
import bibtexparser
import requests
import json


class CommonsFunctions():
    """This class contain all global functions to aplication"""

    def searchInElsevier(self, query, bdreference):
        """Search documents in the BD Scopus or ScienceDirect, it make a http petiton with a query"""    
        # petition path
        path = ""
        if bdreference == "Scopus":
             path = config('ROOT_PATH_SCOPUS')
        if bdreference =="ScienceDirect":
            path = config('ROOT_PATH_SCIENCE_DIRECT')
        # petition header
        headers = {
            'Accept': 'application/json',
            'X-ELS-APIKey': config('X-ELS-APIKEY')
            }
        # petition params
        params = {
            'query': encoder.quote_plus(query), # query: equation search.
            'subj': 'COMP', # subj: area of interest
            'content': 'core', #  used to filter specific categories of content that should be searched
            'count': '25', # max number results get.
            'suppressNavLinks': True, # desactivate links.
            'sort': 'relevance', # sort the result
            'view': 'STANDARD' # i'm not allowed use the COMPLETE caracteristics.
        }
        # execute petition
        response = requests.get(path,headers=headers, params=params)
        return response.json()

    def getAbstractInfo(self, doi):
        """Receive a doi document and retrive the abstract full metadata"""
        # petition path
        path = config('ROOT_PATH_ABSTRACT')+doi
        # petition header
        headers = {
            'Accept': 'application/json',
            'X-ELS-APIKey': config('X-ELS-APIKEY')
            }
        # petition params
        params = {
            'view': 'META' # i'm not allowed use the COMPLETE caracteristics FULL, META_ABS.
        }
        # execute petition
        response = requests.get(path,headers=headers, params=params)
        return response

    def convertJsonElsevierToDictionary(self, json):
        """Receive a Json response of elsevier api and return a dictionary with bibtex structure."""
        dictionary = []
        for entry in json.get('search-results').get('entry'):
            """loop to make a dictionary by each result"""
            print(entry.get('dc:title'))
            reference = {
                "author": entry.get('dc:creator'),
                "title": entry.get('dc:title'),
                "issn": entry.get('prism:issn'),
                "note": entry.get('citedby-count'),
                "doi": entry.get('prism:doi')
            }
            dictionary.append(reference)
        return dictionary

    def convertBibtextToListDictionary(self, urlbibtex):
        """Receive a Bibtex file and convert this in a dictionary with bibtex structure."""
        dictionary = []
        with open(urlbibtex) as bibtex_file:
             bib_database = bibtexparser.load(bibtex_file)
             dictionary = bib_database.entries 
        return dictionary

    def convertDictionaryToJson(self, dictionary):
        """Convert dictionary or list of its in a json or a list of json."""
        if type(dictionary) is list:
            newdictionary = []
            for dic in dictionary:
                newdictionary.append(json.dumps(dic))
            return newdictionary
        else:
            return json.dumps(dictionary)



