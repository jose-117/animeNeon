from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', MetodosPlural.as_view())
]