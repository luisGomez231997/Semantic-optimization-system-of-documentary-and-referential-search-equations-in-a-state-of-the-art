from django.urls import path

from .views import *

urlpatterns = [
    # Folders
    path('folder/create/', FolderCreate.as_view()),
    path('folder/', FolderList.as_view()),
    path('folder/<pk>', FolderDetail.as_view()),
    path('folder/delete/<pk>', FolderDelete.as_view()),
    path('folder/update/<pk>', FolderUpdate.as_view()),
    path('folder/groupbyuser/<document_id>',FolderGroupByUser.as_view())
]