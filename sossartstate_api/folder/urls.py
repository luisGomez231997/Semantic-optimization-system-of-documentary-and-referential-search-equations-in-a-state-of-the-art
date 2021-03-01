from django.urls import path

from .views import *

urlpatterns = [
    # Folders
    path('create/', FolderCreate.as_view()),
    path('list', FolderList.as_view()),
    path('<pk>', FolderDetail.as_view()),
    path('delete/<pk>', FolderDelete.as_view()),
    path('update/<pk>', FolderUpdate.as_view()),
    path('groupbyuser/<custom_user>', FolderGroupByUser.as_view())
]
