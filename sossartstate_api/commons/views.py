
"""Serializers for the File"""
from .commons_func import  CommonsFunctions
from .bibliometric_func import AnalizerBibliometric
from .semantic_module import AnalizerSemantic
from file.models import File
from file.serializers import FileSerializer 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status


class ProcessBibtexView(APIView):
    """This View, return the grouped meta-data before it's extract and agrupate."""
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """keept the data file"""
        try:
            # implements the operative classes.
            cf = CommonsFunctions()
            ab = AnalizerBibliometric()

            # get the object reference and set the path the file.
            obj = File.objects.get(id=request.data.get("idFile"))
            ab.extractRelevantData(cf.convertBibtextToListDictionary(obj.file.path))
            
            # keept and agroup the relevant information.
            ab.getRelevantData()
            return JsonResponse({"status": status.HTTP_200_OK})
        except:
            return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})

class sendSearchRefactorized(APIView):
    """This View, return the grouped meta-data before it's extract and agrupate."""
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """keept the data file"""
        try:
     
            return JsonResponse({"status": status.HTTP_200_OK})
        except:
            return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})  
