
"""Serializers for the File"""
from .models import  File
 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .serializers import (
    # File
    FileSerializer,
    DeleteFileSerializers,
    )


# ========== upload to file ===================================================================================
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data file"""
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            """if the file is full then save"""
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las File
class FileList(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

# Listar un File por id
class FileDetail(RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

 # Delete un File por id
class FileDelete(DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = DeleteFileSerializers
