from django.urls import path
from .views import DivisionApiView 

urlpatterns = [
    path('addDivision' , DivisionApiView.as_view()),
]