
"""Serializers for the File"""
from .commons_func import  CommonsFunctions
from .bibliometric_func import AnalizerBibliometric
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
        cf = CommonsFunctions()
        ab = AnalizerBibliometric()
        obj = File.objects.get(id=request.data.get("idFile"))
        ab.extractRelevantData(cf.convertBibtextToListDictionary(obj.file.path))
        ab.getRelevantData()
        return JsonResponse(FileSerializer(obj).data)
        

        
