from .commons_func import CommonsFunctions

"""document_type
 abstract
 language
 author
 note
 year"""

class AnalizerBibliometric():
    """This class contain all functions with bibliometics methods, impact and activity"""

    languages = []
    authors = []
    years = []
    affiliation = []
    author_keywords = []
    keywords = []
    document_type = []
    commons = CommonsFunctions()

    def extractRelevantData(self, data):
        """ """
        for reference in data:
            print(data.get('author'))

    def getRelevantData(self):
        """This method keep all information and send a json resum"""
        data = {
                "languages": languages,
                "authors": authors,
                "years": years,
                "affiliation": affiliation,
                "author_keywords":  author_keywords,
                "keywords": keywords,
                "document_type": document_type
             }
        return commons.convertDictionaryToJson(data)

y = AnalizerBibliometric()
x = CommonsFunctions()
y.extractRelevantData(x.convertBibtextToListDictionary("/mnt/c/Users/57313/Desktop/Semantic-optimization-system-of-documentary-and-referential-search-equations-in-a-state-of-the-art/sossartstate_api/media/Folders/luchogr23@gmail.com/2021-01-15_053047.4528080000"))