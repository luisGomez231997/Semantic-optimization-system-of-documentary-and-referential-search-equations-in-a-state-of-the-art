from .commons_func import CommonsFunctions
from spacy.lang.en import English
from spacy.lang.es import Spanish
import spacy

class AnalizerSemantic():
    """This class contain all functions with semantic methods, NER, sinonims, text minering"""

    # global variables to process the text.
    nlp = "not instace, yet."
    doc = "not instace, yet."
    commons = CommonsFunctions()

    def LoadModel(self, model):
        """ """
        if (model == "es_c"):
            self.nlp = spacy.load("es_core_news_lg")
        if (model == "en_c"):
            self.nlp = spacy.load("en_core_web_lg")
    
    def setSearchText(self, text):
        """ """
        self.doc = nlp(text)
        return commons.searchInElsevier(doc.text,"Scopus")