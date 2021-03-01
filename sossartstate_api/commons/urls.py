
from django.urls import path
from .views import *

urlpatterns = [
    # Bibliometrics
    path('uploadbibtext/', ProcessBibtexView.as_view()),
    # Semantics
    # SearchInTheWeb
    path('sendequation/', sendSearchRefactorized.as_view()),
    path('login/', Log_in_Custom.as_view()),
    path('logout/', Log_out.as_view()),
]
