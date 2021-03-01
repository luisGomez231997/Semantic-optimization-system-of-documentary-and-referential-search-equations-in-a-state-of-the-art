
from django.urls import path

from .views import *

urlpatterns = [
    # file
    path('upload/', FileUploadView.as_view()),
    path('list', FileList.as_view()),
    path('<pk>', FileDetail.as_view()),
    path('delete/<pk>', FileDelete.as_view()),
]
