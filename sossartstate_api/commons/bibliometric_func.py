from .commons_func import CommonsFunctions
import jellyfish


class AnalizerBibliometric():
    """This class contain all functions with bibliometics methods, impact and activity"""
    commons = CommonsFunctions()  # Object to use a fuctions commons
    languages = []
    authors = []
    years = []
    affiliation = []
    #author_keywords = []
    keywords = []
    document_types = []
    abstracts = []

    def extractRelevantData(self, data):
        """This method extract all relevant metadata of bibtextfile set references"""
        alldata = []
        for listCollections in data:
            for reference in listCollections:
                self.authors.append(reference.get('author'))
                self.languages.append(reference.get('language'))
                self.years.append(reference.get('year'))
                self.affiliation.append(reference.get('affiliation'))
                # self.author_keywords.append(reference.get('author_keywords'))
                self.keywords.append(reference.get('keywords'))
                self.keywords.append(reference.get('author_keywords'))
                self.document_types.append(reference.get('document_type'))
                self.abstracts.append(reference.get('abstract'))
        self.polishedData("authors", self.authors, ". ")
        self.polishedData("affiliation", self.affiliation, "; ")
        #self.polishedData("author_keywords", self.author_keywords, "; ")
        self.polishedData("keywords", self.keywords, "; ")
        self.polishedData("keywords", self.keywords, ", ")
        self.groupKeyWordsBySimilitude()

    def polishedData(self, name_collections, array, split_text):
        """This method separated all words in a collection"""
        temp = []
        for chain in array:
            if chain != None:
                for element in chain.split(split_text):
                    if element not in temp and element != "null":
                        temp.append(element.lstrip().rstrip())
        if name_collections == "authors":
            self.authors = temp
        if name_collections == "affiliation":
            self.affiliation = temp
        # if name_collections == "author_keywords":
        #    self.author_keywords = temp
        if name_collections == "keywords":
            self.keywords = temp

    def groupKeyWordsBySimilitude(self):
        print(jellyfish.jaro_distance(u'Semantic', u'Semantic approach'))
        print(jellyfish.jaro_distance(u'Semantic', u'Semantic context'))
        print(jellyfish.jaro_distance(u'Semantic', u'Semantic interpretation'))

        print(jellyfish.jaro_distance(u'Grammar rules', u'Semantic approach'))
        print(jellyfish.jaro_distance(u'Grammar rules',
                                      u'Grammar rule inference technique'))
        print(jellyfish.jaro_distance(
            u'Grammar rules', u'Semantic interpretation'))

        print(jellyfish.jaro_distance(u'{MOOCs}', u'{CodeRunner}'))
        print(jellyfish.jaro_distance(
            u'Assessment', u'Assessment of learning'))
        print(jellyfish.jaro_distance(
            u'Assessment', u'Automated assessment'))
        print(jellyfish.jaro_distance(
            u'Assessment', u'Self-assessment'))

    def countElements(self, array):
        """This method count the elements and group its"""
        data = {}
        polished_data = []
        for element in array:
            if element not in polished_data:
                polished_data.append(element)
                data.update({
                    element: array.count(element)
                })
            else:
                continue
        return data

    def getRelevantData(self):
        """This method keep all information and send a json resum"""
        data = {
            "languages": self.countElements(self.languages),
            "authors": self.countElements(self.authors),
            "years": self.countElements(self.years),
            "affiliation": self.countElements(self.affiliation),
            # "author_keywords":  self.countElements(self.author_keywords),
            "keywords": self.countElements(self.keywords),
            "document_type": self.countElements(self.document_types)
        }
        return data
