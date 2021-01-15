
from django.urls import path
from .views import (ProcessBibtexView,sendSearchRefactorized)

urlpatterns = [
    #Bibliometrics
    path('uploadbibtex/', ProcessBibtexView.as_view()),
    #Semantics
    #SearchInTheWeb
    path('sendequation/', sendSearchRefactorized.as_view()),
    ]