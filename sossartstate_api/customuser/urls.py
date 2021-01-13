
from django.urls import path, re_path
from .views import *


urlpatterns = [
    # CRUD => Create, Read, Update, Delete
    path('create', UserCreate.as_view()), #ok
    path('list', UserList.as_view()),#ok
    path('get/<pk>', UserDetail.as_view()), #ok
    path('update/<pk>', UserUpdate.as_view()),#ok
    path('delete/<pk>', UserDelete.as_view()),#ok
]