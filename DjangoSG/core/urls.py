from django.urls import path
from .views import inicio
from .views import galeria


urlpatterns=[
    path('',inicio, name="inicio"),
    path('',galeria, name="galeria"),
    
]