from .commons_func import CommonsFunctions

class AnalizerBibliometric():
    """This class contain all functions with bibliometics methods, impact and activity"""

    commons = CommonsFunctions() # Object to use a fuctions commons
    languages = []
    authors = []
    years = []
    affiliation = []
    author_keywords = []
    keywords = []
    document_types = []
    abstracts = []

    def extractRelevantData(self, data):
        """This method extract all relevant metadata of bibtextfile set references"""
        for reference in data:
            self.authors.append(reference.get('author'))
            self.languages.append(reference.get('language'))
            self.years.append(reference.get('year'))
            self.affiliation.append(reference.get('affiliation'))
            self.author_keywords.append(reference.get('author_keywords'))
            self.keywords.append(reference.get('keywords'))
            self.document_types.append(reference.get('document_type'))
            self.abstracts.append(reference.get('abstract'))

    def getRelevantData(self):
        """This method keep all information and send a json resum"""
        data = {
                "languages": self.languages,
                "authors": self.authors,
                "years": self.years,
                "affiliation": self.affiliation,
                "author_keywords":  self.author_keywords,
                "keywords": self.keywords,
                "document_type": self.document_types
             }
        #print(data)
        return data

#y = AnalizerBibliometric()
#x = CommonsFunctions()
#y.extractRelevantData(x.convertBibtextToListDictionary("/mnt/c/Users/57313/Desktop/Semantic-optimization-system-of-documentary-and-referential-search-equations-in-a-state-of-the-art/sossartstate_api/media/Folders/luchogr23@gmail.com/2021-01-15_053047.4528080000"))