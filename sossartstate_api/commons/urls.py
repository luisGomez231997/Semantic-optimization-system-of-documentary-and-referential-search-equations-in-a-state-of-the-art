
from django.urls import path
from .views import ProcessBibtexView

urlpatterns = [
    path('uploadbibtex/', ProcessBibtexView.as_view()),
    ]