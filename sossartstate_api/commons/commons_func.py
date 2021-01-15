"""Libreries and imports"""
from decouple import config
import requests
import urllib.parse as encoder

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
        return convertJsonElsevierToDictionary(response)

    def convertJsonElsevierToDictionary(self, json):
        """Receive a Json response of elsevier api and return a dictionary with bibtex structure."""
        dictionary = {}
        return dictionary

    def convertBibtextToDictionary(self, bibtex):
        """Receive a Bibtex file and convert this in a dictionary with bibtex structure."""
        dictionary = {}
        return dictionary

    def convertDictionaryToJson(self):
        """Receive a Bibtex file and convert this in a dictionary with bibtex structure."""
        dictionary = {}
        return dictionary
