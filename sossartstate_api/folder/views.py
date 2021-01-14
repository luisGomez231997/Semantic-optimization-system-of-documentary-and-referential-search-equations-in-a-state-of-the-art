
"""Serializers for the Resource"""
from .models import Folder

from file.models import File
from customuser.models import CustomUser
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .serializers import *

class FolderList(ListAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class FolderGroupByUser(ListAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def get_queryset(self):
        query = Folder.objects.filter(
            custom_user__document_id=self.kwargs['document_id']
        )
        return query

class FolderDetail(RetrieveAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class FolderCreate(ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = CreateFolderSerializer

class FolderUpdate(UpdateAPIView):
    queryset = Folder.objects.all()
    serializer_class = UpdateFolderSerializer

class FolderDelete(DestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = DeleteFolderSerializer
