
from django.urls import path

from .views import (
                    #file
                    FileUploadView,
                    FileDetail,
                    FileList,
                    FileDelete
                    )

urlpatterns = [
    #file
    path('file/', FileUploadView.as_view()),
    path('', FileList.as_view()),
    path('<pk>', FileDetail.as_view()),
    path('delete/<pk>', FileDelete.as_view()),
    ]